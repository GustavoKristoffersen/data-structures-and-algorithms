def selection_sotr(arr):
    for i in range(len(arr)):
        lowest_at_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[lowest_at_index]:
                lowest_at_index = j
        if lowest_at_index != i:
            arr[i], arr[lowest_at_index] = arr[lowest_at_index], arr[i]
    
    return arr
        