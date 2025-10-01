# recursive knapsack, as a first approach of the problem, but unefficient
def recursive_knapsack(weights, values, capacity, size):
    # Base case: return 0 value and empty list
    if capacity == 0 or size == 0:
        return (0, [])

    # If current item is too heavy, skip it
    if weights[size - 1] > capacity:
        return recursive_knapsack(weights, values, capacity, size - 1)

    else:
        # Option 1: Include current item
        reduced_capacity = capacity - weights[size - 1]
        # Get result from subproblem
        val_included, items_included = recursive_knapsack(
            weights, values, reduced_capacity, size - 1)
        total_val_included = values[size - 1] + val_included
        # Instead of append, as items_included could be empty
        new_items_included = items_included + [size - 1]

        # Option 2: Exclude current item
        val_excluded, items_excluded = recursive_knapsack(
            weights, values, capacity, size - 1)

        # Choose better option
        if total_val_included > val_excluded:
            print(
                f"Inc value: {total_val_included} --> [{new_items_included}]")
            return (total_val_included, new_items_included)
        else:
            print(f"Exc value: {val_excluded} --> [{items_excluded}]")
            return (val_excluded, items_excluded)


def memoized_knapsack_rep(weights, values, capacity, size, memo):
    # Base case: return 0 value and empty list
    if capacity == 0 or size == 0:
        return 0

    # If current item is heavier that the capacity, skip it by moving the call to size-1 (next item)
    if weights[size - 1] > capacity:
        return memoized_knapsack_rep(weights, values, capacity, size - 1, memo)

    include_item = 0
    if weights[size - 1] <= capacity:
        # If the current item fits into the bag, add it and then evaluate the next one
        include_item += values[size - 1]
        include_item += memoized_knapsack_rep(
            weights, values, capacity - weights[size - 1], size - 1, memo)
    # Also evaluate the scenario where the item is skipped (not added to the bag)
    exclude_item = memoized_knapsack_rep(
        weights, values, capacity, size - 1, memo)
    # Then check which option is the best
    if include_item > exclude_item:
        memo[size][capacity] = include_item
        return include_item
    else:
        memo[size][capacity] = exclude_item
        return exclude_item


def memoized_knapsack(weights, values, capacity, size):
    # Fill the memo matrix with -1, dividing the problem in subproblems
    # Where the column represents the capacity and the row represents the size
    # And in each position, we hold de maximum value got from that subproblem
    memoMatrix = [[-1 for i in range(capacity + 1)] for j in range(size + 1)]
    # The solution is in the last position of the matrix
    # Stating  that all elements were taken into account and the capacity was reached
    max_value = memoized_knapsack_rep(
        weights, values, capacity, size, memoMatrix)
    print(f"Maximum value: {max_value}")
    for row in memoMatrix:
        print(row)
    return max_value


# knapsack problem using dynamic programming
# Dynamic programming is a method for solving complex problems by breaking
# them down into simpler subproblems and storing the results of these
# subproblems to avoid redundant calculations.


def iterative_knapsack(capacity, values, weights):
    n = len(weights)
    # The matrix holds the maximum value got from each subproblem
    # Row repesents the items while the column represents the capacity of the knapsack
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0
                # Pick ith item if it does not exceed the capacity of knapsack
                if weights[i - 1] <= j:
                    pick = values[i - 1] + dp[i - 1][j - weights[i - 1]]
                # Don't pick the ith item
                notPick = dp[i - 1][j]
                # Check the best approach
                dp[i][j] = max(pick, notPick)
    print("Dynamic Programming Matrix:")
    for row in dp:
        print(row)
    return dp[n][capacity]


if __name__ == "__main__":
    # The problem must optimize the total value of the items in the knapsack
    # without exceeding the capacity
    values = [130, 30, 52, 22, 100, 77, 66]
    weights = [5, 2, 4, 3, 3, 5, 2]
    capacity = 8
    elements = len(values)
    max_value, selected_items = recursive_knapsack(
        weights, values, capacity, elements)
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {selected_items}")
    print(
        f"Memoized Knapsack: {memoized_knapsack(weights, values, capacity, elements)}")
    print(
        f"Iterative Knapsack: {iterative_knapsack(capacity, values, weights)}")
