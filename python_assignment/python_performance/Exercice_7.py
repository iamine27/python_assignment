import time

# lazy evaluation. This approach avoids the need to store all the results in
# memory before processing them, which can be crucial for large computations.

# Function using yield for computation
def compute_with_yield(n):
    for i in range(n):
        yield i * 2


# Function without using yield for computation
def compute_without_yield(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result


x = 1000000000

# Computation time using yield
start_time = time.time()
for item in compute_with_yield(x):
    pass
end_time = time.time()
yield_time = end_time - start_time

print(f"Computation time using yield: {yield_time} seconds")

# Computation time without yield
start_time = time.time()
result = compute_without_yield(x)
for item in result:
    pass
end_time = time.time()
no_yield_time = end_time - start_time

print(f"Computation time without yield: {no_yield_time} seconds")
