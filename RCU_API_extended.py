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