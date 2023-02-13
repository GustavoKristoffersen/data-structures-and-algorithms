class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
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
            self.head = self.tail = new_node
        else:
            left_node = self._get_node_at_index(index - 1)
            right_node = left_node.next
            left_node.next = new_node
            new_node.next = right_node
            new_node.previous = left_node
            right_node.previous = new_node
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
            self.head.previous = None
            self.head.next.previous = self.head.next
        else:
            left_node = self._get_node_at_index(index - 1)
            node_to_delete = left_node.next
            right_node = node_to_delete.next
            left_node.next = right_node
            right_node.previous = left_node
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

    def prepend(self, value):
        node = Node(value)
        if self._is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def append(self, value):
        node = Node(value)
        if self._is_empty():
            self.head = node
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1
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
        distance_from_head = index - 1
        distance_from_tail = self.length - index
        if distance_from_head < distance_from_tail:
            position = 0
            current_node = self.head
            while position < index:
                current_node = current_node.next
                position += 1
            return current_node
        else:
            position = self.length - 1
            current_node = self.tail
            while position > index:
                current_node = current_node.previous
                position -= 1
            return current_node