import numpy as np

a = np.array([[2,3],
              [2,3]])

res1 = np.insert(a,1,[6,7], axis=0)        # row insertion
print(res1)
res2 = np.insert(a,1,[6,7], axis=1)         #colom insertion
print(res2)