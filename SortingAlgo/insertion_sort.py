import time
import pandas as pd

# Read the Excel file and convert it to a list of lists
excel_file = pd.read_excel("D:/SIT University/Y1T3/Data Structure and Algorithm/Project/FINAL_DATASET.xlsx").values.tolist()

# Initialize an empty list to store the lengths of the CVE IDs
cve_id_length = []

# Calculate the length of each CVE ID and store it in cve_id_length
for entry in excel_file:
    cve_id_length.append(len(entry[0]))

# Determine the maximum length of the CVE IDs
maximum_cve_id_length = max(cve_id_length)

# Pad the CVE IDs with zeros to make them all the same length
for i in range(len(excel_file)):
    while len(excel_file[i][0]) < maximum_cve_id_length:
        cve_id_string = list(excel_file[i][0])
        cve_id_string.insert(5, "0")
        cve_id_string = "".join(cve_id_string)
        excel_file[i][0] = cve_id_string

# Define the Insertion Sort function
def insertion_sort(input_data):
    start = time.time()
    for i in range(1, len(input_data)):
        key = input_data[i]
        j = i - 1
        while j >= 0 and input_data[j][0] > key[0]:
            input_data[j + 1] = input_data[j]
            j -= 1
        input_data[j + 1] = key
    end = time.time()
    return "Insertion Sort", (end - start)

# Call the Insertion Sort function and capture the result
algorithm_type, time_elapsed = insertion_sort(excel_file)

# Convert sorted data back to a DataFrame
sorted_data_df = pd.DataFrame(excel_file)

# Define the output Excel file path
output_excel_file = "D:/SIT University/Y1T3/Data Structure and Algorithm/Project/insertion_sorted_cve_list.xlsx"

# Save the sorted data to Excel
sorted_data_df.to_excel(output_excel_file, index=False)

# Print the results
print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f ms" % (time_elapsed * 1000))
print(f"Sorted data saved to {output_excel_file}")
