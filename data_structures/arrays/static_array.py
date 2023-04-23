from algorithms.searching.linear_search.linear_search import linear_search


class StaticArray:
  # On static arrays, the size of it is declared at the time
  # the arrays is created and can not be changed afterwards
  def __init__(self, length):
    self.length = length
    self.last_position = -1
    self.values = [None] * length

  # O(1)
  def insert(self, index, value):
      if index >= self.length:
          raise IndexError('index out of bond')
      self.values[index] = value
      return self

  # O(1)
  def delete(self, index):
      if index >= self.length:
          raise IndexError('index out of bond')
      self.values[index] = None
      return self

  # O(n)
  def linear_search(self, value):
    return linear_search(self.values, value)