def selection_sort(arr, key):
    size_of_array = len(arr)
    for i in range(size_of_array):
        min_position = i
        for j in range(i + 1, size_of_array):
            if key(arr[j]) < key(arr[min_position]):
                min_position = j
        # Swap in the list
        arr[i], arr[min_position] = arr[min_position], arr[i]
    
    return arr
