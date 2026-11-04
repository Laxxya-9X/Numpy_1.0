import numpy as np

a = np.array([[2,3],
              [2,3]])
b = np.array([[4,5],
              [4,5]])

res = np.concatenate((a,b))      #default row wise
print(res)
res = np.concatenate((a,b),axis=0)    #row wise
print(res)
res = np.concatenate((a,b),axis=1)     #colom wise
print(res)

