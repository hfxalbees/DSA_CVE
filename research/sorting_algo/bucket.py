import pandas as pd

def preprocess_cve_id(cve_id):
    """Extracts digits and converts to integer for sorting."""
    numeric_part = ''.join(filter(str.isdigit, cve_id))
    return int(numeric_part)

def bucket_sort(data, column_name):
    # Convert CVE IDs to integers for sorting
    for item in data:
        item['temp'] = preprocess_cve_id(item[column_name])

    # Determine max value based on preprocessed integer data
    max_val = max(item['temp'] for item in data)
    size = max_val // len(data) if len(data) > 0 else 1

    # Create buckets
    buckets = [[] for _ in range(len(data))]

    # Distribute data into buckets
    for item in data:
        index = item['temp'] // size
        if index != len(data):
            buckets[min(index, len(buckets) - 1)].append(item)
        else:
            buckets[-1].append(item)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort(key=lambda x: x['temp'])

    # Compile sorted data into a single list
    sorted_arr = []
    for bucket in buckets:
        for item in bucket:
            del item['temp']  # Clean up the temporary key
            sorted_arr.append(item)

    return sorted_arr
