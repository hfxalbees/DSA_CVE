import time
import pandas


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key, row):
    if root is None:
        root = TreeNode(key)
        root.rows = [row]

    else:
        if root.val < key:
            root.right = insert(root.right, key, row)

        elif root.val > key:
            root.left = insert(root.left, key, row)

        else:
            root.rows.append(row)

    return root


def search(root, substring):
    if root is None or substring in root.val:
        return root

    if root.val < substring:
        return search(root.right, substring)

    return search(root.left, substring)


def insert_excel_data_into_bst(root, df):
    for index, row in df.iterrows():
        for cell in row:
            root = insert(root, str(cell), row)

    return root


def search_substring_in_excel_bst(bst_root, substring):
    start = time.perf_counter()
    result_node = search(bst_root, substring)

    if result_node:
        end = time.perf_counter()
        return "Binary Search Tree", (end - start) * 1000

    else:
        return None


excel_file = "C:/Users/wenzh/Downloads/Input_Data.xlsx"
df = pandas.read_excel(excel_file)

bst_root = None
bst_root = insert_excel_data_into_bst(bst_root, df)
search_substring = "2015-0918"
algorithm_type, time_elapsed = search_substring_in_excel_bst(bst_root, search_substring)

print("Algorithm Type:", algorithm_type)
print("Time Elapsed: %0.5f" % time_elapsed, "ms")
