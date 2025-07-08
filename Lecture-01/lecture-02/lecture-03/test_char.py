inchar = input("Input your character: ")
if inchar >= 'A' and inchar <= 'z':
    print("You in put upper Case Latter" , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put lower Case Latter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put Number Case Latter" , inchar)
else:
    print("It's not a letter or number." , inchar)