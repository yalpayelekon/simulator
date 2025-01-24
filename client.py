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

def create_ethernet_config_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_ethernet_config(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Ethernet Config query: {wrapped_msg.hex()}")
    return wrapped_msg

# Onboard Device query functions
def create_application_state_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_application_state(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Application State query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_masthead_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_devices_masthead(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Masthead query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_output_groups_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_output_groups(msg, [0])  # Query for first group
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Output Groups query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_input_groups_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_input_groups(msg, [0])  # Query for first group
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Input Groups query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_input_instance_behaviour_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_input_instance_behaviour(msg, [0])  # Query for first instance
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Input Instance Behaviour query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_output_scenes_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_output_scenes(msg, [0])  # Query for first scene
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Output Scenes query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_output_features_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_output_features(msg, [0])  # Query for first feature set
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Output Features query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_output_triac_run_methode_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_output_triac_run_methode(msg, [0])  # Query for first triac
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Output Triac Run Method query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_onboard_device_name_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_device_name(msg, [0])  # Query for first device
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Onboard Device Name query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_output_obj_feature_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_onboard_output_obj_features(msg, [0])  # Query for first object
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Output Object Feature query: {wrapped_msg.hex()}")
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
                
            # Handle Ethernet
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Eternet:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet.FB_EternetConfig:
                    config_data = msg.data.decode('ascii').strip('\0\n').split(';')
                    return (f"QUERY RESPONSE: Ethernet Config:\n"
                           f"  IP: {config_data[0]}\n"
                           f"  MAC: {config_data[1]}\n"
                           f"  Mask: {config_data[2]}\n"
                           f"  Gateway: {config_data[3]}")

            # Handle Onboard Devices
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_ApplicationState:
                    state = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Application State = {state}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_Masthead:
                    masthead = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Masthead = {masthead}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputGroups:
                    groups = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Output Groups = {groups}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_InputGroups:
                    groups = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Input Groups = {groups}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_InputInstanceBehaviour:
                    behaviors = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Input Instance Behaviours = {behaviors}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputScenes:
                    scenes = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Output Scenes = {scenes}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputFeatures:
                    features = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Output Features = {features}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputTriacRunMethode:
                    method_map = {0: "Leading", 1: "Trailing", 2: "Auto"}
                    method = method_map.get(msg.data[0], "Unknown")
                    return f"QUERY RESPONSE: Output Triac Run Method = {method}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_DeviceName:
                    name = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Onboard Device Name = {name}"

                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputObjFeature:
                    features = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: Output Object Features = {features}"
                
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
    print("  12 - Send Ethernet Config query")
    print("  13 - Send Application State query")
    print("  14 - Send Masthead query")
    print("  15 - Send Output Groups query")
    print("  16 - Send Input Groups query")
    print("  17 - Send Input Instance Behaviour query")
    print("  18 - Send Output Scenes query")
    print("  19 - Send Output Features query")
    print("  20 - Send Output Triac Run Method query")
    print("  21 - Send Onboard Device Name query")
    print("  22 - Send Output Object Feature query")
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
            elif command == '12':
                query = create_ethernet_config_query()
            elif command == '13':
                query = create_application_state_query()
            elif command == '14':
                query = create_masthead_query()
            elif command == '15':
                query = create_output_groups_query()
            elif command == '16':
                query = create_input_groups_query()
            elif command == '17':
                query = create_input_instance_behaviour_query()
            elif command == '18':
                query = create_output_scenes_query()
            elif command == '19':
                query = create_output_features_query()
            elif command == '20':
                query = create_output_triac_run_methode_query()
            elif command == '21':
                query = create_onboard_device_name_query()
            elif command == '22':
                query = create_output_obj_feature_query()

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