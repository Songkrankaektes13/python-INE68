import numpy as np
random_matrix = np.random.randint(1, 11, size=(3, 3 ))
print("Random 3x3 Matrix:\n", random_matrix)

random_sum = np.sum(random_matrix)
print(f"\nSum of all elements: {random_sum}")

random_mean = np.mean(random_matrix)
print(f"Mean of all elements: {random_mean}")

tranaposed_matrix = np.transpose(random_matrix)
print("\nTransposed Matrix:\n", tranaposed_matrix)