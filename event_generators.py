import random
from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants

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