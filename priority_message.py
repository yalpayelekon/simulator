import time
from rcu_lib_module.RCU_protocol import RCU_MessageStructure

PRIORITY_QUERY = 1
PRIORITY_EVENT = 2

class PriorityMessage:
    def __init__(self, priority, message: RCU_MessageStructure, client_socket=None):
        self.priority = priority
        self.message = message
        self.client_socket = client_socket
        self.timestamp = time.time()

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp