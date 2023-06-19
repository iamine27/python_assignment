import time

# Create a list of strings
strings = ["string" + str(i) for i in range(10000000)]

# Concatenate the strings using list and join
def concatenate_strings_mutable(strings_input):
    return "".join(strings_input)


def concatenate_strings_immutable(strings_input):
    string = ""
    for str in strings_input:
        string = string + str
    return string


# Start the timer
start_time = time.time()

# Code block to measure execution time
# Replace this with your actual code
concatenate_strings_mutable(strings)

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
execution_time = end_time - start_time

# Print the execution time
print(f"Execution time using mutable: {execution_time} seconds")


# Start the timer
start_time = time.time()

# Code block to measure execution time
# Replace this with your actual code
concatenate_strings_immutable(strings)

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
execution_time = end_time - start_time

# Print the execution time
print(f"Execution time using immutable: {execution_time} seconds")
