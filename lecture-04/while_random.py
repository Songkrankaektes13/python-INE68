import random

print("What is my magic number (1 to 100)?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
print("DEBUG: mynuber is", mynumber) #random number for testing

while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + ">>"
    if ntries == 6:
        msg = "Your last chance\n6>>"

    yourguess = int(input(msg))

    if yourguess > mynumber:
        print("--> too high")
    elif yourguess < mynumber:
        print("--> too low")

    ntries += 1

if yourguess == mynumber:
    print("Yes! it is", mynumber)
else:
    print("Sorry! my number is", mynumber)