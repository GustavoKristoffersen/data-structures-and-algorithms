from algorithms.searching.linear_search.linear_search import linear_search


class StaticArray:
  # On static arrays, the size of it is declared at the time
  # the arrays is created and can not be changed afterwards
  def __init__(self, capacity):
    self.capacity = capacity
    self.last_position = -1
    self.values = [None] * capacity

  # O(1)
  def add(self, value):
    # no space left
    if self.last_position == self.capacity - 1:
        return
    self.last_position += 1
    self.values[self.last_position] = value

  # O(n)
  def delete(self, value):
    p = self.linear_search(value)
    if p == -1:
      return -1
    for i in range(p, self.last_position):
        self.values[i] = self.values[i + 1]
    self.last_position -= 1

  # O(n)
  def linear_search(self, value):
    return linear_search(self.values, value)