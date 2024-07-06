import pandas as pd
import time

# Read the Excel file and convert it to a list of lists
print("Reading excel file...")
excel_file = pd.read_excel("CVE data/FINAL_DATASET.xlsx").values.tolist()
print("Excel file read successfully.")

# Initialize an empty list to store the lengths of the CVE IDs
cve_id_length = []

# Calculate the length of each CVE ID and store it in cve_id_length
print("Calculating lengths of CVE IDs...")
for entry in excel_file:
    cve_id_length.append(len(entry[0]))

# Determine the maximum length of the CVE IDs
maximum_cve_id_length = max(cve_id_length)
print(f"Maximum CVE ID length is {maximum_cve_id_length}.")

# Pad the CVE IDs with zeros to make them all the same length
print("Padding CVE IDs with zeros...")
for i in range(len(excel_file)):
    while len(excel_file[i][0]) < maximum_cve_id_length:
        cve_id_string = list(excel_file[i][0])
        cve_id_string.insert(5, "0")
        cve_id_string = "".join(cve_id_string)
        excel_file[i][0] = cve_id_string
print("Padding completed.")

# Convert padded CVE IDs to integers for sorting
print("Converting padded CVE IDs to integers...")
for i in range(len(excel_file)):
    excel_file[i][0] = int(excel_file[i][0].replace("-", ""))
print("Conversion completed.")

# Define the Selection Sort function
def selection_sort(input_data):
    start = time.time()
    print("Selection sort started...")

    size_of_array = len(input_data)
    print(f"Number of elements to sort: {size_of_array}")

    for i in range(size_of_array):
        min_position = i
        for j in range(i + 1, size_of_array):
            if input_data[j][0] < input_data[min_position][0]:
                min_position = j
        # swap in the list
        input_data[i], input_data[min_position] = input_data[min_position], input_data[i]
        if i % 100 == 0:
            print(f"Progress: {i}/{size_of_array} elements sorted...")

    end = time.time()
    print("Selection sort completed.")
    return input_data, "Selection Sort", (end - start)

# Call the Selection Sort function and capture the result
print("Sorting started...")
sorted_data, algorithm_type, time_elapsed = selection_sort(excel_file)
print("Sorting completed.")

# Convert sorted data back to a DataFrame
print("Converting sorted data back to DataFrame...")
sorted_data_df = pd.DataFrame(sorted_data)
print("Conversion completed.")

# Define the output Excel file path
output_excel_file = "Sorted CVE/SelectionSort.xlsx"

# Save the sorted data to Excel
print("Saving sorted data to Excel file...")
sorted_data_df.to_excel(output_excel_file, index=False)
print(f"Sorted data saved to {output_excel_file}")

# Print the results
print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f ms" % (time_elapsed * 1000))
