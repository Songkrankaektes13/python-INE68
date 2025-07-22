'''
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()

print(counter)
'''

counter = 0

def increment():
    counter = 5
    counter += 1
    print(counter)

increment()
increment()

print(counter)