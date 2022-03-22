# For this course, we will make heavy use of numerical libraries. The
# main ones "numpy" and "scipy". We won't use pre-built ML tools in most
# cases. Data visualization will rely on "matplotlib".

# Numpy main objects are multidimensional arrays (ndarray class). We
# will mainly use one-dimensional (vector) and two-dimensional
# (matrices) arrays (not to be confused with the (matrix) class).
import numpy
arr1 = numpy.array([1, 2, 3])
print("1-D array is:\n", arr1)
print("type of numpy array1 is", type(arr1))

# 2-D array represents a matrix
arr2 = numpy.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array is\n:", arr2)
print("type of numpy array2 is", type(arr1))

# Arrays have attributes that describe the array itself:
#   ndarray.size:  Total number of elements
#   ndarray.shape: Tuple with the number of elements for
#                  each axis — A m x n matrix will have a shape (m, n)
#   ndarray.ndim:  Number of axes
#   ndarray.dtype: The data type (for example, numpy.int32,
#                  numpy.float32, numpy.float64

# ndarray.size:  Total number of elements
print("\nTotal number of elements of", arr2, "is:", arr2.size)

# ndarray.shape: Tuple with the number of elements for each axis
print("\nShape of the matrix", arr2, "is:", arr2.shape)

# ndarray.ndim:  Number of axes
print("\nNumber of axes of the matrix", arr2, "is:", arr2.ndim)

# ndarray.dtype: The data type
print("\nData type of the matrix", arr2, "is:", arr2.dtype)

# Arrays can be created in many ways: From Python lists or tuples. To
# create multi-dimensional arrays, use nested lists. We can specify the
# data type passing the argument dtype:
list_l = [1, 2, 3, 4]
arr3 = numpy.array(list_l)
print("\narr3 is:", arr3, "and its type is:", type(arr3))
arr4 = numpy.array([1, 2, 3], dtype=numpy.float64)
print("\narr4 is:", arr4)

# Arrays can be created in many ways: As a copy of another array:
arr5 = arr3
print("\narr5 is", arr5, "and its type is", type(arr5))

# Arrays can be created in many ways: Using functions that create
# predefined arrays: zero, ones, arange, eye, ...
zero = numpy.zeros((2, 3))
print("\nzero array is:\n", zero)
zero2 = numpy.zeros((2, 3), dtype=numpy.float32)
print("\nzero2 array is:\n", zero2)
ones = numpy.ones((2, 3), dtype=numpy.int32)
print("\nones array is:\n", ones)
identity_m = numpy.eye(3, dtype=numpy.int32)
print("\nIdentity matrix of size 3x3 is:\n", identity_m)
ranged = numpy.arange(5)
print("\nranged array is:\n", ranged)

# The arange function is similar to the range function, and allows
# specifying a step size. It will leave a space as the defined distance
# between the elements.
ranged2 = numpy.arange(0, 10, 3)
print("\nranged2 will be a matrix with multiples of 3 until 10:\n", ranged2)

# If we want to create an array of evenly spaced values in a range, we
# can use "linspace". Becareful with linspace. For example down below,
# number 4 is not the step range, it is the number of elements in total,
# including starting point (1) and the ending point(10):
arr6 = numpy.linspace(1, 10, 4)
print("\narr6 is:\n", arr6)

# Arithmetic operators on numpy array operate element-wise! They require
# arrays with matching shapes:
x = numpy.array([[1, 2, 3], [4, 5, 6]])
y = numpy.array([[2, 2, 2], [3, 3, 3]])
print("\nx is:\n", x)
print("\ny is:\n", y)
print("\nx+y is:\n", x+y)
print("\nx*y is:\n", x*y)
# Normally you'd expect to see an error according to math, because we
# know from math that x: (2,3) and y:(2,3) but we know that for the
# multiplication we should have the from (m,n)x(n,k), but as we've said
# before, in numpy we operate element-wise. Also, arithmetic operators
# in general create new arrays. To modify an existing array, use
# in-place operators such as *= , += , ...

# Matrix product can be performed using the dot function, or the @
# operator (requires Python >= 3.5). This time dimensions should match:
x = numpy.array([[1, 2], [3, 4], [5, 6]])  # x: (3x2) matrix
y = numpy.array([[1, 1, 1, 1], [2, 2, 0, 2]])  # y: (2x4) matrix
z = x@y  # z will be a (3x4) matrix
print("\nx is:\n", x)
print("\ny is:\n", y)
print("\nx@y=z is:\n", z)
q = numpy.array([[1], [0], [0], [0]])
print("\nq is:\n", q)  # q:(4x1) matrix
r = numpy.dot(z, q)  # r will be a (3x1) matrix
print("\nzXq=r is:\n", r)

# Numpy arrays can be reshaped (the order of the data is preserved, but
# the shape is changed):
x = numpy.array([[1, 2], [3, 4], [5, 6]])  # x has 3x2=6 elements
print("\n x is:\n", x)
y = x.reshape((2, 3))  # that's why can reshape it as 2x3
print("\nreshaped x will be:\n", y)

# We will mainly use this to create row and column vectors:
arry = numpy.arange(3)  # will create [0,1,2]
print("\narry is:\n", arry)
arry_row = arry.reshape((1, arry.size))  # becomes a row vector
print("\nrow vector of arry is:\n", arry_row)
arry_column = arry.reshape((arry.size, 1))  # becomes a column vector
print("\ncolumn vector of arry is:\n", arry_column)

# Method ndarray.ravel() allows reshaping the array to a 1- dimensional
# vector.
arry2 = numpy.arange(12).reshape((2, 2, 3))  # 3-D matrix
print("\narry2 is:\n", arry2)
arry2_unrvl = arry2.ravel()
print("\n1-D ravel narry2 is:\n", arry2_unrvl)

# Please note that 1-dimensional arrays (shape (n,)) are NOT row vectors
# (shape (1, n))! There is also the x.flatten(), so there is more than
# one way to do things.
arry2_flttn = arry2.flatten()
print("\n1-D flatten narry2 is:\n", arry2_flttn)


# We will represent data mainly as "column" vectors, and data matrices
# will consist of horizontally stacked column vectors. Many ML libraries
# adopt the opposite convention — data points are represented as row
# vectors, and data matrices are made up of vertically stacked column
# vectors. So we will use the y=Ax mathematical notation, not y=xA in
# this course.

# Arrays can be transposed using the .T attribute. Transposition can be
# applied also to n-dimensional array — if interested check the
# documentation for the semantic, but we'll most likely not use it in
# this course.
x = numpy.arange(3).reshape((3, 1))
print("\nx is:\n", x)
x = x.T
print("\n x transposed is:\n", x)

# Numpy also provides functions (and methods) to perform reduction
# operations (e.g. sum or product of all elements, maximum, minimum).
# These functions operate over the whole array as if it were
# one-dimensional.
x = numpy.array([[1, 2, 3], [4, 5, 6]])
print("\nx is:\n", x)
print("\nsum of all elements of x is:", x.sum())
print("\nmax element of x is:", x.max())

# If we want to perform the operation over a specific axis, we can
# specify the axis parameter:
print("\nsum of rows of x is:", x.sum(axis=0))
print("\nsum of columns of x is:", x.sum(axis=1))

# Numpy also provides a set of element-wise functions that can be
# applied to all elements of an array, creating a new array:
x = numpy.array([[1, 2, 3], [4, 5, 6]])
print("\narray of e^(elements of x) is:\n", numpy.exp(x))
print("\narray of log(elements of x) is:\n", numpy.log(x))

# Please note that, whenever possible, it’s best to avoid iterating
# explicitly over array elements. The Python interpreter is slow, and
# loops are expensive. Numpy functions are implemented directly in C,
# and therefore loops are executed much faster.

# DON'T DO THIS:
#   s=0
#   x=numpy.arange(1000000)
#   for i in x:
#       s+=i

# DO THIS:
N = 1000000
x = numpy.arange(N)
s = x.sum()
print("\nsum of x is:", s, "\n")

# Arrays can be sliced. For 1-dimensional arrays, this is similar to
# Python lists:
x = numpy.arange(5)  # x = [0,1,2,3,4]
print(x[1:3])  # = [1,2]
print(x[::2])  # = [0,2,4]
print(x[3])    # = 3

# Multidimensional arrays allow specifying a slice for each axis. Note:
# if we specify a single value for an axis, we get an array with one
# dimension less:

x = numpy.arange(15).reshape(3, 5)
print("\nx is:\n", x)
# means print the first 3 elements of the second row, will return:
# [5,6,7]
print(x[1, 0:3])

# if we want a 1-row matrix, we have to specify also the end of the
# slice, will return [[5,6,7]] (notice the extra brackets)
print(x[1:2, 0:3])

# Numpy allows for advanced indexing. In addition to slices, we can use
# numpy integer arrays and boolean arrays for indexing. Using complex
# indexing is not always straightforward, we will mainly use
# 1-dimensional indices — You can check on the documentation for further
# information on advanced indexing.

# We can provide an index array in place of a slice:
x = numpy.arange(15).reshape(3, 5)
print("\nx is:\n", x)
idx = numpy.array([0, 0, 2])

# y's 1st row will be x's 1st row, y's 2nd row will be x's 1st row, y's
# 3rd row will be x's 3rd row:
y = x[idx, :]
print("\ny = x[idx, :] is:\n", y)

# z's 1st column will be x's 1st column, z's 2nd column will be x's 1st
# column, z's 3rd column will be x's 3rd column
z = x[:, idx]
print("\nz = x[:,idx] is:\n", z)

# Careful when using this! If you can't use it, you something simpler.
# Avoid this. Note: Since idx and jdx are 1-dimensional, x[idx, jdx]
# will keep the elements whose indices are the pairs of values
# (idx[i], jdx[i])
x = numpy.arange(15).reshape(3, 5)
print("\nx is:\n", x)
idx = numpy.array([0, 2])
jdx = numpy.array([1, 3])

# The code below means: print x[0][1] and x[2][3] respectively
print("\nx[idx, jdx] will be:", x[idx, jdx])

# If we want to extract all rows in idx and all columns in jdx, we can
# either use a two-step approach, use the "ix_" function, or reshape the
# index arrays.

# two-step approach: x[idx, :][:, jdx] means take the matrix with rows,
# row 0 and row 2 of x ([0,1,2,3,4],[10,11,12,13,14]), then from this
# make a matrix copying the column 1 and column 3, i.e.:
# [1   3]
# [11 13]
print("\nx[idx, :][:, jdx] is:\n", x[idx, :][:, jdx])

# "ix_" function:
print("\nx[idx, :][:, jdx] with 'ix_' is:\n", x[numpy.ix_(idx, jdx)])

# reshaping:
print("\nWith reshaping, its:\n", x[idx.reshape((2, 1)), jdx.reshape((1, 2))])

# Indexing can also use boolean arrays
x = numpy.arange(15).reshape(3, 5)
print("\nx is:\n", x)
xMask = x > 5
print("\nxMask for x>5 is:\n", xMask)
# The print below, will only shows the the values of x>5, so boolean
# indexing:
print(x[xMask])
z = numpy.array([1, 0, 1], dtype=numpy.bool8)
print("\nboolean array z is:", z)
# will only print the 1st and 3rd rows of x
print("\nx[z] is:\n", x[z])

# Slices and indexing can be also used to assign values to an array
x = numpy.zeros(6)
# will change the value of every other element to starting from index 0
x[::2] = 3
print("\nx is:\n", x)
# the code below means put 0 on the 0th position, 1 on the 2nd position,
# put 2 on the 3rd position and put 3 on the 4th position of array x, so
# we will have: [0, 0, 1, 2, 3, 0]
x[numpy.array([True, False, True, True, True, False],
              dtype=numpy.bool8)] = numpy.arange(4)
print("\nmasked x is:\n", x)

# In general, slicing creates array "views". A view is an array that
# shares its data with a different one. We can also create explicit
# views. Modification to a view modifies the original array! Please note
# that x[:]=0 modifies the elements of the array, x=0 binds name x to
# value 0:
x = numpy.arange(5)
print("\nx is:", x)
y = x[0:3]
print("y is:", y)
y[:] = 10
print("After modifying the view y, x will be:", x)

# Advanced indexing creates copies of an array. We can also explicitly
# create a copy using the method copy, or creating a new array through
# numpy.array. If in doubt, we can check whether an array owns its data:
x = numpy.arange(5)
print("\ndoes x own its data:", x.flags.owndata)
y = x[0:3]
print("\ndoes y own its data:", y.flags.owndata)

# An important feature of numpy array is "broadcasting". Broadcasting
# allows applying elementwise operations, such as addition and
# multiplication, to arrays with different shapes. Whenever arrays have
# different shapes:
#   1’s will be prepended (added to the beginning) to the shapes of
#   smaller arrays until all arrays have the same number of dimensions.
#
#   Axes with shape 1 are treated as if they had the same dimension as
#   the array with largest size along the axis, and all elements were
#   the same along the axis.
# Of course, numpy arrays should have the same dimensions after
# broadcasting. Broadcasting examples: adding the same values to each
# row of a 2-D array:
x = numpy.zeros((3, 4))  # x is a (3x4) matrix
print("\nx is:\n", x)
m = numpy.arange(4)
print("\nm is:\n", m)
# in normal cases x+m wouldn't make sense, but numpy allows us to do it,
# in this case array m is broadcasted to a shape (1, 4), and then
# replicated along axis 0:
print("\nresult of x+m is:\n", x+m)

# Array n already has the same number of dimensions as x, and gets
# replicated along axis 0
n = numpy.arange(4).reshape((1, 4))  # n is a (1x4) row matrix
print("\nn is:\n", n)
print("\nresult of x+n is:\n", x+n)

# Note that, in this case below, o has to be a column vector. Array o
# already has the same number of dimensions as x, and gets replicated
# along axis 1
o = numpy.arange(3).reshape((3, 1))  # o is a (3x1) column matrix
print("\no is:\n", o)
print("\nresult of x+o is:\n", x+o)

# Broadcasting is widely used, so get familiar with it. This topic is
# open to errors, so learn it well. Always check if you're using the
# correct sizes and shapes.

# Numpy arrays can be concatenated. We can use "hstack" and "vstack" to
# stack vectors horizontally or vertically. For 2-D arrays:
x1 = numpy.array([1, 2, 3])
x2 = numpy.array([4, 5, 6])
print("\nx1 is:", x1)
print("x2 is:", x2)
hx12 = numpy.hstack([x1, x2])
vx12 = numpy.vstack([x1, x2])
print("Horizontally stacked array is:", hx12)
print("Vertically stacked array is:\n", vx12)

# hstack and vstack can be used for N-dimensional arrays. hstack
# concatenates arrays along axis 1. vstack concatenates arrays along
# axis 0. We can also use the function "concatenate" — we need to
# specify the axis
#   numpy.hstack(l) is equivalent to numpy.concatenate(l, axis = 1)
#   numpy.vstack(l) is equivalent to numpy.concatenate(l, axis = 0)

# Numpy also provides several linear algebra functions. These can be
# found inside "numpy.linalg". For example, we can compute the
# eigenvalue decomposition of a 2-D array:
x = numpy.arange(9).reshape(3, 3)
print("\nThe square matrix x is:\n", x)
print("Eigenvalue decomposition of x is:\n", numpy.linalg.eig(x))

# We will discuss the different functionalities as needed
