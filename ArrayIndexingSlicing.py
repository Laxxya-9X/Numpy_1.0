import numpy as np

a = np.array([1,2,3,4,5])

# element appending or adding in last 
print(np.append(a,6))
print(a)
print(a.size)
b = np.append(a,6)
print(b.size)

#Note - append hone k baad bhi size change nhi hota actual array jo hai vhi rehta hai
# element removing from last
print(np.delete(a,4))



#colom addition or y axis addtion  --- 1
print(np.append(a,[1,2,3]))


# row addition to 2D array
b  = np.array([[1,2],
               [4,5]])
print(np.append(b,[[1,3]] , axis=0))

# colom addition to 2D array
c  = np.array([[1,2],
               [4,5]])
print(np.append(c,[[1],[4]] , axis=1))



