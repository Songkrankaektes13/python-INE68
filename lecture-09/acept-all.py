try:
    print("Starting the progame")
    value = int(input("Enter a number: "))
    print(f"Value: {value}")
    result = 10 / value
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")

print("End of program")