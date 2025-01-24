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

# RTC Query Functions
def create_rtc_time_date_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_rtc_time_and_date(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated RTC Time and Date query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_gmt_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_gmt(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated GMT query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_latitude_longitude_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_latitude_and_longitude(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Latitude/Longitude query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_sunrise_time_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_sunrise_time(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Sunrise Time query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_sunset_time_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_sunset_time(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Sunset Time query: {wrapped_msg.hex()}")
    return wrapped_msg

# DALI Query Functions
def create_dali_discovered_devices_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_discovered_devices(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Discovered Devices query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_device_masthead_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_device_masthead(msg, bytes([0]))  # Query for first device
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Device Masthead query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_gear_nvm_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_gear_nvm_content(msg, bytes([0]))  # Query for first gear
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Gear NVM query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_gear_ram_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_gear_ram_content(msg, bytes([0]))  # Query for first gear
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Gear RAM query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_input_nvm_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_input_nvm_content(msg, bytes([0]))  # Query for first input
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Input NVM query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_device_name_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_device_obj_name(msg, bytes([0]))  # Query for first device
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Device Name query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_dali_gear_feature_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dali_gear_feature(msg, bytes([0]))  # Query for first gear
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DALI Gear Feature query: {wrapped_msg.hex()}")
    return wrapped_msg

# Occupancy Query Functions
def create_occupancy_duration_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_ocuupancy_duration(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Occupancy Duration query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_room_situation_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_occupancy_room_situation(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Room Situation query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_door_position_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_occupancy_door_position(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Door Position query: {wrapped_msg.hex()}")
    return wrapped_msg

# DND App Query Function
def create_dnd_summary_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_dndapp_summary(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated DND Summary query: {wrapped_msg.hex()}")
    return wrapped_msg

# Modbus Query Functions
def create_modbus_device_masthead_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_modbus_device_masthead(msg, bytes([0]))  # Query for first device
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Modbus Device Masthead query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_modbus_register_address_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_modbus_device_reg_add(msg, bytes([0]))  # Query for first register
    wrapped_msg = msg.Wrap()
    print(f"\nCreated Modbus Register Address query: {wrapped_msg.hex()}")
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
            # Handle Onboard Device Input Events
            if (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice and 
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice.InputEvents):
                if len(msg.data) >= 2:
                    short_address = msg.data[0]
                    signal_type = msg.data[1]
                    addr_char = chr(short_address) if 65 <= short_address <= 76 else f"0x{short_address:02x}"
                    return f"EVENT: Onboard Input from address {addr_char} ({short_address:02x}), signal type {signal_type} (0x{signal_type:02x})"
                return f"EVENT: Invalid Onboard Input data length: {msg.data.hex()}"

            # Handle DALI Digidim Input Events
            elif (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DALI and
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.DigidimEvents):
                if len(msg.data) >= 2:
                    input_address = msg.data[0]
                    input_state = msg.data[1]
                    state_str = "ON" if input_state == 1 else "OFF"
                    return f"EVENT: DALI Digidim Input address {input_address} state changed to {state_str}"
                return f"EVENT: Invalid DALI Digidim Input data length: {msg.data.hex()}"

            # Handle DALI Initialization Finished Events
            elif (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DALI and
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.InitializationProcessFinished):
                if len(msg.data) >= 1:
                    status = msg.data[0]
                    status_str = "Success" if status == 0 else "Error"
                    return f"EVENT: DALI Initialization Process Finished with status: {status_str}"
                return f"EVENT: Invalid DALI Initialization data length: {msg.data.hex()}"

            # Handle DALI Scan and Reset Finished Events
            elif (msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DALI and
                msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.ScanAndResetProcessFinished):
                if len(msg.data) >= 2:
                    status = msg.data[0]
                    devices_found = msg.data[1]
                    status_str = "Success" if status == 0 else "Error"
                    return f"EVENT: DALI Scan/Reset Process Finished - Status: {status_str}, Devices Found: {devices_found}"
                return f"EVENT: Invalid DALI Scan/Reset data length: {msg.data.hex()}"

            return f"EVENT: Unknown event type: CMD={msg.cmd_no.name}, SubCMD={msg.sub_cmd_no.name}"
                
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

            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.RTC:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_RtcTimeAndDate:
                    time_date = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: RTC Time and Date = {time_date}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_GMT:
                    gmt = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: GMT Offset = {gmt}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_LatitudeAndLongtude:
                    coords = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Latitude/Longitude = {coords}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_SunriseTime:
                    sunrise = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Sunrise Time = {sunrise}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_SunsetTime:
                    sunset = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Sunset Time = {sunset}"

            # Handle DALI responses
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DALI:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DiscoveredDevNumberAndAddress:
                    count, addr = msg.data[0], msg.data[1]
                    return f"QUERY RESPONSE: DALI Discovered Devices = Count: {count}, Start Address: {addr}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DaliDeviceObjMastHead:
                    masthead = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: DALI Device Masthead = {masthead}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearNvmContent:
                    nvm = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: DALI Gear NVM Content = {nvm}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearRamContent:
                    ram = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: DALI Gear RAM Content = {ram}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_InputNvmContent:
                    input_nvm = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: DALI Input NVM Content = {input_nvm}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DeviceObjName:
                    name = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: DALI Device Name = {name}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearFeature:
                    features = ' '.join([f"0x{b:02x}" for b in msg.data])
                    return f"QUERY RESPONSE: DALI Gear Features = {features}"

            # Handle Occupancy responses
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Occupancy:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_Duration:
                    duration = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Occupancy Duration = {duration} seconds"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_occupancy_room_situation:
                    situation = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Room Situation = {situation}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_occupancy_door_position:
                    position = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Door Position = {position}"

            # Handle DND App responses
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DND_App:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App.FB_dndapp_summary:
                    summary = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: DND Summary = {summary}"

            # Handle Modbus responses
            elif msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Modbus:
                if msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.FB_modbus_device_masthead:
                    masthead = msg.data.decode('ascii').strip('\0\n')
                    return f"QUERY RESPONSE: Modbus Device Masthead = {masthead}"
                
                elif msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.FB_modbus_dev_register_address_for_event:
                    reg_addr = int.from_bytes(msg.data, 'little')
                    return f"QUERY RESPONSE: Modbus Register Address = 0x{reg_addr:04x}"
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
    print("  23 - Send RTC Time and Date query")
    print("  24 - Send GMT query")
    print("  25 - Send Latitude/Longitude query")
    print("  26 - Send Sunrise Time query")
    print("  27 - Send Sunset Time query")
    print("  28 - Send DALI Discovered Devices query")
    print("  29 - Send DALI Device Masthead query")
    print("  30 - Send DALI Gear NVM query")
    print("  31 - Send DALI Gear RAM query")
    print("  32 - Send DALI Input NVM query")
    print("  33 - Send DALI Device Name query")
    print("  34 - Send DALI Gear Feature query")
    print("  35 - Send Occupancy Duration query")
    print("  36 - Send Room Situation query")
    print("  37 - Send Door Position query")
    print("  38 - Send DND Summary query")
    print("  39 - Send Modbus Device Masthead query")
    print("  40 - Send Modbus Register Address query")
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
            elif command == '23':
                query = create_rtc_time_date_query()
            elif command == '24':
                query = create_gmt_query()
            elif command == '25':
                query = create_latitude_longitude_query()
            elif command == '26':
                query = create_sunrise_time_query()
            elif command == '27':
                query = create_sunset_time_query()
            elif command == '28':
                query = create_dali_discovered_devices_query()
            elif command == '29':
                query = create_dali_device_masthead_query()
            elif command == '30':
                query = create_dali_gear_nvm_query()
            elif command == '31':
                query = create_dali_gear_ram_query()
            elif command == '32':
                query = create_dali_input_nvm_query()
            elif command == '33':
                query = create_dali_device_name_query()
            elif command == '34':
                query = create_dali_gear_feature_query()
            elif command == '35':
                query = create_occupancy_duration_query()
            elif command == '36':
                query = create_room_situation_query()
            elif command == '37':
                query = create_door_position_query()
            elif command == '38':
                query = create_dnd_summary_query()
            elif command == '39':
                query = create_modbus_device_masthead_query()
            elif command == '40':
                query = create_modbus_register_address_query()

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