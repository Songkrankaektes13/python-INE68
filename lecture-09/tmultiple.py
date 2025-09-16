try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("End of program")