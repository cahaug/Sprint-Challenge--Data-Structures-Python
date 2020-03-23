from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the storage is not empty, go to the end of the list
        if self.storage.length > 0:
            current_node = self.storage.head
            while current_node:
                # print(current_node.value[0])
                # print(current_node.value[1])
                current_item = current_node.value[0]
                current_count = current_node.value[1] + 1
                current_node.value = (current_item, current_count)
                current_node = current_node.next
        # then check the capacity to see if we can just add or go to end & rewrite last value
        if self.storage.length < self.capacity:
            self.storage.add_to_tail((item, 0))
        if self.storage.length == self.capacity:
            current_node = self.storage.head
            while current_node:
                if current_node.value[1] == self.capacity:
                    current_node.value = (item, 0)
                current_node = current_node.next
        pass


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # go to the head
        current_node = self.storage.head
        # read the contents of the head, append to list and select the next value if it's there
        while current_node:
            list_buffer_contents.append(current_node.value[0])
            current_node = current_node.next
        return list_buffer_contents

# buffer = RingBuffer(3)
# print(buffer.get())
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# print(buffer.get())
# buffer.append('c')
# buffer.append('c')
# print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
