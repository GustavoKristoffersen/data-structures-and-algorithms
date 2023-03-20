def merge(left_arr, right_arr):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1

    return result + left_arr[left_index:] + right_arr[right_index:]


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle_index = len(arr) // 2
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    return merge(
        merge_sort(left_arr),
        merge_sort(right_arr),
    )