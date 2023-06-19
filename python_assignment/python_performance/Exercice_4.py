import timeit

# Dict hashable, list is not
# dict O(1), list O(n)

# Create a large list
large_list = list(range(1000000))

# Create a dictionary from the list
dict = {num: True for num in large_list}

# Perform lookups using a list
def lookup_list():
    return 500000 in large_list


# Perform lookups using a dict
def lookup_dict():
    return 500000 in dict


# Execution time for list lookup
time_list = timeit.timeit(lambda: lookup_list(), number=1000)

# Execution time for dict lookup
time_dict = timeit.timeit(lambda: lookup_dict(), number=1000)

# Print the execution times
print(f"Lookup time using list: {time_list} seconds")
print(f"Lookup time using dict: {time_dict} seconds")
