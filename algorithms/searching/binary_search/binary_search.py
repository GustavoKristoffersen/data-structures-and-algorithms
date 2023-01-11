def binary_search(arr, value):
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = arr[middle_index]
        if middle_value == value:
            return middle_index
        elif middle_value > value:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return -1
