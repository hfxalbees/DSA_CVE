def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current_value[key]:  # Change to ascending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr
