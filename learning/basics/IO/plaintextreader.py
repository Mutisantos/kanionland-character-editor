import os
# Construct the file path relative to the current script
file_path = os.path.join(os.path.dirname(__file__), "guerrero.txt")
original_lines = []
# The mode R states which operations are allowed on file.
# with open(file_path, "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())# Print each line without extra newlines

# The readlines() method reads all lines
# with open(file_path, "r", encoding="utf-8") as file:
#     original_lines = file.readlines()
# The print shows reserved characters, as an array of strings
#     print(lines)

# The mode A states that content will be appended at the end of the file
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n\n Written By: BeakLimit")  # Append a new line to the file
with open(file_path, "r", encoding="utf-8") as file:
    original_lines = file.readlines()
    print(original_lines[len(original_lines) - 1])  # Print the last line added

# The mode W states that content will be (over)written with the provided
# content
with open(file_path, "w", encoding="utf-8") as file:
    file.write("\n\n Written By: BeakLimit")  # Append a new line to the file
with open(file_path, "r", encoding="utf-8") as file:
    print("--------After overwrite:")
    for line in file:
        print(line.strip())  # Print each line without extra newlines
    print("---------------------- :")
with open(file_path, "a", encoding="utf-8") as file:
    for line in original_lines:
        file.write(line)  # Restore the original content
