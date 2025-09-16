#functional operators
_functionpower = lambda x, y: x ** y
print(f"5 ^ 5: {_functionpower(5,5)}")

#lambda operations
numbers = [1,2,3,4,5,6,7,8,9,10]
# Map states the operation for each element on the list, then get the resulting elements as list
doubled = list(map(lambda x: x*2, numbers))
print(f"Squared: {doubled}")
# Filter will only return the elements that meet the condition
oddNumbers = list(filter(lambda x: x % 2 != 0, doubled))
print(f"Odd numbers: {oddNumbers}") 
#Inner operations will occur first, so filter will be applied before map, removing even numbers and then multiplying the odd results by 2
singleOperation = list(map(lambda x: x*2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Single operation (filter then map): {singleOperation}")

