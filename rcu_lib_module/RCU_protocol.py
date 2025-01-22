from enum import Enum
import struct
from rcu_lib_module.GeneralFunctions import get_member_from_value

class DALI_Constants:
    pass

class RCU_EventMsgConstants:
    class EventMessageInfos(Enum):
        idle = 0
        single_press = 0x10
        continues = 0x20
        edge_open = 0x30
        edge_short = 0x31
        timed_short = 40
        timed_long = 41

    class EventModbusAckInfos(Enum):
        mb_err_ok = 0
        mb_err_transmit_err = 1
        mb_err_receiver_err = 2
        mb_err_modbus_f3_err = 3
        mb_err_modbus_wrong_dev_add_err = 4
        mb_err_modbus_wrong_data_size_err = 5
        mb_err_modbus_crc_err = 6
        mb_err_receiver_timeout = 7
        mb_err_trasnmitter_timeout = 8
        mb_err_modbus_f16_err = 9

    class EventModbusInfoEventInfos(Enum):
        active = 0
        pended = 1
        comminication_err = 2
        comminication_chaos = 3
        info_received = 4

class RCU_NACK_Infos:
    class Configuration(Enum):
        idle = 255
        wong_data_range = 1
        wrong_address = 2
        inactive_address = 3
        wrong_instance_range = 4
        proccess_not_executed = 5

    class Control(Enum):
        idle = 0
        wong_data_range = 1
        wrong_address = 2
        inactive_address = 3
        wrong_instance_range = 4

    class Bootloader(Enum):
        idle = 255
        WrongDataRange = 1
        WrongAddress = 2
        InactiveAddress = 3
        WrongInstanceRange = 4
        not_executed = 5
        wrong_password = 6
        wrong_resetvec_or_msp = 7
        unfinished_transaction = 8
        wrong_checksum = 9
        wrong_force_jmp_password = 10
        wrong_app_prog_size = 11
        wrong_app_CRC = 12
        mem_not_erased = 13
        checksum_err = 14
        flash_locked = 15
        


class RCU_MessageStructureConstants:
    class CMD_Type_No(Enum):
        Query                   = 0x2
        Events                  = 0x4
    class CMD_No(Enum):
        General                 = 0x0
        Eternet                 = 0x1
        OnboardDevice           = 0x2
        RTC                     = 0x3
        DALI                    = 0x4
        Occupancy               = 0x5
        DND_App                 = 0x6
        Modbus                  = 0x7
    class Sub_CMD_No:
        class Query:
            class General(Enum):
                Q_GTIN                                  = 0x00
                FB_GTIN                                 = 0x01
                Q_Serial_Number                         = 0x2
                FB_Serial_Number                        = 0x3
                Q_Software_Version                      = 0x4
                FB_Software_Version                     = 0x5
                Q_Hardware_Version                      = 0x6
                FB_Hardware_Version                     = 0x7
                Q_SW_Commit_SHA                         = 0x08
                FB_SW_Commit_SHA                        = 0x09
                Q_SW_Author                             = 0x0A
                FB_SW_Author                            = 0x0B
                Q_Last_Commit_Date                      = 0xC
                FB_Last_Commit_Date                     = 0xD
                Q_PowerSourcePeriod                     = 0x0E
                FB_PowerSourcePeriod                    = 0x0F
                Q_DeviceName                            = 0x10
                FB_DeviceName                           = 0x11
                Q_HardFault1                            = 0x12
                FB_HardFault1                           = 0x13
                Q_DatabaseInfo                          = 0x14
                FB_DatabaseInfo                         = 0x15
            class Eternet(Enum):
                Q_EternetConfig                         = 0x00
                FB_EternetConfig                        = 0x01
            class OnboardDevice(Enum):
                Q_ApplicationState                      = 0x00
                FB_ApplicationState                     = 0x01
                Q_Masthead                              = 0x2
                FB_Masthead                             = 0x3
                Q_OutputGroups                          = 0x04
                FB_OutputGroups                         = 0x05
                Q_InputGroups                           = 0x06
                FB_InputGroups                          = 0x07
                Q_InputInstanceBehaviour                = 0x8
                FB_InputInstanceBehaviour               = 0x9
                Q_OutputScenes                          = 0x0A
                FB_OutputScenes                         = 0x0B
                Q_OutputFeatures                        = 0x0C
                FB_OutputFeatures                       = 0x0D
                Q_OutputTriacRunMethode                 = 0x0E
                FB_OutputTriacRunMethode                = 0x0F
                Q_DeviceName                            = 0x10
                FB_DeviceName                           = 0x11
                Q_OutputObjFeature                      = 0x12
                FB_OutputObjFeature                     = 0x13
            class Rtc(Enum):
                Q_RtcTimeAndDate                        = 0x00
                FB_RtcTimeAndDate                       = 0x01
                Q_GMT                                   = 0x02
                FB_GMT                                  = 0x03
                Q_LatitudeAndLongtude                   = 0x04
                FB_LatitudeAndLongtude                  = 0x05
                Q_SunriseTime                           = 0x06
                FB_SunriseTime                          = 0x07
                Q_SunsetTime                            = 0x08
                FB_SunsetTime                           = 0x09
            class DALI(Enum):
                Q_DiscoveredDevNumberAndAddress         = 0x00
                FB_DiscoveredDevNumberAndAddress        = 0x01
                Q_DaliDeviceObjMastHead                 = 0x02
                FB_DaliDeviceObjMastHead                = 0x03
                Q_GearNvmContent                        = 0x04
                FB_GearNvmContent                       = 0x05
                Q_GearRamContent                        = 0x06
                FB_GearRamContent                       = 0x07
                Q_InputNvmContent                       = 0x08
                FB_InputNvmContent                      = 0x09
                Q_DeviceObjName                         = 0x0A
                FB_DeviceObjName                        = 0x0B
                Q_GearObjFeature                        = 0x0C
                FB_GearFeature                          = 0x0D
                # Q_Button13xNvmContent                   = 0x0E
                # FB_Button13xNvmContent                  = 0x0F
                FB_DaliNACK                             = 0xFE
            class Occupancy(Enum):
                Q_Duration                              = 0x00
                FB_Duration                             = 0x01
                Q_occupancy_room_situation              = 0x02
                FB_occupancy_room_situation             = 0x03
                Q_occupancy_door_position               = 0x04
                FB_occupancy_door_position              = 0x05
            class DND_App(Enum):
                Q_dndapp_summary                        = 0x00
                FB_dndapp_summary                       = 0x01
            class Modbus(Enum):
                Q_modbus_device_masthead                = 0x00
                FB_modbus_device_masthead               = 0x01
                Q_modbus_dev_register_address_for_event = 0x02
                FB_modbus_dev_register_address_for_event= 0x03
        class Events:
            class OnboardDevice(Enum):
                InputEvents                             = 0x0
            class DALI(Enum):
                DigidimEvents                           = 0x00
                InitializationProcessFinished           = 0x01
                ScanAndResetProcessFinished             = 0x02
                GenericReturn                           = 0x03
                GenericEvents                           = 0x04
            class Occupancy(Enum):
                Event_occapp_door_opened                = 0x00
                Event_occapp_door_closed                = 0x01
                Event_occapp_door_open_alarm            = 0x02
                Event_occapp_door_open_alarm_deleted    = 0x03
                Event_occapp_room_empty                 = 0x04
                Event_occapp_room_occupied              = 0x05
            class DND_App(Enum):
                Event_dndapp_mur_requested              = 0x00
                Event_dndapp_mur_request_canceled       = 0x01
                Event_dndapp_loundry_requested          = 0x02
                Event_dndapp_loundry_request_canceled   = 0x03
                Event_dndapp_dnd_active                 = 0x04
                Event_dndapp_dnd_passive                = 0x05
                Event_dndapp_mur_started                = 0x06
                Event_dndapp_mur_finished               = 0x07
                Event_dndapp_occ_queried                = 0x08
                Event_dndapp_doorbell_triggered         = 0x09
            class Modbus(Enum):
                ReadRegisterReturn                      = 0x00
                WriteRegisterReturn                     = 0x01
                SpecialRegister                         = 0x02
                Information                             = 0x03
        

valid_sub_commands = [
    RCU_MessageStructureConstants.Sub_CMD_No.Query.General,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App,
    RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus,
   
    RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice,
    RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI,
    RCU_MessageStructureConstants.Sub_CMD_No.Events.Occupancy,
    RCU_MessageStructureConstants.Sub_CMD_No.Events.DND_App,
    RCU_MessageStructureConstants.Sub_CMD_No.Events.Modbus,
]

class RCU_MSG_STRUCTURE_VERSION:
    VERSION1 = 1
    VERSION2 = 2

HEADER = 0x3E

class RCU_MessageStructure:
    def __init__(self, message_structure_version = RCU_MSG_STRUCTURE_VERSION.VERSION2) -> None:
        self.__structure_version = message_structure_version
        self.__header = HEADER
        self.__data_length = 0
        self.__cmd_type_no = 0
        self.__cmd_no = 0
        self.__sub_cmd_no = 0
        self.__data = b''

    @property
    def structure_version(self):
        return self.__structure_version

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, value):
        if 0 <= value <= 255:  # 1 byte değeri için 0-255 aralığında değerler
            self.__header = value
        else:
            raise ValueError("header should be a single byte value (0-255)")
        
    @property
    def data_length(self):
        return self.__data_length

    @data_length.setter
    def data_length(self, value):
        if(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION2):
            if value >= 0 and value <= 1024:
                self.__data_length = value
            else:
                raise ValueError("Data length must be between 0 and 1024")
        elif(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION1):
            if value >= 0 and value <= 255:
                self.__data_length = value
            else:
                raise ValueError("Data length must be between 0 and 255")
        else:
            raise TypeError("Wrong structure version type")

    @property
    def cmd_type_no(self):
        return self.__cmd_type_no

    @cmd_type_no.setter
    def cmd_type_no(self, value):
        if isinstance(value, RCU_MessageStructureConstants.CMD_Type_No):
            self.__cmd_type_no = value
        else:
            raise ValueError("cmd_type_no should be an instance of CMD_Type")
        
    @property
    def cmd_no(self):
        return self.__cmd_no

    @cmd_no.setter
    def cmd_no(self, value):
        if isinstance(value, RCU_MessageStructureConstants.CMD_No):
            self.__cmd_no = value
        else:
            raise ValueError("cmd_no should be an instance of CMD_No")
        
    @property
    def sub_cmd_no(self):
        return self.__sub_cmd_no

    @sub_cmd_no.setter
    def sub_cmd_no(self, value):
        if type(value) in valid_sub_commands:
            self.__sub_cmd_no = value
        else:
            raise ValueError("sub_cmd_no should be an instance of Sub_CMD_No")
        
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION2):
            if isinstance(data, bytes) and len(data) <= (1024 - 3):
                self.data_length = len(data) + 3
                self.__data = data
            else:
                raise ValueError("Data must be a bytes object and cannot be greater than 1024 bytes")
        elif(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION1):
            if isinstance(data, bytes) and len(data) <= (255 - 3):
                self.data_length = len(data) + 3
                self.__data = data
            else:
                raise ValueError("Data must be a bytes object and cannot be greater than 255 bytes")
        else:
            raise TypeError("Wrong structure version type")
        
    def FindCmdTypeNo(self, value):
        return get_member_from_value(value, RCU_MessageStructureConstants.CMD_Type_No)
    
    def FindCmdNo(self, value):
        return get_member_from_value(value, RCU_MessageStructureConstants.CMD_No)
    
    def FindSubCmdNo(self, cmd_type_no, cmd_no, value):
        sub_cmd = None
        if(cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Query):
            if(cmd_no == RCU_MessageStructureConstants.CMD_No.General):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.General)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.Eternet):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.Eternet)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.OnboardDevice)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.RTC):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.Rtc)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.DALI):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.DALI)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.Occupancy):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.Occupancy)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.DND_App):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.DND_App)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.Modbus):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Query.Modbus)

        elif(cmd_type_no == RCU_MessageStructureConstants.CMD_Type_No.Events):
            if(cmd_no == RCU_MessageStructureConstants.CMD_No.OnboardDevice):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Events.OnboardDevice)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.DALI):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Events.DALI)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.Occupancy):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Events.Occupancy)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.DND_App):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Events.DND_App)
            elif(cmd_no == RCU_MessageStructureConstants.CMD_No.Modbus):
                sub_cmd = get_member_from_value(value, RCU_MessageStructureConstants.Sub_CMD_No.Events.Modbus)

        return sub_cmd

    def Wrap(self):
        # buf = [self.header, self.data_length, self.cmd_type_no.value, self.cmd_no.value, self.sub_cmd_no.value, self.data]

        if(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION2):
            buf = struct.pack(f"6B{len(self.data)}s", self.header, (self.data_length & 0xFF), (self.data_length >> 8 & 0xFF), self.cmd_type_no.value, self.cmd_no.value, self.sub_cmd_no.value, self.data)
        elif(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION1):
            buf = struct.pack(f"5B{len(self.data)}s", self.header, self.data_length, self.cmd_type_no.value, self.cmd_no.value, self.sub_cmd_no.value, self.data)
        else:
            raise TypeError("Wrong structure version type")

        return buf
    
    def Parse(self, buff):
        buff_len = len(buff)
        if(buff_len > 0):
            # Take length
            if(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION2):
                length = int.from_bytes(buff[1:3], 'little', signed = False) + 3    # Length off all message
            elif(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION1):
                length = buff[1] + 2                                                # Length off all message
            else:
                raise TypeError("Wrong structure version type")
            
            if(length == buff_len):
                if(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION2):
                    length = length - 3                                             # Length of the message part
                    unpacked_data = struct.unpack(f"6B{length - 3}s", buff)

                    self.header = unpacked_data[0]
                    self.data_length = (unpacked_data[1] | (unpacked_data[2]) << 8) & 0xFFFF 
                    self.cmd_type_no = self.FindCmdTypeNo(unpacked_data[3])
                    self.cmd_no = self.FindCmdNo(unpacked_data[4])
                    self.sub_cmd_no = self.FindSubCmdNo(self.__cmd_type_no, self.__cmd_no, unpacked_data[5])
                    self.data = unpacked_data[6]
                elif(self.structure_version == RCU_MSG_STRUCTURE_VERSION.VERSION1):
                    length = length - 2                                             # Length of the message part
                    unpacked_data = struct.unpack(f"5B{length - 3}s", buff)

                    self.header = unpacked_data[0]
                    self.data_length = unpacked_data[1]
                    self.cmd_type_no = self.FindCmdTypeNo(unpacked_data[2])
                    self.cmd_no = self.FindCmdNo(unpacked_data[3])
                    self.sub_cmd_no = self.FindSubCmdNo(self.__cmd_type_no, self.__cmd_no, unpacked_data[4])
                    self.data = unpacked_data[5]
                else:
                    raise TypeError("Wrong structure version type")
                return True
            else:
                return False
        else:
            return False


