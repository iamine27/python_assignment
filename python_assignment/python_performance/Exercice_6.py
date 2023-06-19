import functools
import time

# caching mechanism helps avoid redundant computations by reusing previously
# computed results.

# Fibonacci function without caching
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci function with caching using lru_cache
@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


if __name__ == "__main__":

    x = 38

    # Start the timer
    start_time = time.time()
    fib_x = fibonacci(x)
    # Stop the timer
    end_time = time.time()
    # Calculate the elapsed time
    execution_time = end_time - start_time
    # Print the execution time
    print(f"Execution time not using cached: {execution_time} seconds")

    # Start the timer
    start_time = time.time()
    fib_x = fibonacci_cached(x)
    # Stop the timer
    end_time = time.time()
    # Calculate the elapsed time
    execution_time = end_time - start_time
    # Print the execution time
    print(f"Execution time using cached: {execution_time} seconds")
