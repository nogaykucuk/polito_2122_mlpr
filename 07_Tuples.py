# Besides lists, Python supports another sequence type: "tuples". A
# tuple is a sequence of values separated by commas.

l = [1, 2, 3, 'A']
t = 1, 2, 3, 'A'
print("The list l is:", l)
print("The tuple t is:", t)

# Although in some case it’s not necessary, to ensure the proper
# operation order, it’s better to enclose the values in parentheses:
t = (1, 2, 3, 'A')
print("Tuple written in paranthesis:", t)
tup = (1, 2, (1, 2))
print("3rd element of the tuple is", tup[2])

# Tuples are immutable (their values cannot be changed), but can be
# sliced, indexed and iterated in the same way as lists. So in a way,
# they are the "list versions of strings", since strings are also
# immutable. The empty tuple is represented by a set of empty brackets
# (). Pay attention: x = 1 is different from x = 1,. To write a tuple,
# containing a single value you have to include a comma, even though
# there is only one value. So while x=1 creates an integer variable x,
# x=1, will create a tuple variable x!
x = 1
print("x=1 will create the integer variable x:", x)
x = 1,
print("x=1, will create the tuple variable x:", x)

# Python allows also for "tuple unpacking" — the elements of a tuple can
# be assigned to a sequence of variables directly.
x, y, z = (1, 2, 3)
print("x, y, z are", x, y, z, "respectively.")

# We can also use these unpacking as follows:
colors = ("Red", "Green", "Blue")
col1, col2, col3 = colors
print("col1, col2, col3 are", col1, col2, col3, "respectively.")

# Tuples packing and unpacking is useful, for example, to return more
# than a single value from a function:


def f():
    return 1, 2


a, b = f()
print("a and b are", a, "and", b, "respectively.")

# Another interesting use case is iteration of tuples of values. For
# example, down below we have a list that has tuples as elements. We can
# iterate this list in the following way:
l = [(1, "a"), (2, "b"), (3, "c")]
for val, name in l:
    print(val, name)

# The "zip" function can be used to create tuples of values from a set
# of lists (zip actually returns an iterator, i.e. an object that we can
# iterate to get values from, but can be iterated only once —we use the
# list function to create a real list in the example). We will use this
# "zip" when we work with datasets.
l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
l = list(zip(l1, l2))
print("l is", l)

# Even though we haven't seen the string interpolation, we can do the
# following example (for more information check: "02_BasicDataTypes"
# lines 117 - 128):
for indx, name in zip(l1, l2):
    print("The %d element has the value: %s." % (indx, name))

# In the example above, if the lengths of the lists don't match nothing
# changes, it will still make 3 tuple elements for the list
l3 = [1, 2, 3, 4]
l4 = ["a", "b", "c"]
lst1 = list(zip(l3, l4))
print("lst1 is", lst1)
l5 = [1, 2, 3]
l6 = ["a", "b", "c", "d"]
lst2 = list(zip(l5, l6))
print("lst2 is", lst2)

# Since "zip" is an iterator, we can also do:
course_id = [101, 102, 103, 104]
course_name = ["ENG", "HIST", "MATH", "PHYS"]
for val, name in zip(course_id, course_name):
    print(val, name)

# The function "enumerate" returns an iterator that provides pairs of
# (index, value) from a given iterable:
l2 = ["a", "b", "c"]
for val, name in enumerate(l2):
    print(val, name)
# See the similarities between "zip" and "enumerate". When used with a
# "for" iteration "zip" allows us to join to lists in to a tuple, while
# "enumerate" is used when we have one list, and enumerate iterates the
# first elements for the tuple and joins them. Please also note that,
# iterators like those returned by "zip", "range" and "enumerate" are
# consumed once they are used. If we need to iterate the result multiple
# times use "list" to convert the result to a list.
course_id = [101, 102, 103, 104]
course_name = ["ENG", "HIST", "MATH", "PHYS"]
course_programme = list(zip(course_id, course_name))
print(course_programme)
