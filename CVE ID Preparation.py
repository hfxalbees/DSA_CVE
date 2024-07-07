import pandas

excel_file = pandas.read_excel("C:/Users/wenzh/Downloads/Dataset.xlsx")
excel_file_columns = excel_file.columns
excel_file = excel_file.values.tolist()
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

cleaned_excel_file = pandas.DataFrame(excel_file, columns = excel_file_columns).to_excel("C:/Users/wenzh/Downloads/Dataset_Cleaned.xlsx")
