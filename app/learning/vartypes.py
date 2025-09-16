_integer = 10
_float = 2.71828
_scientific = 6.023e23
_boolean = True #Boolean values are case-sensitive
print(f"{type(_integer)}: {_integer}")
print(f"{type(_float)}: {_float}")
print(f"{type(_scientific)}: {_scientific}")
# Special float format rounds up values to fit provided format
print("Valor: {:.2f}".format(_float))
print(f"{type(_boolean)}: {_boolean}")
_boolean = False
print(f"{type(_boolean)}: {_boolean}")

#Numeric Operators
print(f"+ = {_integer + _float}")
print(f"- = {_integer - _float}")
print(f"* = {_integer * _float}")
print(f"** (a^b) = {_integer ** _float}")
print(f"/ = {_integer / _float}")
print(f"// = {_integer // _float}") #Integer Division
print(f"% = {_integer % _float}")

#Shorthand operators
_integer += 5
print(f"Shorthand += : {_integer}")

#Arrays and Lists
#Arrays can hold different types of variables
to_do_list = ["Taxes", "Services", "Groceries", "Courses", 55, [True, False, False]]
print(f"{type(to_do_list)}-{to_do_list}")
to_do_list.append("New Element")
to_do_list.insert(2, "Second Slot")
print(f"{type(to_do_list)}-{to_do_list}")
foundIndex = to_do_list.index("Second Slot")
print(f"Second Slot Position: {foundIndex}")

# Query list operations
nums = [1,4,120,-102,12,5,22]
print (nums, max(nums))
print (nums, min(nums))
del nums[:3]
print (nums, max(nums))
print (nums, min(nums))