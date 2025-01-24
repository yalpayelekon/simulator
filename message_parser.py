from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants

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