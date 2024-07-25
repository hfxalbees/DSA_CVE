import pandas as pd

def fibonacci_search(data, key, search_key):
    """Performs a Fibonacci search on the provided data looking for the specified search key."""
    if key not in data.columns:
        raise ValueError(f"Key '{key}' not found in DataFrame.")
    
    # Convert to list of dictionaries only if needed (consider optimizing this part)
    arr = data.sort_values(by=key).to_dict(orient='records')
    x = search_key
    n = len(arr)

    # Initialize fibonacci numbers
    fibM = 1
    fib1 = 1  # (m-1)'th Fibonacci number
    fib2 = 0  # (m-2)'th Fibonacci number

    # fibM is going to store the smallest Fibonacci number >= n
    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib1 + fib2

    # Marks the eliminated range from front
    offset = -1

    while fibM > 1:
        i = min(offset + fib2, n - 1)

        if arr[i][key] < x:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i][key] > x:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return arr[i]  # Element found

    # Checking the last element
    if fib1 and offset < (n - 1) and arr[offset + 1][key] == x:
        return arr[offset + 1]

    return None  # Element not found
