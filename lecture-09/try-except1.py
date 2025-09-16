try:
    x = 1 / 0  
except ZeroDivisionError as e:
    print(f"Error: {e}")

x = 2/0
print("End of program")