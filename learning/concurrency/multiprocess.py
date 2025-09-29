import multiprocessing
import random
import time


def calculate_cube(n):
    rand_time = random.randint(1, n+1)
    time.sleep(rand_time)
    print(f"Request {n} processed after {rand_time} seconds")
    return n * n * n


# Define the main process, the next processes will be secondary to this main process
if __name__ == "__main__":
    print(__name__)
    numbers = list(range(10))
    random.shuffle(numbers)
    # Create a pool of processes in parallel
    with multiprocessing.Pool(processes=4) as pool:
        # The pool will execute the function in parallel
        # The results list will be treated as a queue, where each result is pushed to the queue
        results = pool.map(calculate_cube, numbers)
    print(results, type(results))
    stringo = "0.12"
    stringo = float(stringo)
    print(stringo, type(stringo))
