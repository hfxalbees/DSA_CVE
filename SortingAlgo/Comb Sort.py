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


def next_gap(gap):
    gap = (gap * 10)//13

    if gap < 1:
        return 1

    return gap


def comb_sort(input_data):
    start = time.perf_counter()
    n = len(input_data)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = next_gap(gap)
        swapped = False

        for i in range(0, n-gap):
            if input_data[i] > input_data[i + gap]:
                input_data[i], input_data[i + gap] = input_data[i + gap], input_data[i]
                swapped = True

    end = time.perf_counter()

    return "Comb Sort", (end - start)


algorithm_type, time_elapsed = comb_sort(excel_file)
print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f" % (time_elapsed * 1000), "ms")
