from priority_message import PRIORITY_QUERY, PRIORITY_EVENT

def process_message_queue(message_queue, rcu_simulator):
    while True:
        try:
            priority_message = message_queue.get()
            
            if not priority_message.client_socket._closed:
                if priority_message.priority == PRIORITY_QUERY:
                    print("\nProcessing query message...")
                    response = rcu_simulator.handle_query(priority_message.message)
                    if response:
                        print(f"Sending response: {response.hex()}")
                        priority_message.client_socket.send(response)  # Send the wrapped response directly
                
                elif priority_message.priority == PRIORITY_EVENT:
                    print("\nProcessing event message...")
                    wrapped_message = priority_message.message.Wrap()
                    print(f"Sending event: {wrapped_message.hex()}")
                    priority_message.client_socket.send(wrapped_message)
            
            message_queue.task_done()
            
        except Exception as e:
            print(f"Error processing message: {str(e)}")
            if "Bad file descriptor" not in str(e):
                print(f"Exception details: {e}")