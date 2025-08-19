heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

def display_heroes(hero_list):
    print("Heroes:", hero_list)

def add_hero(hero_list, hero):
    hero_list.append(hero)

def insert_hero(hero_list, index, hero):
    hero_list.insert(index, hero)

def remove_hero(hero_list, hero):
    while hero in hero_list:
        hero_list.remove(hero)

def display_sorted_heroes(hero_list, reverse=False):
    sorted_list = sorted(hero_list, reverse=reverse)
    print("Sorted heroes:", sorted_list)

# Example usage:
display_heroes(heroes)
add_hero(heroes, 'Superman')
display_heroes(heroes)
insert_hero(heroes, 2, 'Batman')
display_heroes(heroes)
remove_hero(heroes, 'Thor')
display_heroes(heroes)
display_sorted_heroes(heroes)
display_sorted_heroes(heroes, reverse=True)