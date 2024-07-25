def pigeonhole_sort(arr, key):
    # Convert CVE IDs to an integer by taking the numeric part after the dash
    converted = [int(x[key].split('-')[1]) for x in arr]
    min_val = min(converted)
    max_val = max(converted)
    range_size = max_val - min_val + 1

    holes = [[] for _ in range(range_size)]

    for x in arr:
        index = int(x[key].split('-')[1]) - min_val
        holes[index].append(x)

    sorted_arr = []
    for hole in holes:
        sorted_arr.extend(hole)

    return sorted_arr
