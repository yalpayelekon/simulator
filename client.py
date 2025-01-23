import socket
import threading
from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants
from rcu_lib_module.RCU_API import RCU_API

def create_gtin_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_device_GTIN(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated GTIN query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_serial_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_device_serial_number(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Serial Number query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_version_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_software_version(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Version query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_hardware_version_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_hardware_version(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Hardware Version query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_sw_commit_sha_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_SW_commit_SHA(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated SW Commit SHA query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_sw_author_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_SW_author(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated SW Author query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_last_commit_date_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_Last_commit_date(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Last Commit Date query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_power_source_period_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_power_source_period(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Power Source Period query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_device_name_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_device_name(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Device Name query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_hardfault1_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_hardfault_1_reg(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Hardfault1 query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_database_info_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_database_info(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Database Info query: {wrapped_msg.hex()}")
    return wrapped_msg

def parse_message(message_bytes):
    try:
        print(f"\nParsing message: {message_bytes.hex()}")
        msg = RCU_MessageStructure()
        if not msg.Parse(message_bytes):
            print("Failed to parse message")
            return f"Failed to parse message: {message_bytes.hex()}"
        
        print(f"Parsed message - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")

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
            if msg.cmd_no == RCU_MessageStructureConstants.CMD_No.General:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_GTIN:
                    gtin_data = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: GTIN = {gtin_data}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Serial_Number:
                    sn_data = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Serial Number = {sn_data}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Software_Version:
                    version_data = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Version = {version_data}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Hardware_Version:
                    hw_version = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Hardware Version = {hw_version}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_SW_Commit_SHA:
                    commit_sha = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: SW Commit SHA = {commit_sha}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_SW_Author:
                    author = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: SW Author = {author}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Last_Commit_Date:
                    date = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Last Commit Date = {date}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_PowerSourcePeriod:
                    period = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Power Source Period = {period}Hz"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_DeviceName:
                    name = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Device Name = {name}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_HardFault1:
                    fault_data = msg.data.hex()
                    return f"QUERY RESPONSE: HardFault1 Register = 0x{fault_data}"
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_DatabaseInfo:
                    db_info = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Database Info = {db_info}"
                
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

    print("\nConnected to server.")
    print("Commands:")
    print("  1 - Send GTIN query")
    print("  2 - Send Serial Number query")
    print("  3 - Send Version query")
    print("  4 - Send Hardware Version query")
    print("  5 - Send SW Commit SHA query")
    print("  6 - Send SW Author query")
    print("  7 - Send Last Commit Date query")
    print("  8 - Send Power Source Period query")
    print("  9 - Send Device Name query")
    print("  10 - Send Hardfault1 query")
    print("  11 - Send Database Info query")
    print("  q - Quit")

    try:
        while True:
            command = input("Enter command: ")
            if command.lower() == 'q':
                break
            query = None
            if command == '1':
                query = create_gtin_query()
            elif command == '2':
                query = create_serial_query()
            elif command == '3':
                query = create_version_query()
            elif command == '4':
                query = create_hardware_version_query()
            elif command == '5':
                query = create_sw_commit_sha_query()
            elif command == '6':
                query = create_sw_author_query()
            elif command == '7':
                query = create_last_commit_date_query()
            elif command == '8':
                query = create_power_source_period_query()
            elif command == '9':
                query = create_device_name_query()
            elif command == '10':
                query = create_hardfault1_query()
            elif command == '11':
                query = create_database_info_query()

            if query:
                client_socket.send(query)
                print("Query sent")
            else:
                print("Invalid command")
    except KeyboardInterrupt:
        print("\nDisconnecting from server...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()