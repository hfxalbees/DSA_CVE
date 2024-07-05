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

print(excel_file)
