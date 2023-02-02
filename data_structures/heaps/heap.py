class Heap:
    def __init__(self):
        self.data = []
        self.length = 0

    def root(self):
        return self.data[0] if self.data else None

    def last(self):
        return self.data[len(self.data) - 1] if self.data else None

    def print_as_list(self):
        print(self.data)

    def _get_left_child_index(self, index):
        return (index * 2) + 1

    def _get_right_child_index(self, index):
        return (index * 2) + 2

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value)
        new_node_index = len(self.data) - 1
        parent_index = self._get_parent_index(new_node_index)
        while new_node_index > 0 and self.data[new_node_index] > self.data[parent_index]:
            self.data[parent_index], self.data[new_node_index] = self.data[new_node_index], self.data[parent_index]
            new_node_index = parent_index
            parent_index = self._get_parent_index(new_node_index)
        self.length += 1
        return self

    def delete(self):
        if not self.data:
            return None
        self.data[0] = self.data.pop()
        trickle_node_index = 0
        while self._has_children_with_greater_value(trickle_node_index):
            greatest_child_index = self._get_greatest_child_index(trickle_node_index)
            self.data[greatest_child_index], self.data[trickle_node_index] = self.data[trickle_node_index], self.data[greatest_child_index]
            trickle_node_index = greatest_child_index
        self.length -= 1
        return self

    def _has_children_with_greater_value(self, index):
        trickle_node = self.data[index]
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        left_child = self.data[left_child_index] if left_child_index < len(self.data) else None
        right_child = self.data[right_child_index] if right_child_index < len(self.data) else None
        return (left_child and left_child > trickle_node) or (right_child and right_child > trickle_node)

    def _get_greatest_child_index(self, index):
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        left_child = self.data[left_child_index]
        right_child = self.data[right_child_index] if right_child_index < len(self.data) else None
        if not right_child:
            return self._get_left_child_index(index)
        if right_child > left_child:
            return self._get_right_child_index(index)
        else:
            return self._get_left_child_index(index)