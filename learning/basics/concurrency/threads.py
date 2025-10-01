# Usually, scripts handle their execution in a single thread
# However, Python can handle multiple threads for concurrent performance
# Concurrency splits a problem into smaller tasks to be executed in parallel
# - Ideal for I/O bound tasks (network requests, file I/O, etc.)
# - Threading, asyncio, etc.
# Parallelism executes tasks in parallel
# - Ideal for CPU bound tasks (complex calculations, etc.)
# - Multiprocessing, Pool,  etc.

import threading
from random import randint
import time


def process_request(request_id: int):
    print(f"Processing request {request_id}")
    rand_time = randint(1, 10)
    time.sleep(rand_time)
    print(f"Request {request_id} processed after {rand_time} seconds")


threads = []

for i in range(10):
    # target states which function will be executed by the thread
    # args as parameters (as iterable) passed for said target function
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    # trigger the thread execution
    thread.start()

# Wait for all threads to finish their execution
for thread in threads:
    thread.join()

print("All requests processed")
