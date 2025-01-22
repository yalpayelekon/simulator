from rcu_lib_module.RCU_protocol import RCU_MessageStructure
import copy


class RCU_Msg_RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer:list[RCU_MessageStructure] = [RCU_MessageStructure] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push(self, item):
        if self.is_full():
            # Tampon dolu ise en eski elemanı eziyoruz
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1

        self.buffer[self.head] = copy.deepcopy(item)
        self.head = (self.head + 1) % self.capacity

    def pop(self):
        if self.is_empty():
            return None

        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

    def get_all(self):
        if self.is_empty():
            return []
        
        if self.head > self.tail:
            result_list = self.buffer[self.tail:self.head]
        else:
            result_list = self.buffer[self.tail:] + self.buffer[:self.head]
            
        self.tail = self.head
        self.size = 0

        return result_list


# # Kullanım örneği
# ring_buffer = RingBuffer(5)

# ring_buffer.push(1)
# ring_buffer.push(2)
# ring_buffer.push(3)
# ring_buffer.push(4)
# ring_buffer.push(5)

# print("Tampon Durumu:", ring_buffer.get_all())

# ring_buffer.push(6)
# ring_buffer.push(7)

# print("Tampon Durumu:", ring_buffer.get_all())

# popped_item = ring_buffer.pop()
# print("Çıkarılan Eleman:", popped_item)
# print("Tampon Durumu:", ring_buffer.get_all())
