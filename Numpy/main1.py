import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9,0])
# 2D Array:
arr = np.array([[1,2,3],[4,5,6]])

# Special Arrays:
# zeros = np.zeros((3,3)) #3x3 matrix of zeros
# ones = np.ones((2,4)) #2x4 matrix of ones
# random_arr = np.random.random((2,2))



# Sequences:
# arr = np.arange(0,10,2) # [0,2,,4,6,8]
# arr_linspace = np.linspace(0, 1, 5)  # [0.  0.25  0.5  0.75  1.]

# 3. Array Properties
# print(arr.shape)       # Shape of the array
# print(arr.size)        # Number of elements
# print(arr.ndim)        # Number of dimensions
# print(arr.dtype)       # Data type of elements

# 4. Indexing and Slicing
# 1D Array:
# print(arr[1])          # Access the second element
# print(arr[1:4])        # Slice from index 1 to 3v

# 2D Array:
# print(arr[0, 1])    # Access first row, second column
# print(arr[:, 1])    # Access all rows, second column
# print(arr[1, :])    # Access second row, all columns


# 5. Basic Array Operations

# Arithmetic:
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)           # [5 7 9]
# print(a * b)           # [4 10 18]


# Broadcasting:
# print(arr * 10)        # Add 10 to each element

# Matrix Multiplication:
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# result = np.dot(A, B)
# print(A)
# print(B)
# print(result)

# Element-wise Operations:
# print(np.sqrt(arr))    # Square root
# print(np.sum(arr))     # Sum of elements
# print(np.mean(arr))    # Mean of elements
# print(np.max(arr))     # Maximum value

