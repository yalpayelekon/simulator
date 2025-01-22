from enum import Enum

class BYTE_ORDER_TYPE(Enum):
    big = 'big'
    little = 'little'

def ConvertToByte(number:int, byte_count:int, byte_order:BYTE_ORDER_TYPE, signed:bool):
    return int(number).to_bytes(byte_count, byteorder=byte_order.value, signed=signed)

def get_member_from_value(value, enum_class):
    for member in enum_class:
        if member.value == value:
            return member
    return None