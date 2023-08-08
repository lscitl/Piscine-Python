#!/usr/bin/python3

from array2D import slice_me

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print()
print(slice_me(family, 1, -2))
print()
print(slice_me(family, 1, -4))
print()
print(slice_me(family, -2, -1))
print()


print("--------------------------------")
print()
family = [1, 2, 3]
print(slice_me(family, 0, 2))
print()

family = []
print(slice_me(family, 0, 0))
print()

family = [[]]
print(slice_me(family, 0, 4))
print()

print("--------------------------------")
print()
family = [[1.80, 78.4], [2.15, 102.7], (3, 4)]
print(slice_me(family, 0, 4))
print()

family = [[1.80, 78.4], [2.15, 102.7], 3, 4]
print(slice_me(family, 0, 4))
print()

family = [[1.80, 78.4], [2.15, 102.7], ["a", 4]]
print(slice_me(family, 0, 4))
print()
