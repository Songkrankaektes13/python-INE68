class Animal:
    def __init__(self, name):
        self.name = name

    def apeak(self):
        return "Some sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
dog = Dog("Budy")
cat = Cat("ehiskers")

print(dog.speak())
print(cat.speak())