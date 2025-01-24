from rcu_lib_module.RCU_protocol import RCU_MessageStructure
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
    RCU_API.Q_RTC_time_and_date(msg, bytes([]))
    wrapped_msg = msg.Wrap()
    print(f"\nCreated RTC Time and Date query: {wrapped_msg.hex()}")
    return wrapped_msg

def create_gmt_query():
    msg = RCU_MessageStructure()
    RCU_API.Q_GMT(msg, bytes([]))
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
    RCU_API.Q_dali_device_discovered_sadd(msg, bytes([]))
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

query_functions = {
        'GTIN': create_gtin_query,
        'Serial Number': create_serial_query,
        'Version': create_version_query,
        'Hardware Version': create_hardware_version_query,
        'SW Commit SHA': create_sw_commit_sha_query,
        'SW Author': create_sw_author_query,
        'Last Commit Date': create_last_commit_date_query,
        'Power Source Period': create_power_source_period_query,
        'Device Name': create_device_name_query,
        'Hardfault1': create_hardfault1_query,
        'Database Info': create_database_info_query,
        'Ethernet Config': create_ethernet_config_query,
        'Application State': create_application_state_query,
        'Masthead': create_masthead_query,
        'Output Groups': create_output_groups_query,
        'Input Groups': create_input_groups_query,
        'Input Instance Behaviour': create_input_instance_behaviour_query,
        'Output Scenes': create_output_scenes_query,
        'Output Features': create_output_features_query,
        'Output Triac Run Method': create_output_triac_run_methode_query,
        'Onboard Device Name': create_onboard_device_name_query,
        'Output Object Feature': create_output_obj_feature_query,
        'RTC Time and Date': create_rtc_time_date_query,
        'GMT': create_gmt_query,
        'Latitude/Longitude': create_latitude_longitude_query,
        'Sunrise Time': create_sunrise_time_query,
        'Sunset Time': create_sunset_time_query,
        'DALI Discovered Devices': create_dali_discovered_devices_query,
        'DALI Device Masthead': create_dali_device_masthead_query,
        'DALI Gear NVM': create_dali_gear_nvm_query,
        'DALI Gear RAM': create_dali_gear_ram_query,
        'DALI Input NVM': create_dali_input_nvm_query,
        'DALI Device Name': create_dali_device_name_query,
        'DALI Gear Feature': create_dali_gear_feature_query,
        'Occupancy Duration': create_occupancy_duration_query,
        'Room Situation': create_room_situation_query,
        'Door Position': create_door_position_query,
        'DND Summary': create_dnd_summary_query,
        'Modbus Device Masthead': create_modbus_device_masthead_query,
        'Modbus Register Address': create_modbus_register_address_query
    }
