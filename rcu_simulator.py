import queue
from rcu_lib_module.RCU_protocol_ring_buffer import RCU_Msg_RingBuffer
from event_generators import *
from query_handler import QueryHandler

class RCUSimulator:
    def __init__(self):
        self.message_queue = queue.PriorityQueue()
        self.ring_buffer = RCU_Msg_RingBuffer(100)
        self.query_handler = QueryHandler()

    # Event creation methods
    @staticmethod
    def create_event_onboard_inputs():
        return create_event_onboard_inputs()
        
    @staticmethod
    def create_event_dali_digidim_inputs():
        return create_event_dali_digidim_inputs()
        
    @staticmethod
    def create_event_dali_initialization_finished():
        return create_event_dali_initialization_finished()
        
    @staticmethod
    def create_event_dali_scan_reset_finished():
        return create_event_dali_scan_reset_finished()
        
    def handle_query(self, query_msg):
        return self.query_handler.handle_query(query_msg)