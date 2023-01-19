class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def push(self, value):
        return self.data.append(value)

    def peek(self):
        return self.data[len(self.data) - 1] if self.data else None

    def is_empty(self):
        return len(self.data) == 0

    def print_as_list(self):
        print(self.data)