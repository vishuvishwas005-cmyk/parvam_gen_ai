# Introduction to NumPy

import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
random_arr = np.random.rand(3, 3)

print("1D Array:", arr1)
print("2D Array:")
print(arr2)
print("Zeros array:")
print(zeros)
print("Ones array:")
print(ones)
print("Random array:")
print(random_arr)

# Array properties
print("Shape of arr2:", arr2.shape)
print("Size of arr2:", arr2.size)
print("Data type of arr1:", arr1.dtype)
print("Number of dimensions of arr2:", arr2.ndim)

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Scalar multiplication:", 2 * a)

# Array indexing and slicing
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Original array:")
print(arr)
print("Element at [1, 2]:", arr[1, 2])
print("First row:", arr[0, :])
print("First column:", arr[:, 0])
print("Subarray [1:3, 1:3]:")
print(arr[1:3, 1:3])

# Array functions
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))