# Linear search on a unordered array
def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

# Linear search on an ordered array
def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
        if arr[i] > value:
            break
    return -1
