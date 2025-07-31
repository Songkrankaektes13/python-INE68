numbers = [4, 2, 9, 1, 5, 6]
length = len(numbers)
print(f"length of thhe list: {length}")

total_sum  = sum(numbers)
print(f"sum of all elements: {total_sum}")

max_value = max(numbers)
print(f"maximum value: {max_value}")

min_value = min(numbers)
print(f"mininum value: {min_value}")

sorted_numbers = sorted(numbers)
print(f"sorted list: {sorted_numbers}")

bool_list = [False, True, False]
any_true = any(bool_list)
print(f"is any element true? {any_true}")

all_true = all(bool_list)
print(f"are all element true? {all_true}")

string = "hello"
char_list = list(string)
print(f"list of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"reversed list: {reversed_numbers}")

enumerate_nuumbers = list(enumerate(numbers))
print(f"enumerated  list: {enumerate_nuumbers}")
