import socket
import threading
import time
import random
import queue
from rcu_lib_module.RCU_protocol import RCU_MessageStructure
from priority_message import PriorityMessage, PRIORITY_QUERY, PRIORITY_EVENT
from rcu_simulator import RCUSimulator
from message_processor import process_message_queue

def handle_client(client_socket, addr, message_queue, rcu_simulator):
    print(f"\nNew connection from {addr}")
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            print(f"\nReceived data: {data.hex()}")
            msg = RCU_MessageStructure()
            if msg.Parse(data):
                print(f"Parsed message - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
                priority_message = PriorityMessage(PRIORITY_QUERY, msg, client_socket)
                message_queue.put(priority_message)
            else:
                print("Failed to parse message")
            
    except Exception as e:
        print(f"Error in client handler: {str(e)}")
    finally:
        client_socket.close()
        print(f"\nConnection from {addr} closed")

def send_events(client_socket, message_queue, rcu_simulator):
    try:
        while not client_socket._closed:
            # Randomly choose which event to send
            event_type = random.randint(0, 3)
            
            if event_type == 0:
                event_message = rcu_simulator.create_event_onboard_inputs()
            elif event_type == 1:
                event_message = rcu_simulator.create_event_dali_digidim_inputs()
            elif event_type == 2:
                event_message = rcu_simulator.create_event_dali_initialization_finished()
            else:  # event_type == 3
                event_message = rcu_simulator.create_event_dali_scan_reset_finished()
            
            priority_message = PriorityMessage(PRIORITY_EVENT, event_message, client_socket)
            message_queue.put(priority_message)
            
            # Random delay between 5 and 10 seconds between events
            delay = random.uniform(1.0, 3.0)
            time.sleep(delay)
            
    except Exception as e:
        if not client_socket._closed:
            print(f"Error in event sender: {str(e)}")

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(5)
    print("\nServer is listening on localhost:5001")

    message_queue = queue.PriorityQueue()
    rcu_simulator = RCUSimulator()

    NUM_PROCESSOR_THREADS = 3
    processor_threads = []
    for i in range(NUM_PROCESSOR_THREADS):
        processor = threading.Thread(target=process_message_queue, 
                                  args=(message_queue, rcu_simulator))
        processor.daemon = True
        processor.start()
        processor_threads.append(processor)
        print(f"Started processor thread {i+1}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            
            client_handler = threading.Thread(target=handle_client, 
                                           args=(client_socket, addr, message_queue, rcu_simulator))
            event_sender = threading.Thread(target=send_events, 
                                         args=(client_socket, message_queue, rcu_simulator))
            
            client_handler.daemon = True
            event_sender.daemon = True
            
            client_handler.start()
            event_sender.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()