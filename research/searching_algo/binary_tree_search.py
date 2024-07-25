# binary_tree_search.py
import pandas as pd

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.rows = []

def insert(root, key, row):
    """ Insert a node into the BST iteratively. """
    new_node = TreeNode(key)
    new_node.rows.append(row)
    
    if root is None:
        return new_node

    current = root
    parent = None

    while current:
        parent = current
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            current.rows.append(row)
            return root

    if key < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    return root

def search(root, key):
    """ Search for a key in the BST iteratively. """
    current = root
    while current:
        if key < current.val:
            current = current.left
        elif key > current.val:
            current = current.right
        else:
            return current.rows  # Return all rows that match the key
    return None

def build_bst_from_df(df, column):
    """ Build a BST from a DataFrame based on the specified column. """
    root = None
    for index, row in df.iterrows():
        root = insert(root, row[column], row.to_dict())
    return root

def binary_tree_search(data, key, search_key):
    """ Search for the search_key in the BST built from the data DataFrame. """
    bst_root = build_bst_from_df(data, key)
    return search(bst_root, search_key)
