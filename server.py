import socket
import threading
import time
import random
import queue
from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants
from rcu_lib_module.RCU_protocol_ring_buffer import RCU_Msg_RingBuffer
from RCU_API_extended import RCU_API_Extended

PRIORITY_QUERY = 1
PRIORITY_EVENT = 2

class PriorityMessage:
    def __init__(self, priority, message: RCU_MessageStructure, client_socket=None):
        self.priority = priority
        self.message = message
        self.client_socket = client_socket
        self.timestamp = time.time()

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp

class RCUSimulator:
    def __init__(self):
        self.message_queue = queue.PriorityQueue()
        self.ring_buffer = RCU_Msg_RingBuffer(100)
        
    def create_event_onboard_inputs(self):
        msg = RCU_MessageStructure()
        short_address = random.randint(65, 76)
        signal_type = random.randint(0, 255)
        data = bytes([short_address, signal_type])
        print(f"Creating event with address={short_address}, signal={signal_type}")
        
        msg.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Events
        msg.cmd_no = RCU_MessageStructureConstants.CMD_No.OnboardDevice
        msg.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice.InputEvents
        msg.data = data
        
        wrapped_msg = msg.Wrap()
        print(f"Created event message: {wrapped_msg.hex()}")
        print(f"Message details - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
        print(f"Data: {msg.data.hex()}")
        return msg
    
    def create_event_dali_digidim_inputs(self):
        msg = RCU_MessageStructure()
        input_address = random.randint(0, 15)  # DALI input device address (0-15)
        input_state = random.randint(0, 1)     # Input state (0=OFF, 1=ON)
        data = bytes([input_address, input_state])
        print(f"Creating DALI Digidim input event with address={input_address}, state={input_state}")
        
        msg.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Events
        msg.cmd_no = RCU_MessageStructureConstants.CMD_No.DALI
        msg.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.DigidimEvents
        msg.data = data
        
        wrapped_msg = msg.Wrap()
        print(f"Created DALI Digidim event message: {wrapped_msg.hex()}")
        print(f"Message details - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
        print(f"Data: {msg.data.hex()}")
        return msg

    def create_event_dali_initialization_finished(self):
        msg = RCU_MessageStructure()
        status = random.randint(0, 1)  # 0=Success, 1=Error
        data = bytes([status])
        print(f"Creating DALI initialization finished event with status={status}")
        
        msg.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Events
        msg.cmd_no = RCU_MessageStructureConstants.CMD_No.DALI
        msg.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.InitializationProcessFinished
        msg.data = data
        
        wrapped_msg = msg.Wrap()
        print(f"Created DALI initialization finished event message: {wrapped_msg.hex()}")
        print(f"Message details - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
        print(f"Data: {msg.data.hex()}")
        return msg

    def create_event_dali_scan_reset_finished(self):
        msg = RCU_MessageStructure()
        status = random.randint(0, 1)  # 0=Success, 1=Error
        devices_found = random.randint(0, 64)  # Number of DALI devices found
        data = bytes([status, devices_found])
        print(f"Creating DALI scan/reset finished event with status={status}, devices={devices_found}")
        
        msg.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Events
        msg.cmd_no = RCU_MessageStructureConstants.CMD_No.DALI
        msg.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.ScanAndResetProcessFinished
        msg.data = data
        
        wrapped_msg = msg.Wrap()
        print(f"Created DALI scan/reset finished event message: {wrapped_msg.hex()}")
        print(f"Message details - Type: {msg.cmd_type_no.name}, CMD: {msg.cmd_no.name}, SubCMD: {msg.sub_cmd_no.name}")
        print(f"Data: {msg.data.hex()}")
        return msg

    def handle_query(self, query_msg: RCU_MessageStructure):
        print(f"\nHandling query - Type: {query_msg.cmd_type_no.name}, CMD: {query_msg.cmd_no.name}, SubCMD: {query_msg.sub_cmd_no.name}")
        response_msg = RCU_MessageStructure()

        if (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.General):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_GTIN:
                gtin = f"GTIN{random.randint(1000, 9999)}".encode('ascii')
                print(f"Generated GTIN response: {gtin.decode()}")
                RCU_API_Extended.FB_device_GTIN(response_msg, gtin)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Serial_Number:
                serial = f"SN{random.randint(10000, 99999)}".encode('ascii')
                print(f"Generated Serial Number response: {serial.decode()}")
                RCU_API_Extended.FB_device_serial_number(response_msg, serial)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Software_Version:
                version = f"V{random.randint(1,9)}.{random.randint(0,9)}.{random.randint(0,9)}".encode('ascii')
                print(f"Generated Version response: {version.decode()}")
                RCU_API_Extended.FB_software_version(response_msg, version)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Hardware_Version:
                hw_version = f"HW{random.randint(1,9)}.{random.randint(0,9)}".encode('ascii')
                print(f"Generated Hardware Version response: {hw_version.decode()}")
                RCU_API_Extended.FB_hardware_version(response_msg, hw_version)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_SW_Commit_SHA:
                commit_sha = f"{hex(random.randint(0, 16**40))[2:].zfill(40)}".encode('ascii')
                print(f"Generated SW Commit SHA response: {commit_sha.decode()}")
                RCU_API_Extended.FB_SW_commit_SHA(response_msg, commit_sha)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_SW_Author:
                authors = ["john.doe", "jane.smith", "bob.wilson", "alice.johnson"]
                author = random.choice(authors).encode('ascii')
                print(f"Generated SW Author response: {author.decode()}")
                RCU_API_Extended.FB_SW_author(response_msg, author)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Last_Commit_Date:
                date = f"20{random.randint(20,23)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}".encode('ascii')
                print(f"Generated Last Commit Date response: {date.decode()}")
                RCU_API_Extended.FB_last_commit_date(response_msg, date)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_PowerSourcePeriod:
                period = str(random.randint(45, 65)).encode('ascii')  # Hz
                print(f"Generated Power Source Period response: {period.decode()}Hz")
                RCU_API_Extended.FB_power_source_period(response_msg, period)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_DeviceName:
                device_names = ["RCU_Main", "RCU_Backup", "RCU_Test", "RCU_Debug"]
                name = random.choice(device_names).encode('ascii')
                print(f"Generated Device Name response: {name.decode()}")
                RCU_API_Extended.FB_device_name(response_msg, name)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_HardFault1:
                fault_data = bytes([random.randint(0, 255) for _ in range(4)])  # 4 bytes of fault data
                print(f"Generated HardFault1 response: {fault_data.hex()}")
                RCU_API_Extended.FB_hardfault_1(response_msg, fault_data)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_DatabaseInfo:
                db_info = f"DB_Ver_{random.randint(1,9)}.{random.randint(0,9)}".encode('ascii')
                print(f"Generated Database Info response: {db_info.decode()}")
                RCU_API_Extended.FB_database_info(response_msg, db_info)

        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
          query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Eternet):
        
            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet.Q_EternetConfig:
                # Generate sample Ethernet config (IP, MAC, etc.)
                config = {
                    'ip': f"192.168.{random.randint(1,254)}.{random.randint(1,254)}",
                    'mac': ':'.join([f"{random.randint(0,255):02x}" for _ in range(6)]),
                    'mask': "255.255.255.0",
                    'gateway': "192.168.1.1"
                }
                config_str = f"{config['ip']};{config['mac']};{config['mask']};{config['gateway']}".encode('ascii')
                print(f"Generated Ethernet config response: {config_str.decode()}")
                RCU_API_Extended.FB_ethernet_config(response_msg, config_str)

            # Handle Onboard Device queries
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice):
            
            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_ApplicationState:
                    state = random.choice([b"RUNNING", b"IDLE", b"ERROR", b"INIT"])
                    print(f"Generated Application State response: {state.decode()}")
                    RCU_API_Extended.FB_application_state(response_msg, state)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_Masthead:
                masthead = f"RCU-{random.randint(1000,9999)}".encode('ascii')
                print(f"Generated Masthead response: {masthead.decode()}")
                RCU_API_Extended.FB_masthead(response_msg, masthead)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputGroups:
                groups = bytes([random.randint(0,255) for _ in range(4)])  # 4 output groups
                print(f"Generated Output Groups response: {groups.hex()}")
                RCU_API_Extended.FB_output_groups(response_msg, groups)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_InputGroups:
                groups = bytes([random.randint(0,255) for _ in range(4)])  # 4 input groups
                print(f"Generated Input Groups response: {groups.hex()}")
                RCU_API_Extended.FB_input_groups(response_msg, groups)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_InputInstanceBehaviour:
                behavior = bytes([random.randint(0,3) for _ in range(8)])  # 8 instances
                print(f"Generated Input Instance Behaviour response: {behavior.hex()}")
                RCU_API_Extended.FB_input_instance_behaviour(response_msg, behavior)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputScenes:
                scenes = bytes([random.randint(0,100) for _ in range(16)])  # 16 scenes
                print(f"Generated Output Scenes response: {scenes.hex()}")
                RCU_API_Extended.FB_output_scenes(response_msg, scenes)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputFeatures:
                features = bytes([random.randint(0,255) for _ in range(4)])
                print(f"Generated Output Features response: {features.hex()}")
                RCU_API_Extended.FB_output_features(response_msg, features)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputTriacRunMethode:
                method = bytes([random.randint(0,2)])  # 0=Leading, 1=Trailing, 2=Auto
                print(f"Generated Output Triac Run Method response: {method.hex()}")
                RCU_API_Extended.FB_output_triac_run_methode(response_msg, method)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_DeviceName:
                name = f"ONBOARD-{random.randint(1,999):03d}".encode('ascii')
                print(f"Generated Onboard Device Name response: {name.decode()}")
                RCU_API_Extended.FB_onboard_device_name(response_msg, name)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputObjFeature:
                features = bytes([random.randint(0,255) for _ in range(4)])
                print(f"Generated Output Object Features response: {features.hex()}")
                RCU_API_Extended.FB_output_obj_feature(response_msg, features)
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
          query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.RTC):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_RtcTimeAndDate:
                time_date = time.strftime("%Y-%m-%d %H:%M:%S").encode('ascii')
                print(f"Generated RTC Time and Date response: {time_date.decode()}")
                RCU_API_Extended.FB_RTC_time_and_date(response_msg, time_date)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_GMT:
                gmt_offset = "+02:00".encode('ascii')  # Example GMT offset
                print(f"Generated GMT response: {gmt_offset.decode()}")
                RCU_API_Extended.FB_GMT(response_msg, gmt_offset)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_LatitudeAndLongtude:
                coords = "51.5074,0.1278".encode('ascii')  # Example coordinates
                print(f"Generated Latitude/Longitude response: {coords.decode()}")
                RCU_API_Extended.FB_latitude_and_longitude(response_msg, coords)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_SunriseTime:
                sunrise = "06:30".encode('ascii')
                print(f"Generated Sunrise Time response: {sunrise.decode()}")
                RCU_API_Extended.FB_sunrise_time(response_msg, sunrise)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_SunsetTime:
                sunset = "20:15".encode('ascii')
                print(f"Generated Sunset Time response: {sunset.decode()}")
                RCU_API_Extended.FB_sunset_time(response_msg, sunset)

    # Handle DALI queries
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DALI):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DiscoveredDevNumberAndAddress:
                device_info = bytes([random.randint(1, 64), random.randint(0, 63)])  # [device_count, start_address]
                print(f"Generated DALI Device Discovery response: Count={device_info[0]}, StartAddr={device_info[1]}")
                RCU_API_Extended.FB_dali_device_discovered_sadd(response_msg, device_info)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DaliDeviceObjMastHead:
                masthead = f"DALI_DEV_{random.randint(1,999):03d}".encode('ascii')
                print(f"Generated DALI Device Masthead response: {masthead.decode()}")
                RCU_API_Extended.FB_dali_device_masthead(response_msg, masthead)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearNvmContent:
                nvm_data = bytes([random.randint(0, 255) for _ in range(16)])
                print(f"Generated DALI Gear NVM Content response: {nvm_data.hex()}")
                RCU_API_Extended.FB_dali_gear_nvm_content(response_msg, nvm_data)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearRamContent:
                ram_data = bytes([random.randint(0, 255) for _ in range(16)])
                print(f"Generated DALI Gear RAM Content response: {ram_data.hex()}")
                RCU_API_Extended.FB_dali_gear_ram_content(response_msg, ram_data)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_InputNvmContent:
                input_data = bytes([random.randint(0, 255) for _ in range(8)])
                print(f"Generated DALI Input NVM Content response: {input_data.hex()}")
                RCU_API_Extended.FB_dali_input_nvm_content(response_msg, input_data)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DeviceObjName:
                name = f"DALI_{random.randint(1,999):03d}".encode('ascii')
                print(f"Generated DALI Device Object Name response: {name.decode()}")
                RCU_API_Extended.FB_dali_device_obj_name(response_msg, name)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearObjFeature:
                features = bytes([random.randint(0, 255) for _ in range(4)])
                print(f"Generated DALI Gear Feature response: {features.hex()}")
                RCU_API_Extended.FB_dali_gear_feature(response_msg, features)

        # Handle Occupancy queries
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Occupancy):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_Duration:
                duration = str(random.randint(30, 300)).encode('ascii')  # 30-300 seconds
                print(f"Generated Occupancy Duration response: {duration.decode()} seconds")
                RCU_API_Extended.FB_ocuupancy_duration(response_msg, duration)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_occupancy_room_situation:
                situation = random.choice([b"OCCUPIED", b"VACANT", b"UNKNOWN"])
                print(f"Generated Room Situation response: {situation.decode()}")
                RCU_API_Extended.FB_occupancy_room_situation(response_msg, situation)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_occupancy_door_position:
                position = random.choice([b"OPEN", b"CLOSED", b"UNKNOWN"])
                print(f"Generated Door Position response: {position.decode()}")
                RCU_API_Extended.FB_occupancy_door_position(response_msg, position)

        # Handle DND_App queries
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.DND_App):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App.Q_dndapp_summary:
                summary = f"DND_STATUS_{random.choice(['ACTIVE', 'INACTIVE'])}".encode('ascii')
                print(f"Generated DND App Summary response: {summary.decode()}")
                RCU_API_Extended.FB_dndapp_summary(response_msg, summary)

        # Handle Modbus queries
        elif (query_msg.cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query and
            query_msg.cmd_no == RCU_MessageStructureConstants.CMD_No.Modbus):

            if query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.Q_modbus_device_masthead:
                masthead = f"MODBUS_DEV_{random.randint(1,999):03d}".encode('ascii')
                print(f"Generated Modbus Device Masthead response: {masthead.decode()}")
                RCU_API_Extended.FB_modbus_device_masthead(response_msg, masthead)

            elif query_msg.sub_cmd_no == RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.Q_modbus_dev_register_address_for_event:
                reg_addr = bytes([random.randint(0, 255) for _ in range(2)])  # 2-byte register address
                print(f"Generated Modbus Device Register Address response: {reg_addr.hex()}")
                RCU_API_Extended.FB_modbus_device_reg_add(response_msg, reg_addr)

        if response_msg.cmd_type_no:
            print(f"Response message: {response_msg.Wrap().hex()}")
            return response_msg

        return None

def process_message_queue(message_queue, rcu_simulator):
    while True:
        try:
            priority_message = message_queue.get()
            
            if not priority_message.client_socket._closed:
                if priority_message.priority == PRIORITY_QUERY:
                    print("\nProcessing query message...")
                    response = rcu_simulator.handle_query(priority_message.message)
                    if response:
                        wrapped_response = response.Wrap()
                        print(f"Sending response: {wrapped_response.hex()}")
                        priority_message.client_socket.send(wrapped_response)
                
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