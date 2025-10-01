# O(n^2) time complexity, using an auxiliar element for swapping until the array is sorted

def bubble_sort(arr):
    # Iterate over all positions of the array
    for i in range(len(arr)):
        # Traverses again the array in a lineal manner, even if the length is being reduced in each upper iteration
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # Python's swapping notation
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Despite not using an auxiliar element, Insertion Sort is still O(n^2) time complexity
# It will traverse all the array in a lineal manner, even if the length is being reduced in each upper iteration


def insert_sort(arr):
    print(arr)
    # Start from the second element, so it will be compared with the previous one
    for i in range(1, len(arr)):
        j = i
        # Compare the element with the previous one, if it is smaller, swap them
        while j > 0 and arr[j] < arr[j - 1]:
            # Does swapping without an aditional variable as Bubble's
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        print(arr)
    return arr

# Merge Sort is a divide and conquer algorithm
# It will divide the array in two halves, sort them and then merge them


def merge_sort(arr):
    # Split the array recursively until no more splits can be made
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Split the arrays in two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(arr, left, right)


def merge(main_arr, left_arr, right_arr):
    # Iterators for sublists
    i = j = 0
    # Iterator for the main list
    k = 0
    # As long as there are elements in both sublists
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            # Add the element to the main list
            main_arr[k] = left_arr[i]
            i += 1
        else:
            main_arr[k] = right_arr[j]
            j += 1
        k += 1
    # If there are elements left in the left array
    while i < len(left_arr):
        main_arr[k] = left_arr[i]
        i += 1
        k += 1
    # If there are elements left in the right array
    while j < len(right_arr):
        main_arr[k] = right_arr[j]
        j += 1
        k += 1
    print(main_arr)
    return main_arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr_b = [64, 34, 25, 12, 22, 11, 90]
    arr_c = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    insert_sort(arr_b)
    print("-----------Merge Sort-----------")
    merge_sort(arr_c)
    squares = [x**2 for x in arr_c]
    print(squares)
