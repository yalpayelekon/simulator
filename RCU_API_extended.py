from rcu_lib_module.RCU_protocol import RCU_MessageStructure, RCU_MessageStructureConstants
from rcu_lib_module.RCU_API import RCU_API

class RCU_API_Extended(RCU_API):
    @staticmethod
    def FB_device_GTIN(obj: RCU_MessageStructure, data: bytes):
        RCU_API._RCU_API__SetQUERY(obj)  # Access private method
        RCU_API._RCU_API__SetGeneral(obj)  # Access private method
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