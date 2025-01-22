# This is api for our rcu device.
from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants, RCU_MSG_STRUCTURE_VERSION
from rcu_lib_module.GeneralFunctions import ConvertToByte, BYTE_ORDER_TYPE
from enum import Enum

class RCU_API:
    # ----------------------------------------- Functions ------------------------------------------
    def PrintCMDMesage(obj:RCU_MessageStructure):
        print("---------------------------------------------------------")
        print("Header: ", obj.header)
        print("Data Length: ", obj.data_length)
        print("CMD TYPE NO: ", obj.cmd_type_no.name)
        print("CMD NO: ", obj.cmd_no.name)
        print("SUB CMD NO: ", obj.sub_cmd_no.name)
        print("Data: ", obj.data)
        print("---------------------------------------------------------")
    # ----------------------------------------- Functions ------------------------------------------
    def PrintReplyMesage(obj:RCU_MessageStructure):
        print("---------------------------------------------------------")
        print("Header: ", obj.header)
        print("Data Length: ", obj.data_length)
        print("CMD TYPE NO: ", obj.cmd_type_no.name)
        print("CMD NO: ", obj.cmd_no.name)
        print("SUB CMD NO: ", obj.sub_cmd_no.name)
        print("DATA: ", obj.data)
        print("---------------------------------------------------------")

    def __CheckStructureVersion(obj:RCU_MessageStructure, target_version:RCU_MSG_STRUCTURE_VERSION):
        if(obj.structure_version != target_version):
            raise TypeError("Wrong structure version type")

    def __SetQUERY(obj:RCU_MessageStructure):
        obj.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Query

    def __SetEVENT(obj:RCU_MessageStructure):
        obj.cmd_type_no = RCU_MessageStructureConstants.CMD_Type_No.Events

    def __SetGeneral(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.General

    def __SetEternet(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.Eternet

    def __SetOnboardDevice(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.OnboardDevice

    def __SetRtc(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.RTC

    def __SetDali(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.DALI

    def __SetOccupancy(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.Occupancy

    def __SetDND_App(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.DND_App

    def __SetModbus(obj:RCU_MessageStructure):
        obj.cmd_no = RCU_MessageStructureConstants.CMD_No.Modbus

# ------------------------------ QUERY ------------------------------------------
# ------------------------------ General -----------------------------------------
    def Q_device_GTIN(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_GTIN
        obj.data = bytes([])

    def Q_device_serial_number(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Serial_Number
        obj.data = bytes([])

    def Q_software_version(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Software_Version
        obj.data = bytes([])

    def Q_hardware_version(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Hardware_Version
        obj.data = bytes([])

    def Q_SW_commit_SHA(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_SW_Commit_SHA
        obj.data = bytes([])

    def Q_SW_author(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_SW_Author
        obj.data = bytes([])

    def Q_Last_commit_date(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_Last_Commit_Date
        obj.data = bytes([])

    def Q_power_source_period(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_PowerSourcePeriod
        obj.data = bytes([])

    def Q_device_name(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_DeviceName
        obj.data = bytes([])

    def Q_hardfault_1_reg(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_HardFault1
        obj.data = bytes([])

    def Q_database_info(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.Q_DatabaseInfo
        obj.data = bytes([])

# ------------------------------ Eternet ------------------------------------------
    def Q_ethernet_config(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetEternet(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet.Q_EternetConfig
        obj.data = bytes([])

# ------------------------------ Onboard Device ------------------------------------------
    def Q_onboard_application_state(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_ApplicationState
        obj.data = bytes([])

    def Q_onboard_devices_masthead(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_Masthead
        obj.data = bytes([])

    def Q_onboard_output_groups(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputGroups
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_input_groups(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_InputGroups
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_input_instance_behaviour(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_InputInstanceBehaviour
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_output_scenes(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputScenes
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_output_features(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputFeatures
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_output_triac_run_methode(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputTriacRunMethode
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_device_name(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_DeviceName
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_onboard_output_obj_features(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.Q_OutputObjFeature
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

# ------------------------------ Rtc ------------------------------------------
    def Q_RTC_time_and_date(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_RtcTimeAndDate
        obj.data = bytes([])

    def Q_GMT(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_GMT
        obj.data = bytes([])

    def Q_latitude_and_longitude(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_LatitudeAndLongtude
        obj.data = bytes([])

    def Q_sunrise_time(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_SunriseTime
        obj.data = bytes([])

    def Q_sunset_time(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.Q_SunsetTime
        obj.data = bytes([])

# ------------------------------ DALI ------------------------------------------
    def Q_dali_device_discovered_sadd(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DiscoveredDevNumberAndAddress
        obj.data = bytes([])

    def Q_dali_device_masthead(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DaliDeviceObjMastHead
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_dali_gear_nvm_content(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearNvmContent
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_dali_gear_ram_content(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearRamContent
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_dali_input_nvm_content(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_InputNvmContent
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_dali_device_obj_name(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_DeviceObjName
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_dali_gear_feature(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.Q_GearObjFeature
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

# ------------------------------ Occupancy ------------------------------------------
    def Q_ocuupancy_duration(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_Duration
        obj.data = bytes([])

    def Q_occupancy_room_situation(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_occupancy_room_situation
        obj.data = bytes([])

    def Q_occupancy_door_position(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.Q_occupancy_door_position
        obj.data = bytes([])

# ------------------------------ DND_App ------------------------------------------
    def Q_dndapp_summary(obj: RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetDND_App(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App.Q_dndapp_summary
        obj.data = bytes([])

# ------------------------------ Modbus ------------------------------------------
    def Q_modbus_device_masthead(obj:RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetModbus(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.Q_modbus_device_masthead
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

    def Q_modbus_device_reg_add(obj:RCU_MessageStructure, data):
        RCU_API.__SetQUERY(obj)
        RCU_API.__SetModbus(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.Q_modbus_dev_register_address_for_event
        i = 0
        data0 = ConvertToByte(data[i], 1, BYTE_ORDER_TYPE.big, False) 
        obj.data = data0

# ------------------------------ EVENTS ------------------------------------------
# ------------------------------ Onboard Devices ------------------------------------------
    def Event_onboard_inputs(obj:RCU_MessageStructure, data):
        RCU_API.__SetEVENT(obj)
        RCU_API.__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice.InputEvents
        obj.data = bytes([])

# ------------------------------ Dali ------------------------------------------
    def Event_dali_digidim_inputs(obj:RCU_MessageStructure, data):
        RCU_API.__SetEVENT(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.DigidimEvents
        obj.data = bytes([])

    def Event_dali_initialization_finished(obj:RCU_MessageStructure, data):
        RCU_API.__SetEVENT(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.InitializationProcessFinished
        obj.data = bytes([])

    def Event_dali_scan_and_reset_finished(obj:RCU_MessageStructure, data):
        RCU_API.__SetEVENT(obj)
        RCU_API.__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI.ScanAndResetProcessFinished
        obj.data = bytes([])