
def stable_quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][key]
        less = [x for x in arr if x[key] < pivot]
        equal = [x for x in arr if x[key] == pivot]
        greater = [x for x in arr if x[key] > pivot]
        return stable_quick_sort(less, key) + equal + stable_quick_sort(greater, key)

