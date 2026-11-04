import numpy as np
d_1 = np.array([1,2,3,4,5])
print(d_1)
print(d_1.shape)
# print(type(d))
# avg = np.mean(d)
# print(avg)

d_2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])

print(d_2)
print(d_2.shape)

d_3 = np.array([[[1,2,3,4,5],
                 [1,2,3,4,5]],
                [[1,2,3,4,5],
                [1,2,3,4,5]]])
print(d_3)
print(d_3.ndim)
print(d_3.shape)
print(d_3.size)
print(d_3.dtype)
print(d_3.reshape(1,4,5))