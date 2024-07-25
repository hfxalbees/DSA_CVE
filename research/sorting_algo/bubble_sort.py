import pandas as pd


def bubble_sort(data, column_name):
    n = len(data)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if data[j][column_name] > data[j + 1][column_name]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break


def sort_excel_file(input_file, output_file, column_name):
    df = pd.read_excel(input_file)
    data = df.to_dict(orient='records')
    bubble_sort(data, column_name)
    sorted_df = pd.DataFrame(data)
    sorted_df.to_excel(output_file, index=False)
    print(f"\nSorted data based on '{column_name}' column has been saved to '{output_file}'")



