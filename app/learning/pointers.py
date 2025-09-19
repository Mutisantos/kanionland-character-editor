# Array Operations
a_array = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 8, 6, 3]
b_array = a_array
print(f"{a_array} vs {b_array}")
del a_array[a_array.index(3)]
# variables will share the same memory segment if they are copied.
# Modifying one will result in modifying their copies
print(f"{a_array}{id(a_array)} vs {b_array}{id(b_array)}")
c_array = a_array[:]
print(f"{a_array} vs {c_array}")
# In contrast, slicing decouples the copied reference in different memory
# segments
del a_array[a_array.index(3)]
print(f"{a_array}{id(a_array)} vs {c_array}{id(c_array)}")

# Matrix operations
a_matrix = [[1, 2, 3],
            [4, [5, 1], 6],
            [7, 8, 9]]
print(f"{a_matrix[1][1][0]}")

# Tuple operations (inmutable objects)
a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)

# Dictionary operations (Map-esque approach like Java)
configMap = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
configMap_prod = {
    "host": "180.166.0.10",
    "port": 8080,
    "debug": False
}
print("host:" + configMap["host"])
print(configMap.keys())
print(configMap.values())
print(configMap.items())  # key-value pairs

# Dictionaries can hold dictionaries inside them too
configMaps = {"local": configMap, "prod": configMap_prod}
# Indirection inside f-strings need single quote
print(f"Local:{configMaps['local']}")
print(f"Prod:{configMaps['prod']}")


# Loop Operations
for index, item in enumerate(c_array):
    print(f"--{index+1}::{item}")

for key, value in configMaps.items():
    print(f"{key}:{value}")

for item in range(9, 22, 2):
    print(f"2-step:{item}")

# Iterator
# Iterators allow traversing through any kind of collection
# Also, they remain on the latest position after each iteration
_start = 1001
_limit = 1040
_iterator_odds = iter(range(_start, _limit + 1, 2))
for item in _iterator_odds:
    print(item)

# Generator methods
# Yield is used to produce a series of values over time, pausing after
# each one until the next value is requested


def fibonacci_sequence(n):
    a, b = 0, 1  # Set the initial values of the series
    while a < n:
        yield a  # Yield the current value of 'a'
        a, b = b, a + b  # Update the series


print("Fibonacci sequence up to 100:")
for num in fibonacci_sequence(100):
    print(num)
