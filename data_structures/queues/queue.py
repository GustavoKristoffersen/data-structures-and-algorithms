class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def _is_empty(self):
        return self.first is None and self.last is None
    
    # O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self._is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    # O(1)
    def dequeue(self):
        if self._is_empty():
            return None
        elif self.length == 1:
            self.last = None
        node_to_pop = self.first
        self.first = node_to_pop.next
        self.length -= 1
        return node_to_pop.value

    # O(1)
    def peek(self):
        return self.first.value if self.first is not None else None

    def print_as_list(self):
        data = []
        current_node = self.first
        while current_node is not None:
            data.append(current_node.value)
            current_node = current_node.next
        print(data)

    

    