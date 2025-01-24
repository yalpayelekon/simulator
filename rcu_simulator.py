import queue
from rcu_lib_module.RCU_protocol_ring_buffer import RCU_Msg_RingBuffer
from event_generators import *
from query_handler import handle_query as query_handler

class RCUSimulator:
    def __init__(self):
        self.message_queue = queue.PriorityQueue()
        self.ring_buffer = RCU_Msg_RingBuffer(100)
        
    def create_event_onboard_inputs(self):
        return create_event_onboard_inputs()
        
    def create_event_dali_digidim_inputs(self):
        return create_event_dali_digidim_inputs()
        
    def create_event_dali_initialization_finished(self):
        return create_event_dali_initialization_finished()
        
    def create_event_dali_scan_reset_finished(self):
        return create_event_dali_scan_reset_finished()
        
    def handle_query(self, query_msg):
        return query_handler(query_msg)