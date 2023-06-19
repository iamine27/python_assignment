import time


def use_list(n):
    return sum([i for i in range(n)])


def use_generator(n):
    return sum((i for i in range(n)))


# generators are more memory efficient than lists when dealing with large sequences of
# data because they generate values dynamically on-the-fly, rather than storing
# them all in memory at once.

# Start the timer
start_time = time.time()

N = 10 ** 8

# Code block to measure execution time
# Replace this with your actual code
use_generator(N)  # 8.63 secs

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
execution_time = end_time - start_time

# Print the execution time
print(f"Execution time using list: {execution_time} seconds")


# Start the timer
start_time = time.time()

use_list(N)

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
execution_time = end_time - start_time

# Print the execution time
print(f"Execution time using generator: {execution_time} seconds")
