# Generate all permutations of the elements in the array
def permutations(arr):
    # Base case: if the array is empty, return a list with an empty permutation
    if len(arr) == 0:
        return [[]]

    result = []
    for i in range(len(arr)):
        # Extract the current element
        current = arr[i]
        # The rest of the array without the current element
        rest = arr[:i] + arr[i+1:]

        # Generate all permutations of the rest
        for p in permutations(rest):
            result.append([current] + p)

    return result


if __name__ == "__main__":
    arr = "AGOSTINA"
    result = permutations(arr)
    with open("permutations.txt", "w") as f:
        for i in result:
            f.write("".join(i) + "\n")
