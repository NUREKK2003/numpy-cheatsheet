import numpy as np

# Basics
# a = np.array([1,2,3])
# print(a)
#
# b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# print(b)
#
# print(a.ndim)
# print(b.shape)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)
# print(a.nbytes)


# Accesing specified elements

# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)
#
# # Get a specific element [r c]
# print(a[1, 5])
#
# # Get a specific row
# print(a[0, :])
#
# # Get a specific column
# print(a[:, 2])
#
# # startIndex:endindex:stepSize
# print(a[0, 1:6:2])
#
# a[1, 5] = 20
# print(a)
#
# a[:, 2] = [1, 2]
# print(a)

# Initializing diffrent types of Arrays

# All 0s matrix
# print(np.zeros((5,2)))
#
# # All 1s matrix
# print(np.ones((5,2)))
#
# # Any other number
# print(np.full((2,2),99))
#
# # Any other number look like
# a = np.array([1,2,3])
# print(np.full_like(a,4))
# print(np.full_like(a.shape,4))
#
# # random decimal numbers
# print(np.random.rand(4,2))
#
# # random integer
# print(np.random.randint(-4,7,size=(3,3)))
#
# print(np.identity(5))
#
# # Repeat array
# arr = np.array([1,2,3])
# r1 = np.repeat(arr,3)
# print(r1)
#
#
# ouput = np.ones((5,5))
# print(ouput)
#
# z = np.zeros((3,3))
# print(z)
# z[1,1] = 9
# print(z)
#
# ouput[1:-1,1:-1] = z
# print(ouput)

# copying arrays

# a = np.array([1,2,3])
# b = a.copy()
# b[0] = 100
# print(a)

# MAthematics

# a = np.array([1,2,3,4])
#
# print(a + 2)
# print(a - 2)
# print(a * 2)
# print(a / 2)
#
# b = np.array([1,0,1,0])
#
# print(a + b)
#
# print(a **2)
#
# print(np.sin(a))

# Linear Algebra

# a = np.ones((2,3))
# print(a)
#
# b = np.full((3,2),2)
# print(b)
#
# print(np.matmul(a,b))
#
# c = np.identity(3)
# print(np.linalg.det(c))
#
# # statistics
# stats = np.array([[1,2,3],[4,5,6]])
# print(stats)
#
# print(np.min(stats))
# print(np.max(stats, axis=1))
# print(np.sum(stats, axis=0))

# Reorginazing arrays

# before = np.array([[1,2,3,4],[5,6,7,8]])
#
# print(before)
#
# after = before.reshape((8,1))
# print(after)
#
# # Verticly stacking vectors
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
#
# print(np.vstack([v1,v2,v2,v2]))
#
# # Horizontal stack
# h1 = np.ones((2,4))
# h2 = np.zeros((2,2))
#
# print(np.hstack((h1,h2)))

# Load data from file

filedata = np.genfromtxt('data.txt',delimiter=',')

filedata = filedata.astype('int32')


# Boolean Masking and Advenced indexing

print(filedata > 50)

print(filedata[filedata > 50])



