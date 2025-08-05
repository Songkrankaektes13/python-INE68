set_a = {1, 2, 3, 4}
set_b = {2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

print("Is set_a a superset of aet_b?:", set_a >= set_b)
print("Is set_b a subset of set_a?:", set_b <= set_a)

print("Is set_a proper superset of set_b?:", set_a > set_b)
print("Is set_b a proper subset of set_a?:", set_b < set_a)

print("Are set_a and set_c equal?:", set_a == set_c)
print("Is set_b a subset of set_d and not equal?:", set_b <= set_d and set_b != set_d)