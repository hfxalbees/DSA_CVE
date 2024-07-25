

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


