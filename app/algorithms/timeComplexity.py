# Measure time spent to execute a function
import time
import random
# With big O notation, we describe the time complexity of an algorithm
# The notation ignores constants and lower order terms, focusing in the highest order term
# Asintotic apporach focuses in the function behavior trend as it goes to infinity
# In the following example, it is O(n^2), ignoring the first loop that is constant and
# the second loop that is linear (n)
# Also, contants are ommited on big O notation


def g(x):
    accumulator = 0
    for i in range(100):
        accumulator += 1
    for i in range(x):
        accumulator += i
    for i in range(x):
        for j in range(x):
            accumulator += i
    return accumulator

# Recursive fibonacci requires 2 calls per recursive call (n-1), (n-2) until the nth element
# Therefore it has a time complexity of O(2^n)


def recursive_fibonacci(nth):
    if (nth == 0):
        return 1
    if (nth == 1):
        return 1
    return recursive_fibonacci(nth - 1) + recursive_fibonacci(nth - 2)

# Memoized approach defines a dictionary of previous calls to avoid redundant calculations
# In this case, every call will store their result so the next call will not need to calculate it again
# Therefore it has a time complexity of O(n): linear growth


def memoized_fibonacci(nth):
    initial_time = time.time()
    memo = {1: 1, 2: 1}

    def helper(x):
        if x not in memo:
            memo[x] = helper(x - 1) + helper(x - 2)
        return memo[x]
    result = helper(nth)
    finish_time = time.time()
    print(
        f"Memoized fibonacci time: {finish_time - initial_time}: {result:.2e}")
    return result
    # Recursive factorial requires n recursive calls
    # Therefore it has a time complexity of O(2^n): exponential growth


def recursive_factorial(n):
    initial_time = time.time()
    if n == 1:
        return 1
    else:
        result = n * recursive_factorial(n - 1)
    finish_time = time.time()
    print(
        f"Recursive factorial time: {finish_time - initial_time}: {result:.2e}")
    return result

# Memoization stores the results of previous calls to avoid redundant calculations
# Therefore it has a time complexity of O(n): linear growth
# The memo is a dictionary that stores the results of previous calls and is passed as reference to next calls


def memoized_factorial(n):
    initial_time = time.time()
    memo = {1: 1}

    def helper(x):
        if x not in memo:
            memo[x] = x * helper(x - 1)
        return memo[x]
    result = helper(n)
    finish_time = time.time()
    print(
        f"Memoized factorial time: {finish_time - initial_time}: {result:.2e}")
    return result

# Find an element in an array sequentially
# Despite breaking the loop, the time complexity is still O(n)
# As the function must iterate over all elements to find the target in worst case scenarios
# Best case scenario is O(1), where the first element is the one to find


def linear_search(arr, target):
    initial_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            finish_time = time.time()
            print(
                f"Linear search time: {finish_time - initial_time}: {arr[i]}, {i}")
            return (i, target)
    finish_time = time.time()
    print(f"Linear search time: {finish_time - initial_time}: No item found")
    return (-1, target)

# Algorithmics require a divide and conquer approach
# Meaning that the problem must be splitted in smaller problems to solve it
# Binary search requires the array to be sorted
# Therefore it has a time complexity of O(log n): logarithmic growth (each iteration halves the array progressively)
# However, sorting the array requires O(n log n) time complexity


def binary_search(arr, target):
    arr = sorted(arr)
    initial_time = time.time()
    left = 0  # initial position
    right = len(arr) - 1  # final position
    while left <= right:  # As long as there are elements to search
        # Split the array in half with floor division, forcing an int
        mid = (left + right) // 2
        # Then check the direction where the target should be located, if exists
        if arr[mid] == target:  # If the middle element is the target
            finish_time = time.time()
            print(
                f"Binary search time: {finish_time - initial_time}: {arr[mid]}, {mid}")
            return (mid, target)
        elif arr[mid] < target:  # If the middle element is less than the target
            left = mid + 1  # Move the left pointer to the current middle
        else:  # If the middle element is greater than the target
            right = mid - 1  # Move the right pointer to the current middle
    finish_time = time.time()
    print(f"Binary search time: {finish_time - initial_time}: No item found")
    return (-1, target)


def generate_random_array(length):
    return [random.randint(0, length) for i in range(length)]


if __name__ == "__main__":
    recursive_factorial(100)
    memoized_factorial(100)
    arr = generate_random_array(1000000)
    result_tuple = linear_search(arr, 255)
    print(
        f'Element {result_tuple[1]} {f"found at index {result_tuple[0]}"  if result_tuple != -1 else "not found"}')
    result_tuple = binary_search(arr, 255)
    print(
        f'Element {result_tuple[1]} {f"found at index {result_tuple[0]}"  if result_tuple != -1 else "not found"}')
