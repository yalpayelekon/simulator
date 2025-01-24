from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants
from rcu_lib_module.RCU_API import RCU_API

class RCU_API_Extended(RCU_API):
    @staticmethod
    def FB_device_GTIN(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)  
        RCU_API._RCU_API__SetGeneral(obj)  
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_GTIN
        obj.data = data

    @staticmethod
    def FB_device_serial_number(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Serial_Number
        obj.data = data

    @staticmethod
    def FB_software_version(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Software_Version
        obj.data = data

    @staticmethod
    def FB_hardware_version(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Hardware_Version
        obj.data = data

    @staticmethod
    def FB_SW_commit_SHA(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_SW_Commit_SHA
        obj.data = data

    @staticmethod
    def FB_SW_author(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_SW_Author
        obj.data = data

    @staticmethod
    def FB_last_commit_date(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_Last_Commit_Date
        obj.data = data

    @staticmethod
    def FB_power_source_period(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_PowerSourcePeriod
        obj.data = data

    @staticmethod
    def FB_device_name(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_DeviceName
        obj.data = data

    @staticmethod
    def FB_hardfault_1(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_HardFault1
        obj.data = data

    @staticmethod
    def FB_database_info(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetGeneral(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.General.FB_DatabaseInfo
        obj.data = data

    # Ethernet Feedback Methods
    @staticmethod
    def FB_ethernet_config(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetEternet(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet.FB_EternetConfig
        obj.data = data

    # Onboard Device Feedback Methods
    @staticmethod
    def FB_application_state(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_ApplicationState
        obj.data = data

    @staticmethod
    def FB_masthead(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_Masthead
        obj.data = data

    @staticmethod
    def FB_output_groups(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputGroups
        obj.data = data

    @staticmethod
    def FB_input_groups(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_InputGroups
        obj.data = data

    @staticmethod
    def FB_input_instance_behaviour(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_InputInstanceBehaviour
        obj.data = data

    @staticmethod
    def FB_output_scenes(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputScenes
        obj.data = data

    @staticmethod
    def FB_output_features(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputFeatures
        obj.data = data

    @staticmethod
    def FB_output_triac_run_methode(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputTriacRunMethode
        obj.data = data

    @staticmethod
    def FB_onboard_device_name(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_DeviceName
        obj.data = data

    @staticmethod
    def FB_output_obj_feature(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOnboardDevice(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice.FB_OutputObjFeature
        obj.data = data
# ------------------------------ Rtc ------------------------------------------
    @staticmethod
    def FB_RTC_time_and_date(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_GMT
        obj.data = data

    @staticmethod
    def FB_GMT(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_RtcTimeAndDate
        obj.data = data

    @staticmethod
    def FB_latitude_and_longitude(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_RtcTimeAndDate
        obj.data = data

    @staticmethod
    def FB_sunrise_time(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_SunriseTime
        obj.data = data

    @staticmethod
    def FB_sunset_time(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetRtc(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc.FB_SunsetTime
        obj.data = data
# ------------------------------ Dali ------------------------------------------
    @staticmethod
    def FB_dali_device_discovered_sadd(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DiscoveredDevNumberAndAddress
        obj.data = data

    @staticmethod
    def FB_dali_device_masthead(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DaliDeviceObjMastHead
        obj.data = data

    @staticmethod
    def FB_dali_gear_nvm_content(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearNvmContent
        obj.data = data

    @staticmethod
    def FB_dali_gear_ram_content(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearRamContent
        obj.data = data

    @staticmethod
    def FB_dali_input_nvm_content(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_InputNvmContent
        obj.data = data

    @staticmethod
    def FB_dali_device_obj_name(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_DeviceObjName
        obj.data = data

    @staticmethod
    def FB_dali_gear_feature(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDali(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI.FB_GearFeature
        obj.data = data

# ------------------------------ Occupancy ------------------------------------------
    @staticmethod
    def FB_ocuupancy_duration(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_Duration
        obj.data = data

    @staticmethod
    def FB_occupancy_room_situation(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_occupancy_room_situation
        obj.data = data

    @staticmethod
    def FB_occupancy_door_position(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetOccupancy(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy.FB_occupancy_door_position
        obj.data = data

    # ------------------------------ DND_App ------------------------------------------
    @staticmethod
    def FB_dndapp_summary(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetDND_App(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App.FB_dndapp_summary
        obj.data = data
    
    # ------------------------------ Modbus ------------------------------------------
    @staticmethod
    def FB_modbus_device_masthead(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetModbus(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.FB_modbus_device_masthead
        obj.data = data

    @staticmethod
    def FB_modbus_device_reg_add(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)
        RCU_API._RCU_API__SetModbus(obj)
        obj.sub_cmd_no = RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus.FB_modbus_dev_register_address_for_event
        obj.data = data