# โครงสร้างข้อมูล
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def find_most_expensive(inventory):
    max_price = -1
    max_name = ""
    for item in inventory:
        if item[2] > max_price:
            max_price = item[2]
            max_name = item[0]
    return max_name

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])

# ตัวอย่างการใช้งานตาม Actions
update_inventory(inventory, "Banana", 20)
print("After selling 20 bananas:", inventory)

total = calculate_total_value(inventory)
print("Total value:", total)

expensive = find_most_expensive(inventory)
print("Most expensive item:", expensive)

add_item(inventory, "Eggs", 30, 0.25)
print("After adding Eggs:", inventory)

add_item(inventory, "Eggs", 50, 0.30)
print("After updating Eggs:", inventory)