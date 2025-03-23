# Numpy : Fundamental package for array operations in python

# Array : Array is a data structure to hold group of elements of same data type

# Install :  pip install numpy
# Use : import numpy as np

import numpy as np


# Array fundamentals
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

# access/indexing
print(a[0])

# slicing can also be used
print(a[:3])
# Note: List slicing copies the elements into a new list,
# but slicing an array returns a view: an object that refers to the data in the original array

# a = np.array(1, 2, 3, 4)    # WRONG

# Use list to create numpy arrays

list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
array1 = np.array(list1)

# array[row index][col index]
print(array1[0][2])

# cons : difficult to access large array, loop through each element and index is computationally inefficient

# Advantages :  Arrays let us perform complex computations on entire block of data easily without loop through
#               Numpy based algorithms runs order of magnitudes faster than traditional approaches in native python
#               Not only faster, data storage is contiguous, where as in lists, its non-contiguous => smaller memory space

arr_0d = np.array(1) # scalar
arr_1d = np.array([0,1,2]) # vector
arr_2d = np.array([[0,1,2], [3,4,5]]) # matrix
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # tensor

# Array attributes: dimension, shape, size and dtype

# dimension : the number of indexes required to access an element from the array
print(arr_3d.ndim)

# shape : is a tuple of integers representing the size along each dimension, starting with the first dimension
print(arr_3d.shape)

# size : total number of elements
print(arr_3d.size)

# dtype :  homogenous, what type?
print(arr_3d.dtype)

np.array([127, 128, 129], dtype=np.int8)

np.array([[1, 2], [3, 4]], dtype=complex)

# Understanding the array

# Create a basic array

np.zeros(2)
np.zeros([2, 3, 4])
# 2 Sets, 3 Rows per Set, 4 Columns

np.ones(2)

np.empty(2)
np.empty((2, 3))

np.arange(4)
np.arange(2, 9, 2)
np.arange(0, 2, 0.3)

# Array with linearly in a specified interval
np.linspace(0, 10, num=5)

# basic operations

p = np.array([20, 30, 40, 50])
q = np.arange(4)
p+q
p-q
p*q
p/q
p**2
p<3
10 * np.sin(p)

A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
A * B     # elementwise product

A @ B     # matrix product
# OR
A.dot(B)  # another matrix product

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

np.concatenate((a, b))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

np.concatenate((x, y), axis=0)
np.concatenate((x, y), axis=1)

a1 = 10
a2 = 20
np.add(a1, a2)

a3 = np.array([9, 7, 12])
scalar = 10
np.add(a3, scalar)

arr1 = np.arange(5)
arr2 = np.arange(8, 12)
np.append(arr1,arr2)

# reshape
np.arange(12)
np.arange(12).reshape(4, 3)
np.arange(24).reshape(2, 3, 4)

np.arange(10000)
np.arange(10000).reshape(100, 100)

b = np.arange(12).reshape(3, 4)
b.sum(axis=0) # sum of each column
b.min(axis=1) # min of each row


# session 2

# layout

# https://stackoverflow.com/questions/38155039/what-is-the-difference-between-native-int-type-and-the-numpy-int-types



# more functions to create numpy arrays


np.full((2, 2), np.inf)
np.full((2, 2), 10)


np.eye(2, dtype=int)
np.eye(3, k=1)

x = np.arange(6, dtype=int)
np.full_like(x, 1)
np.full_like(x, 0.1)
np.full_like(x, 0.1, dtype=np.double)
np.full_like(x, np.nan, dtype=np.double)


np.identity(3)

# convert a 1D array into a 2D array

a = np.array([1, 2, 3, 4, 5, 6])
a.shape

a2 = a[np.newaxis, :]
a2.shape

col_vector = a[:, np.newaxis]
col_vector.shape

b = np.expand_dims(a, axis=1)
b.shape

c = np.expand_dims(a, axis=0)
c.shape

# indexing and slicing

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a < 5])

five_up = (a >= 5)
print(a[five_up])

divisible_by_2 = a[a%2==0]
print(divisible_by_2)

c = a[(a > 2) & (a < 11)]
print(c)

five_up = (a > 5) | (a == 5)
print(five_up)

# slicing

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]

# more self exploration

# stacking and spliting

a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])


np.vstack((a1, a2))

np.hstack((a1, a2))

# splits
x = np.arange(1, 25).reshape(2, 12)
np.hsplit(x, 3)
np.hsplit(x, (3, 4))

# transpose

arr = np.arange(6).reshape((2, 3))
arr

arr.transpose() #or
arr.T

# reverse

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)

# faltten and ravel

# flatten, non mem efficient and orig array unaltered
x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x.flatten()

a1 = x.flatten()
a1[0] = 99
print(x)  # Original array
print(a1)  # New array

a2 = x.ravel()
a2[0] = 98
print(x)  # Original array
print(a2)  # New array

# vectorization and broadcasting

# save and load numpy arrays

a = np.array([1, 2, 3, 4, 5, 6])
np.save('C:\\Users\\Pavan Kulkarni\\PycharmProjects\\python_tutorials\\scilib\\filename.npy', a)

b = np.load('C:\\Users\\Pavan Kulkarni\\PycharmProjects\\python_tutorials\\scilib\\filename.npy')
print(b)

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr)
np.loadtxt('new_file.csv')