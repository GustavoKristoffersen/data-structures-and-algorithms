class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # O(N)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self._get_node_at_index(index)
        return node.value

    # O(N)
    def insert(self, index, value):
        if index < 0:
            return self
        elif index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        new_node = Node(value)
        if self._is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            left_node = self._get_node_at_index(index - 1)
            right_node = left_node.next
            left_node.next = new_node
            new_node.next = right_node
        self.length += 1
        return self

    # O(N)
    def delete(self, index):
        if index < 0 or index >= self.length:
            return self
        if self._is_empty():
            return self
        if index == 0:
            self.head = self.head.next
        else:
            left_node = self._get_node_at_index(index - 1)
            node_to_delete = left_node.next
            left_node.next = node_to_delete.next
            if node_to_delete == self.tail:
                self.tail = left_node
        self.length -= 1
        return self

    # O(N)
    def search(self, value):
        position = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return position
            current_node = current_node.next
            position += 1
        return -1

    # O(1)
    def prepend(self, value):
        node = Node(value)
        if self._is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    # O(1)
    def append(self, value):
        node = Node(value)
        if self._is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self
    
    def reverse(self):
        if self.length == 1 or self._is_empty():
            return self
        current_node = self.head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        return self

    def print_as_list(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)

    def _is_empty(self):
        return self.head is None and self.tail is None

    def _get_node_at_index(self, index):
        position = 0
        current_node = self.head
        while position < index:
            current_node = current_node.next
            position += 1
        return current_node




