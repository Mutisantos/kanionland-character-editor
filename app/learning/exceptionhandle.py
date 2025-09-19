result = 0
try:
    divisor = int(input("Enter a number to divide 10 by: "))
    result = 10 / divisor
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
except ValueError as e:  # Handling invalid input produced by incorrect casting
    print(f"Invalid input, only numeric values are valid: {e}")
except Exception as e:  # Catch the most generic exception
    print(f"An unexpected error occurred: {e}")
finally:
    print(f"Execution completed. Result {result}")
