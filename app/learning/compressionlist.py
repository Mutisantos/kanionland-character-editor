
squares = [x**3 for x in range(1, 11)]
print("Cubed values:", squares)

celcius = [0, 10, 17, 21, 28, 30, 34, 37, 40]
# Inline operation can change every element on the list
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
# Equivalent for int i =0; i < len(celcius); i++
for i in range(len(celcius)):
    print("{:.2f}C = {:.2f}F".format(celcius[i], fahrenheit[i]))
# Filter list with condition
oddNumbers = [x for x in range(1, 21) if x % 2 != 0]
print("Odd numbers:", oddNumbers)

baseMatrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Transpose matrix
transposed = [[row[i] for row in baseMatrix]
              for i in range(len(baseMatrix[0]))]
for row in transposed:
    print(row)

transposed = []
for i in range(len(baseMatrix[0])):
    new_row = []
    for row in baseMatrix:
        new_row.append(row[i])
    transposed.append(new_row)

for row in transposed:
    print(row)
