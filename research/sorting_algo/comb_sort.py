import pandas as pd


def comb_sort(data, column_name):
    n = len(data)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)

        if gap < 1:
            gap = 1

        swapped = False

        for i in range(n - gap):
            if data[i][column_name] > data[i + gap][column_name]:
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True


def sort_excel_file(input_file, output_file, column_name):
    df = pd.read_excel(input_file)
    data = df.to_dict(orient='records')
    comb_sort(data, column_name)
    sorted_df = pd.DataFrame(data)
    sorted_df.to_excel(output_file, index=False)
    print(f"Sorted data based on '{column_name}' column has been saved to '{output_file}'")


