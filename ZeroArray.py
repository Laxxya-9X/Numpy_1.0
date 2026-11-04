import numpy as np

# zero array creation default array
zero_Array = np.zeros((3,3))

print(zero_Array)

#default indentity array creation 
ones_Array = np.ones((3,3))

print(ones_Array)

# constant array creation 

constant_Array = np.full((3,3), 15)

print(constant_Array)

# diagonal array in a square matrix

diagonal = np.eye(3)
diagonal2 = np.eye(3,5)
print(diagonal)
print(diagonal2)

# range array creation
range_arr = np.arange(0,11,2)

print(range_arr)

# deviding  range into given pieces

line_arr = np.linspace(0,10,5)
print(line_arr)

# creation of 2d array from a range by reshaping that

arr= np.arange(6).reshape((3,2))

print(arr)


ar = np.array([[1,2,3],[6,5,4]])

flat = ar.flatten()
transpose  = ar.T
print(transpose)
print(flat)