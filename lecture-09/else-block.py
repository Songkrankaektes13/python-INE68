try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Connot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")

print("End of program")