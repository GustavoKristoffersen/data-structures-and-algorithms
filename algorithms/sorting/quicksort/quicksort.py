def partition(array, left_index, right_index):
    pivot_index = right_index
    pivot = array[right_index]
    right_index -= 1

    while True:
        while array[left_index] < pivot:
            left_index += 1
        
        while array[right_index] > pivot:
            right_index -= 1
        
        if left_index >= right_index:
            break
        else:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index += 1
        
    array[left_index], array[pivot_index] = array[pivot_index], array[left_index]
    
    return left_index

def quicksort(array, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(array) - 1
    
    if right_index - left_index <= 0:
        return

    pivot_index = partition(array, left_index, right_index)
    quicksort(array, left_index, pivot_index - 1)
    quicksort(array, pivot_index + 1, right_index)

    return array