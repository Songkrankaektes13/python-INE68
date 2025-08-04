fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("grape")
print(fruits)

removed_item = fruits.pop()
print(removed_item)
print(fruits)

fruits.clear()
print(fruits)