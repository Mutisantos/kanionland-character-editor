name="Baracus"
singleQuotedName='Baracus'
# Using triple quotes for multi-line strings
tripledQuotedNames='''
Baracus
Chandosín
Pomeranio
'''
stringArray= ["Baracus", 'Chandosín', 'Pomeranio']
# type(variable) gives the inferred type of the variable
print (f"{type(name)}: {name}")
print (f"{type(singleQuotedName)}: {singleQuotedName}")
print ("Type: {}, var: {}".format(type(tripledQuotedNames), tripledQuotedNames))

print(name[0])  # Accessing first character
print(name[-1]) # Accessing last character
print(name[0:4]) # Slicing first 4 characters
print(name[1:])  # Slicing from index 1 to end
print(name[:4])  # Slicing from start to index 4
print(name[:])   # Slicing the whole string

print(tripledQuotedNames.splitlines()) # Splitting multi-line string into list of lines
print(name.splitlines()) # Splitting single line string into list with one element
print(name * 5) # Repeating string 5 times
print(len(name+singleQuotedName)) # Length of concatenated strings
print(stringArray, end="<-----") # Printing list of strings