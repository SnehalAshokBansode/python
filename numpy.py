# Tuples
x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

print("Original tuples:")
print(x)
print(y)
print(z)

# Element-wise sum of the tuples
print("\nElement-wise sum of the said tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)

# Using NumPy for list addition
from numpy import array

lst1 = [1, 5, 7]
lst2 = [3, 2, 1]

a = array(lst1)
b = array(lst2)

print("\nSum of the lists using NumPy:")
print(a + b)
