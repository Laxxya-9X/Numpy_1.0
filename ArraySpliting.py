import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])

a1,a2,a3 = np.split(a,3)

print(a1)
print(a2)
print(a3)

# Horizontal spliting

b = np.array([[1,2,3,4],
              [5,6,7,8]])

b1,b2 = np.hsplit(b,2)

print(b1)
print(b2)

# Horizontal spliting

c = np.array([[1,2,3,4],
              [5,6,7,8]])

c1,c2 = np.vsplit(c,2)

print(c1)
print(c2)