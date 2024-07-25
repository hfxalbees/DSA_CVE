import pandas as pd

def preprocess_cve_id(cve_id):
    """Remove non-numeric characters from CVE ID and convert to integer."""
    numeric_part = ''.join(filter(str.isdigit, cve_id))
    return int(numeric_part)

def radix_sort(data, column_name):
    # Preprocess the data to convert CVE IDs to integers
    for item in data:
        item['temp'] = preprocess_cve_id(item[column_name])

    # Find the maximum value in the preprocessed integer data
    max_val = max(item['temp'] for item in data)

    exp = 1
    while max_val // exp > 0:
        data = counting_sort(data, 'temp', exp)
        exp *= 10

    # Remove the temporary preprocessed key
    for item in data:
        del item['temp']

    return data

def counting_sort(data, key, exp):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (data[i][key] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (data[i][key] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1
        i -= 1

    for i in range(len(data)):
        data[i] = output[i]

    return data
