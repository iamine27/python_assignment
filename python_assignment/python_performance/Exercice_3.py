import timeit

# Create a large list of elements
large_list = list(range(10000000))

# Using list comprehension
def list_comprehension():
    return [x * 2 for x in large_list]


# Using for loop
def for_loop():
    new_list = []
    for x in large_list:
        new_list.append(x * 2)
    return new_list


# Measure the execution time with list comprehension
time_list_comprehension = timeit.timeit(lambda: list_comprehension(), number=10)

# Measure the execution time with for loop
time_for_loop = timeit.timeit(lambda: for_loop(), number=10)

# Print the execution times
print(f"Execution time with list comprehension: {time_list_comprehension} seconds")
print(f"Execution time with for loop: {time_for_loop} seconds")
