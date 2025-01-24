import socket
import threading
import random
import time
from query_generators import query_functions
from message_parser import parse_message

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            parsed_message = parse_message(message)
            print(parsed_message)
            
        except Exception as e:
            print(f"Error receiving message: {str(e)}")
            break
    client_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5001))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    print("\nConnected to server. Starting automated query test...")

    try:
        for query_name, query_func in query_functions.items():
            delay = random.uniform(0, 2)
            
            print(f"\nSending {query_name} query...")
            query = query_func()
            client_socket.send(query)
            
            print(f"Waiting {delay:.2f} seconds...")
            time.sleep(delay)

        print("\nAll queries sent. Waiting for final responses...")
        time.sleep(2)
        
    except Exception as e:
        print(f"\nError during testing: {str(e)}")
    finally:
        print("\nDisconnecting from server...")
        client_socket.close()

if __name__ == "__main__":
    run_client()