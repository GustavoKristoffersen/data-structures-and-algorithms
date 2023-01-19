class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def pop(self):
        if self.is_empty():
            return None
        elif self.length == 1:
            self.bottom = None
        node_to_pop = self.top
        node_below = node_to_pop.next
        self.top = node_below
        self.length -= 1
        return node_to_pop.value

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.bottom = self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length += 1
        return self

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None and self.bottom is None

    def print_as_list(self):
        array = []
        current_node = self.top
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)