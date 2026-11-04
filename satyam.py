import numpy as np
# l1 =[2,3,4,5]
# l2 =[6,7,8,9]

# res = []
# for i in range(len(l1)):
#     res.append(l1[i]+l2[i])

# print(res)

a = np.array([[[6,7,8,9],[6,7,8,9]],
              [[6,7,8,9],[6,7,8,9]]])
# print(a.dtype)
# print(a.shape)
# print(a.size)
# print(a.ndim)
print(a)
print(a.ndim)

b = np.arange(1,37).reshape(3,3,4)
print(b.ndim)