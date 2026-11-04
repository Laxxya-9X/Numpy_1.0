import numpy as np

a = np.array([1,2,3])
b = np.array([5,6,7])

print(np.stack((a,b)))
print(np.hstack((a,b)))
print(np.vstack((a,b)))

c = np.full((2,2),4)

