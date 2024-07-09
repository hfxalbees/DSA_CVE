import pandas as pd

def preprocess_cve_id(cve_id):
    """Remove dashes from CVE ID and convert to integer for sorting."""
    return int(cve_id.replace('-', ''))

def postprocess_cve_id(cve_id_int):
    """Convert integer back to CVE ID format with dashes."""
    cve_str = str(cve_id_int)
    return f"{cve_str[:4]}-{cve_str[4:10]}-{cve_str[10:]}"

def insertion_sort(bucket, column_name):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j][column_name] > up[column_name]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(data, column_name):
    max_val = max(data, key=lambda x: x[column_name])[column_name]
    size = max_val // len(data)

    buckets = [[] for _ in range(len(data))]

    for i in range(len(data)):
        j = data[i][column_name] // size
        if j != len(data):
            buckets[j].append(data[i])
        else:
            buckets[len(data) - 1].append(data[i])

    for i in range(len(data)):
        buckets[i] = insertion_sort(buckets[i], column_name)

    result = []
    for i in range(len(data)):
        result.extend(buckets[i])

    return result

def sort_excel_file(input_file, output_file, column_name):
    try:
        df = pd.read_excel(input_file)
    except FileNotFoundError:
        print(f"\nError: The file '{input_file}' does not exist.")
        return
    except Exception as e:
        print(f"\nError: {e}")
        return

    if column_name not in df.columns:
        print(f"\nError: The column '{column_name}' does not exist in the dataset.")
        return

    # Check column type
    if df[column_name].dtype == 'object':
        # Preprocess CVE IDs
        try:
            df['temp_sort_column'] = df[column_name].apply(preprocess_cve_id)
        except Exception as e:
            print(f"\nError while preprocessing '{column_name}': {e}")
            return

        data = df.to_dict(orient='records')
        sorted_data = bucket_sort(data, 'temp_sort_column')

        # Convert back to original format
        sorted_df = pd.DataFrame(sorted_data)
        sorted_df[column_name] = sorted_df['temp_sort_column'].apply(postprocess_cve_id)
        sorted_df = sorted_df.drop(columns=['temp_sort_column'])

    else:
        # For numeric columns
        sorted_df = df.sort_values(by=[column_name])

    # Print sorted data
    print(f"Sorted data based on '{column_name}':")
    print(sorted_df)

    try:
        sorted_df.to_excel(output_file, index=False)
        print(f"Sorted data based on '{column_name}' column has been saved to '{output_file}'")
    except Exception as e:
        print(f"\nError: {e}")

input_file = '..\\CVE data\\Dataset_Cleaned.xlsx'
output_file = '..\\Temp\\cve.xlsx'
column_name = input("Input a column name to sort by: ")

sort_excel_file(input_file, output_file, column_name)
