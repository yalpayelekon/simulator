from rcu_lib_module.RCU_API import RCU_API

from enum import Enum
from typing import List, Type

class DataType(Enum):
    t_idle = 0
    t_no_data = 1
    t_int = 2
    t_bytes = 3


class RCU_CmdItem:
    def __init__(self, id:int, cmd_name:str, data_type:List[Type[DataType]], cmd_fuction) -> None:
        self._id = id
        self._cmd_name = cmd_name
        self._data_types = data_type
        self._cmd_function = cmd_fuction


def CreateCmdList():
    cmd_list:list[RCU_CmdItem] = []
    i = 0
    # ------------------------------ QUERY ------------------------------------------
    # ------------------------------ General ------------------------------------------
    cmd_list.append(RCU_CmdItem(i, "Q_device_GTIN", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_device_GTIN))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_device_serial_number", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_device_serial_number))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_software_version", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_software_version))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_hardware_version", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_hardware_version))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_SW_commit_SHA", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_SW_commit_SHA))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_SW_author", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_SW_author))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_Last_commit_date", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_Last_commit_date))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_power_source_period", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_power_source_period))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_device_name", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_device_name))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_hardfault_1_reg", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_hardfault_1_reg))

    # ------------------------------ Eternet ------------------------------------------
    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_ethernet_config", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_ethernet_config))


    # ------------------------------ Onboard Device ------------------------------------------
    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_application_state", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_application_state))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_devices_masthead", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_devices_masthead))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_output_groups", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_output_groups))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_input_groups", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_input_groups))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_input_instance_behaviour", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_input_instance_behaviour))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_output_scenes", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_output_scenes))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_output_features", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_output_features))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_output_triac_run_methode", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_output_triac_run_methode))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_device_name", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_device_name))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_onboard_output_obj_features", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_onboard_output_obj_features))

    # ------------------------------ Rtc ------------------------------------------
    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_RTC_time_and_date", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_RTC_time_and_date))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_GMT", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_GMT))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_latitude_and_longitude", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_latitude_and_longitude))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_sunrise_time", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_sunrise_time))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_sunset_time", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_sunset_time))

    # ------------------------------ Dali ------------------------------------------
    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dali_device_discovered_sadd", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_device_discovered_sadd))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dali_device_masthead", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_device_masthead))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dali_gear_nvm_content", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_gear_nvm_content))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dali_gear_ram_content", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_gear_ram_content))

    i+=1
    # cmd_list.append(RCU_CmdItem(i, "Q_dali_input_tiny_nvm_content", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_input_tiny_nvm_content))

    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dali_gear_feature", [DataType.t_int, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dali_gear_feature))

    # ------------------------------ Dali ------------------------------------------
    i+=1
    cmd_list.append(RCU_CmdItem(i, "Q_dndapp_summary", [DataType.t_no_data, DataType.t_no_data, DataType.t_no_data], RCU_API.Q_dndapp_summary))
    
    return cmd_list
