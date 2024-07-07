def pigeonhole_sort(arr, key):
    converted = [key(x) for x in arr]
    min_val = min(converted)
    max_val = max(converted)
    range_size = max_val - min_val + 1

    holes = [[] for _ in range(range_size)]

    for x in arr:
        index = key(x) - min_val
        holes[index].append(x)

    arr = []
    for hole in holes:
        hole.sort(key=key)  # Sort each hole
        arr.extend(hole)
    
    return arr
