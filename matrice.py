import numpy as np

A = np.random.randint(0, 10, (3, 5))
B = np.random.randint(0, 10, (5, 3))

print("A =\n", A)
print("B =\n", B)
print("A + A =\n", A + A)
print("A + B =\n", A + B)
print("A @ B (produit) =\n", A @ B)
print("transposée de A =\n", A.T)
