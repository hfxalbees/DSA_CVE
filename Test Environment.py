# Import the necessary libraries.
import time
import pandas

# Specify the respective Pandas' function and the file path of the target file.
file = pandas.read_excel("C:/Users/wenzh/Downloads/Excel Files/Test.xlsx")

# Store the data into a list.
file_list = file.values.tolist()


# Create a function for the respective sorting algorithm.

def selection_sort(input_list):
    # Store the current time value.
    starting_time = time.perf_counter()

    # Select the element at index 0.
    for i in range(len(input_list)):
        # Select the element at the subsequent index.
        for j in range(i + 1, len(input_list)):
            # Compare the 2 elements and swap if necessary.
            if input_list[j] < input_list[i]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    # After sorting, store the current time value.
    ending_time = time.perf_counter()

    # Return the various values.
    return starting_time, ending_time, input_list


# Store the various values into their respective variables.
start_time, end_time, sorted_array = selection_sort(file_list)

# Output the original array.
print("Unsorted Data:", file_list)

# Output the resulting array.
print("Sorted Data:", sorted_array)

# Output the resulting time elapsed in microsecond.
print("Time Elapsed: %0.12f" % ((end_time - start_time) * (10**6)))
