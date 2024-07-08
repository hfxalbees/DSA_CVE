import pandas as pd

# Load the dataset
file_path = '..\\CVE data\\Dataset_Cleaned.xlsx'
df = pd.read_excel(file_path)

# Key function to extract the numeric part of the CVE ID or any other column based on the provided key
def key_func(row, key_column):
    if key_column == 'CVE ID':
        parts = row.split('-')
        return int(parts[0]), int(parts[1])
    else:
        return row

# Define the counting sort function
def counting_sort(arr, exp, key_column, index, descending=True):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(n):
        index_digit = (key_func(arr[i][key_column], key_column)[index] // exp) % 10
        count[index_digit] += 1

    # Change count[i] so that count[i] now contains the actual position of this digit in output
    if descending:
        for i in range(8, -1, -1):
            count[i] += count[i + 1]
    else:
        for i in range(1, 10):
            count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index_digit = (key_func(arr[i][key_column], key_column)[index] // exp) % 10
        output[count[index_digit] - 1] = arr[i]
        count[index_digit] -= 1
        i -= 1

    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]

# Define the radix sort function
def radix_sort(arr, key_column):
    if key_column == 'CVE ID':
        max_val1 = max(arr, key=lambda x: key_func(x[key_column], key_column)[0])
        max_val2 = max(arr, key=lambda x: key_func(x[key_column], key_column)[1])

        # Sort by numeric part first
        exp = 1
        while key_func(max_val2, key_column)[1] // exp > 0:
            counting_sort(arr, exp, key_column, 1, descending=True)
            exp *= 10

        # Sort by year part
        exp = 1
        while key_func(max_val1, key_column)[0] // exp > 0:
            counting_sort(arr, exp, key_column, 0, descending=True)
            exp *= 10
    else:
        # Handle sorting for non-CVE ID columns
        max_val = max(arr, key=lambda x: key_func(x[key_column], key_column))
        exp = 1
        while key_func(max_val, key_column) // exp > 0:
            counting_sort(arr, exp, key_column, 0, descending=True)
            exp *= 10

# Extract the rows from the dataframe
rows = df.to_dict('records')

# Sort the rows based on the specified column in descending order
key_column = 'CVE ID'  # Change this to any other column name as needed
radix_sort(rows, key_column)

# Create a new DataFrame with the sorted data
sorted_df = pd.DataFrame(rows)

# Save the sorted DataFrame to a new Excel file
output_file_path = '..\\Temp\\Sorted_Dataset.xlsx'
sorted_df.to_excel(output_file_path, index=False)

print(f'Sorted dataset has been saved to {output_file_path}')
