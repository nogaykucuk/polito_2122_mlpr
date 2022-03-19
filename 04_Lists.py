# Python natively supports high-level data types, such as lists, tuples,
# hash tables and sets. A list can be built in Python by:
l = [1, 2, 3]
print("The list l is: ", l)

# List elements can be heterogeneous
l = [1, 'A', 'b', 2, [4, 5]]
print("The updated list l is: ", l)

# The length of a list can be obtained from function len, just as it is
# used for strings. Also note that while strings were immutable, lists
# can be modified.
print("Length of the list l", l, "is", len(l))

# Lists can be indexed and sliced like strings.
print("First element of the list is: ", l[0])
print("l[:5] is:", l[:5])

# Slicing a list returns a new list which contains references to the
# values of the original list (shallow copy, it means that any change
# made to a copy of object do reflect in the original object).

# The slicing operator allows also providing a "step value".
l = [1, 2, 3, 4, 5]
print("For the list", l, "l[0:5:2] will print", l[0:5:2])

# Slice start and end can be omitted (implicitly assumed to be the
# beginning and end of the iterable)
print("For the list", l, "l[::2] will print", l[::2])

# The step can be negative -useful to traverse the iterable in reverse.
print("l[::-1] will print the list in reverse: ", l[::-1])

# Pay attention when providing start or end with negative steps
print("l[0:5:-1] will print nothing: ", l[0:5:-1])
print("l[5:0:-1] will not print the first element, i.e. 1:", l[5:0:-1])

# If we want to slice and reverse, better to do both steps separately
print("l[0:3][::-1] means take the first 3 elements of the list, and then",
      "reverse them: ", l[0:3][::-1])
print("l[5:0:-1] will not print the first element, i.e. 1:", l[5:0:-1],
      "but l[0:][::-1] will print 1 as well:", l[0:][::-1])

# A list can be modified assigning values to its elements (as if it were
# an array)
print("List l is", l)
l[0] = 'A'
print("After modification l is", l)

# Slices can be assigned new values: Assigned values should be iterable
# (e.g. lists). Assignment can both replace and remove values. Assigning
# values to a slice:
l = [1, 2, 3, 4, 5]
l[1:4] = [11, 12, 13]
print("l is", l)

# Removing values ([] i an empty list)
l[1:3] = []
print("l is", l)

# We can append an element to a list using its "append" method (more on
# methods later)
l = [1, 2, 3]
print("l is", l)
l.append(4)
print("Appended list will be", l)

# We can extend a list its "extend" method
l.extend([5, 6])
print("Extended list will be", l)

# We can pop an element using its "pop" method (optional: pass the index
# of the element to pop, otherwise the default elemenent is the last
# one)
l = [1, 2, 3, 4, 5]
print("l is", l)
x = l.pop()
print("After x=l.pop(), l will be", l)
print("After x=l.pop(), x will be", x)
x = l.pop(1)
print("After x=l.pop(1), l will be", l)
print("After x=l.pop(1), x will be", x)

# We can create a list from another iterable object (e.g. another list,
# string, etc.) using lists.
l = list([1, 2, 3])
print("l is ", l)
l = list("Hello")
print("l is ", l)

# We can also sort elements in a list using its "sort" method. The
# default sort will be in ascending order.
l = [4, 3, 2, 5, 22, 1]
print("Pre-sorted list is", l)
l.sort()
print("Sorted list l is", l)

# Python allows for concise syntax to create new lists:
# "list comprehension". This construct allows creating a list by
# applying some operations on the elements of another list or iterable
# object:
l = [i**2 for i in range(4)]
print("List l is:", l)

# We can also do something like:


def f(x):
    return 2*x


l = [f(i) for i in [1, 3, 5, 7, 9]]
print(l)

# Filters can be applied to select only a set of elements
l = [i**2 for i in range(10) if i % 2 == 0]
print("The new l list is:", l)

# No "else" branch should be provided, only elements for which the
# condition is "True" will be selected. Note the difference with
# conditional expressions:
l = [i**2 if i % 2 == 0 else 0 for i in range(10)]
print("The newer l list will be:", l)

# We assing values from lists to different variables in this way:
colors = ["red", "green", "blue"]
col1 = colors[0]
col2 = colors[1]
col3 = colors[2]
print("col1, col2, col3 are", col1, col2, col3, "respectively.")

# But we can do something else. Python also allows for "list unpacking":
# the elements of a list can be assigned to a sequence of variables
# directly
colors = ["red", "green", "blue"]
c1, c2, c3 = colors
print("c1, c2, c3 are", c1, c2, c3, "respectively.")

# We can also do:
fruit1, fruit2, fruit3 = ["apple", "pear", "orange"]
print("fruit1, fruit2, fruit3 are", fruit1, fruit2, fruit3, "respectively.")
