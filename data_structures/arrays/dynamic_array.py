from algorithms.searching.linear_search.linear_search import linear_search


class Array:
    def __init__(self):
        self.data = []
        self.length = 0

    # O(N)
    def push(self, value):
        self.data.append(value)
        self.length += 1
        return self

    # O(N)
    def pop(self):
        if not self.length > 0:
            return None
        item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item

    # O(1)
    def get(self, index):
        return self.data[index] if index < self.length else None

    def _perform_shiftings_to_right(self, index):
        self.data.append(None)
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

   # O(N)
    def insert(self, index, value):
        if index > self.length:
            raise IndexError('index out of bond')
        self._perform_shiftings_to_right(index)
        self.data[index] = value
        self.length += 1
        return self

    def _perform_shiftings_to_left(self, index):
        for i in range(index, self.length - 1, 1):
            self.data[i] = self.data[i + 1]

    # O(N)
    def delete(self, index):
        if index > self.length - 1:
            raise IndexError('index out of bond')
        self._perform_shiftings_to_left(index)
        del self.data[self.length - 1]
        self.length -= 1
        return self

    # O(N)
    def linear_search(self, value):
        return linear_search(self.data, value)


    