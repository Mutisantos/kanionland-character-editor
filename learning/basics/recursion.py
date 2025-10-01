def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n, memo={}):
    if n in memo:
        print(f"{n}th step -> {memo}")
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(f"Factorial of 5: {factorial(5)}")
print(f"10th Fibonnaci Number: {fibonacci(10)}")
