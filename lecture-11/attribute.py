class Dog:
    species = 'mammal' 

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("koekoe", 5)

print("{} is {} and {} is {}."
.format(dog1.name, dog1.age, dog2.name, dog2.age))

if dog1.species == "mammal":
    print("{} is a {}!" .format(dog1.name, dog1.species))