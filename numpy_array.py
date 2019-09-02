# https://towardsdatascience.com/numpy-python-made-efficient-f82a2d84b6f7
import numpy as np

# Define an array with integer elements 1, 2, 3, 4
integerArray = np.array([1, 2, 3, 4], int)

# We can access these elements by using index values.
print(integerArray[0])
# Output: 1

# We can also use ranges to access values
print(integerArray[:2])
# Output: [1 2]

# Find if a value exist in the array
# Returns ture if value exist else returns false.
print( 2 in integerArray)
# Output: True

integerArray2 = np.array([5, 6], int)

# Concatenate two arrays
print(np.concatenate((integerArray, integerArray2)))
# Output: [1 2 3 4 5 6]

# Array of zero
print(np.zeros(10))
# Output: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Array of ones with type int
print(np.ones(10, dtype = int))
# Output: [1 1 1 1 1 1 1 1 1 1]

# Range of numbers
rangeArray = np.array(range(10), int)
print(rangeArray);


## Multidimensional array
floatArray = np.array([[1, 2, 3], [4, 5, 6]], float)
print(floatArray)
# Output:
# [[1. 2. 3.]
#  [4. 5. 6.]]

# Convert one dimensional to multidimensional arrays
rangeArray = rangeArray.reshape(5, 2)
print(rangeArray)
# Output:
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]

# Convert multidimensional to one dimensional array
rangeArray = rangeArray.flatten()
print(rangeArray)
# Output: [0 1 2 3 4 5 6 7 8 9]

# Concatenation of multidimensional arrays
arr1 = np.array([[1, 2], [3, 4]], int)
arr2 = np.array([[5, 6], [7, 8]], int)
print(np.concatenate((arr1, arr2)))
# Output:
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]

# Based on dimensional 1
print(np.concatenate((arr1, arr2), axis = 0))
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Based on dimensional 2
print(np.concatenate((arr1, arr2), axis = 1))
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]


## Numpy Array Operations
print("Array 1\n {}".format(arr1))
print("Array 2\n {}".format(arr2))
# Output:
# Array 1
#  [[1 2]
#  [3 4]]
# Array 2
#  [[5 6]
#  [7 8]]

# not finished

