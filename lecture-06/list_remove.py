fruits_with_duplictes = ["apple","banana","apple","cherry","apple","kiwi"]
while "apple" in fruits_with_duplictes:
    fruits_with_duplictes.remove("apple")
print(f"Fruits after remove: {fruits_with_duplictes}")