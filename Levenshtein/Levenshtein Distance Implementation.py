import numpy as np
import pandas as pd

def levenshtein(token1, token2):
    # Implementing the Levenshtein distance algorithm
    distance = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distance[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distance[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distance[t1][t2] = distance[t1 - 1][t2 - 1]
            else:
                insert_cost = distance[t1][t2 - 1]
                delete_cost = distance[t1 - 1][t2]
                replace_cost = distance[t1 - 1][t2 - 1]

                distance[t1][t2] = min(insert_cost, delete_cost, replace_cost) + 1

    return distance[len(token1)][len(token2)]

try:
    # Ask user for Excel file path
    excel_path = "C:/Users/wenzh/Downloads/Dataset.xlsx"

    # Read Excel file
    df = pd.read_excel(excel_path, engine='openpyxl')

    # Ask user for column name to search
    column_name = input("Enter the name of the column to search: ").strip()

    # Check if column exists
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the Excel file.")
    else:
        # Get all values from the specified column
        column_values = df[column_name].astype(str).tolist()

        # Ask user for input string
        user_input = input("\nEnter a search string: ").strip()

        closely_matched_word_set = set()  # Use a set to store unique closely matched words
        exact_match_found = False

        # Iterate over each value in the specified column
        for data in column_values:
            distance = levenshtein(user_input, str(data))

            if distance == 0:
                exact_match_found = True
                break
            elif distance < 2:
                closely_matched_word_set.add(data)

        # Convert set back to list for printing purposes (if needed)
        closely_matched_word_list = list(closely_matched_word_set)

        # Print results based on the findings
        if exact_match_found:
            print(f"\nExact match found for: {user_input}")
        else:
            if closely_matched_word_list:
                print("\nIt looks like there is a typo in your input.")
                print("Did you mean any of the following?")
                print(closely_matched_word_list)
            else:
                print("\nNo similar words found within the column.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Error: {e}")
