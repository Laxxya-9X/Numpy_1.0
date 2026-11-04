import numpy as np


a = np.array([[2,3],
              [1,3]])

res = np.delete(a,1,axis=0)   #row at index 1 deleted

print(res)

res1 = np.delete(a,1,axis=1)   #col at index 1 deleted

print(res1)

res2 = np.delete(a,(0,1),axis=1)  # multiple cols deleted
print(res2)
