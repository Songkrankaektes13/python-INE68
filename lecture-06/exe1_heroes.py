heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']


newheroes = heroes 
newheroes[0] ='superman'
print(heroes)

while "Thor" in heroes:
    heroes.remove("Thor")
print(f"heroes after remove: {heroes}")