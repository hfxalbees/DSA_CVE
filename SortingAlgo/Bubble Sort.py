import time
import pandas

excel_file = pandas.read_excel("C:/Users/wenzh/Downloads/Input_Data.xlsx").values.tolist()
cve_id_length = []

for entry in excel_file:
    cve_id_length.append(len(entry[0]))

maximum_cve_id_length = max(cve_id_length)

for i in range(len(excel_file)):
    while len(excel_file[i][0]) < maximum_cve_id_length:
        cve_id_string = list(excel_file[i][0])
        cve_id_string.insert(5, "0")
        cve_id_string = "".join(cve_id_string)
        excel_file[i][0] = cve_id_string


def bubble_sort(input_data):
    start = time.time()
    input_data_length = len(input_data)

    for i in range(input_data_length):
        for j in range(0, input_data_length - i - 1):
            if input_data[j] > input_data[j + 1]:
                input_data[j], input_data[j + 1] = input_data[j + 1], input_data[j]

    end = time.time()

    return "Bubble Sort", (end - start)


algorithm_type, time_elapsed = bubble_sort(excel_file)
print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f" % (time_elapsed * 1000), "ms")
