import time
import pandas


def sentinel_linear_search(df, substring):
    start = time.perf_counter()
    df['_sentinel'] = pandas.Series([False] * len(df), dtype=bool)

    for index, row in df.iterrows():
        row_str = ' '.join(map(str, row))
        row_str += ' SENTINEL'

        if substring in row_str:
            del df['_sentinel']
            end = time.perf_counter()
            return "Sentinel Linear Search", (end - start) * 1000

    del df['_sentinel']
    return None


excel_file = "C:/Users/wenzh/Downloads/Input_Data.xlsx"
df = pandas.read_excel(excel_file)
search_substring = "2015-99"

try:
    algorithm_type, time_elapsed = sentinel_linear_search(df, search_substring)
    print("Algorithm Type:", algorithm_type)
    print("Time Elapsed: %0.5f" % time_elapsed, "ms")

except TypeError:
    print("No matching search string.")
