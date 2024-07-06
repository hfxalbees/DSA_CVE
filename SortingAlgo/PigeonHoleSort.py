import time
import pandas as pd

# Read the Excel file and convert it to a list of lists
print("Reading excel file...")
excel_file = pd.read_excel("CVE data/FINAL_DATASET.xlsx").values.tolist()

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

# Convert padded CVE IDs to integers for sorting
for i in range(len(excel_file)):
    excel_file[i][0] = int(excel_file[i][0].replace("-", ""))

# Define the Pigeonhole Sort function
def pigeonhole_sort(input_data):
    start = time.time()

    # Find the range of the values
    min_val = min(input_data, key=lambda x: x[0])[0]
    max_val = max(input_data, key=lambda x: x[0])[0]
    range_size = max_val - min_val + 1

    # Create pigeonholes
    holes = [[] for _ in range(range_size)]

    # Populate the pigeonholes with indices
    for entry in input_data:
        index = entry[0] - min_val
        holes[index].append(entry)

    # Flatten the list
    sorted_data = []
    for hole in holes:
        sorted_data.extend(hole)

    end = time.time()
    return sorted_data, "Pigeonhole Sort", (end - start)

# Call the Pigeonhole Sort function and capture the result
print("Sorting started...")
sorted_data, algorithm_type, time_elapsed = pigeonhole_sort(excel_file)

# Convert sorted data back to a DataFrame
sorted_data_df = pd.DataFrame(sorted_data)

# Define the output Excel file path
output_excel_file = "Sorted CVE/PigeonHoleSort.xlsx"

# Save the sorted data to Excel
sorted_data_df.to_excel(output_excel_file, index=False)

# Print the results
print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f ms" % (time_elapsed * 1000))
print(f"Sorted data saved to {output_excel_file}")
