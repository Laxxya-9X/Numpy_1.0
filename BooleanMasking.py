import numpy as np

# a = np.arange(1,28).reshape(3,3,3)
# print(a)

# print(a[0,1:,1:])

price = np.array([10,20,30,40])
fruits = np.array(['A','B','C','D'])
c = price>20

print(c)
print(price[c])
print(fruits[c])

d = (price > 10) & (price<30)
print(price[d])
