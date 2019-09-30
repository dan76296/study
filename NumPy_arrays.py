import numpy as np

my_list = [1, 2, 3]

arr = np.array(my_list)

my_mat = [[1,2,3], [4, 5, 6], [7, 8, 9]]

np.array(my_mat)

print(my_mat)

# The same as pythons range
np.arange(0,10)

# A range, with a incremented step of 2
np.arange(0, 11, 2)

# Add zeros
np.zeros(3)

# 5 rows and 5 columns of zeros
np.zeros((5, 5))

# Same with ones
np.ones((3, 3))

# One dimensional vector of 10 evenly spaced points from 0-5
np.linspace(0, 5, 10)

# Evenly spaced 100 points
np.linspace(0, 5, 100)

# Identity matrix
np.eye(4)

# One dimensional array of random numbers
np.random.rand(5)

# Multiple lines
np.random.rand(5,5)

# -1 : 1
np.random.randn(2)

# random integers between low, high, count
np.random.randint(1,100,10)

# Range between 0 - 25
arr2 = np.arange(25)

# 10 random integers between 0, 50
ranarr2 = np.random.randint(0, 50, 10)

# Reshape range 0-25, as 5 x 5
arr.reshape(5, 5)

# return max
ranarr2.max()

# return min
ranarr2.min()

# return index
ranarr2.argmax()
ranarr2.argmin()

# can see the shape of an array
arr3 = arr.reshape(5,5)
arr3.shape

# can see the type of an array
arr.dtype
