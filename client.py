import socket
import threading
from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants
from rcu_lib_module.RCU_API import RCU_API

def create_gtin_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_device_GTIN(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated GTIN query: {wrapped_msg.hex()}")
    print(f"Message details - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
    return wrapped_msg

def parse_message(message_bytes):
    try:
        print(f"\nParsing message: {message_bytes.hex()}")
        msg = RCU_MessageStructure()
        if not msg.Parse(message_bytes):
            print("Failed to parse message")
            return f"Failed to parse message: {message_bytes.hex()}"
        
        print(f"Parsed message - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
        print(f"Data: {msg.data.hex() if msg.data else 'None'}")
            
        if msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Events:
            if (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice and 
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice.InputEvents):
                if len(msg.data) >= 2:
                    short_address = msg.data[0]
                    signal_type = msg.data[1]
                    addr_char = chr(short_address) if 65 <= short_address <= 76 else f"0x{short_address:02x}"
                    return f"EVENT: Input from address {addr_char} ({short_address:02x}), signal type {signal_type} (0x{signal_type:02x})"
                return f"EVENT: Invalid data length: {msg.data.hex()}"
                
        elif msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query:
            if (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.General and 
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_GTIN):
                gtin_data = msg.data.decode('ascii').strip('\0\n')
                return f"QUERY RESPONSE: GTIN = {gtin_data}"
            return f"QUERY: Unknown sub-command: {msg.sub_cmd_no.name}"
                
        return f"Unknown message type: {msg.cmd_type_no.name}"
    except Exception as e:
        print(f"Error parsing message: {str(e)}")
        print(f"Message bytes: {message_bytes.hex()}")
        import traceback
        traceback.print_exc()
        return f"Error parsing message: {message_bytes.hex()}"

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            parsed_message = parse_message(message)
            print(f"Received: {parsed_message}")
            
        except Exception as e:
            print(f"Error receiving message: {str(e)}")
            break
    client_socket.close()

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    print("\nConnected to server.")
    print("Press Enter to send GTIN query, 'q' to quit")

    try:
        while True:
            command = input()
            if command.lower() == 'q':
                break
            
            query = create_gtin_query()
            client_socket.send(query)
            print("Sent GTIN query")
            
    except KeyboardInterrupt:
        print("\nDisconnecting from server...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()