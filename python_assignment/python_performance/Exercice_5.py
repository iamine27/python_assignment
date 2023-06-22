import multiprocessing
import threading
import time


# CPU-bound task: Calculate the sum of squares
def calculate_sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


# Using multiprocessing
def using_multiprocessing():
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sum_of_squares, [1000000] * 100)
    return results


# Using threading
def using_threading():
    results = []
    threads = []
    for _ in range(100):
        t = threading.Thread(
            target=lambda: results.append(calculate_sum_of_squares(1000000))
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return results


if __name__ == "__main__":
    # Start the timer
    start_time = time.time()
    result_threading = using_threading()
    # Stop the timer
    end_time = time.time()
    # Calculate the elapsed time
    execution_time = end_time - start_time
    # Print the execution time
    print(f"Execution time using threading: {execution_time} seconds")
    print(f"Result using threading: {result_threading}")

    # Start the timer
    start_time = time.time()
    result_multiprocessing = using_multiprocessing()
    # Stop the timer
    end_time = time.time()
    # Calculate the elapsed time
    execution_time = end_time - start_time
    # Print the execution time
    print(f"Execution time using multiprocessing: {execution_time} seconds")
    print(f"Result using multiprocessing: {result_multiprocessing}")
