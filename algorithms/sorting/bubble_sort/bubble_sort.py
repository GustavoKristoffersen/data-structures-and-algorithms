# Using nested for loops
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Using a while loop (more descriptive)
def bubble_sort(arr):
  unsorted_until_index = len(arr) - 1
  sorted = False
  while not sorted:
    sorted = True
    for i in range(unsorted_until_index):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        sorted = False
    unsorted_until_index -= 1
  return arr