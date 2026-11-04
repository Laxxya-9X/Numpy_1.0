import numpy as np

arr = np.arange(1,1000001)

#square using normal method like loop

# res = [x**2 for x in arr]

# print(res)

#using numpy

res2 = arr**2

print(res2)