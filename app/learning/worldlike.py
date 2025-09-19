# Interpreted Language: statements are executed line by line,
# no compilation process involved
# executed by python worldlike.py
print("Hello world from script")

# Loosely typed language: no need to declare variable types, they are
# inferred at runtime
x = 10
y = "Python"
z = f"Variable inlined: x:{x} and y:{y}"
# Inline print for variables using f-strings similar to C#
print(z)
# print(x+y)  # This will raise an error since you can't add int and str
# (in contrast with JS)


# Identation. Python uses indentation to define code blocks instead of
# braces or keywords
if x > 5:
    print("x is greater than 5")
    if y == "Python":
        print("y is Python")
elif x > 2 and x <= 5:
    print("x is between 2 and 5")
else:
    print("x is 5 or less")
    if y != "Python":
        print("y is not Python")
