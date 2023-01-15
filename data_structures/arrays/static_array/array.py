class Array:
  def __init__(self, capacity):
    self.capacity = capacity
    self.last_position = -1
    self.values = [None] * capacity

  # O(n)
  def print(self):
    if self.last_position == -1:
      print('empty...')
    else:
      for i in range(self.last_position + 1):
        print(f'{i} - {self.values[i]}')

  # O(1)
  def add(self, value):
    # no space left
    if self.last_position == self.capacity - 1:
        return
    self.last_position += 1
    self.values[self.last_position] = value

  # O(n)
  def linear_search(self, value):
      for i in range(self.last_position + 1):
        if self.values[i] == value:
          return i
      return -1

  # O(n)
  def delete(self, value):
    p = self.linear_search(value)
    if p == -1:
      return -1
    for i in range(p, self.last_position):
        self.values[i] = self.values[i + 1]
    self.last_position -= 1