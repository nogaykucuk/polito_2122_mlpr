# Sets are unordered collections of items without duplicates. Sets are
# usually employed for testing membership and removing duplicate entries
# from a collection. Python allows creating sets using a specific
# notation or the built-in class "set", which receives an iterable
# object:
a = {1, 2, 3}      # We can define a set with {...}
print("Set a is", a)
b = set([1, 2, 3])  # We can also define by passing a list with "set"
print("Set b is", b)
c = set((1, 2, 3))  # We can also define by passing a tuple with "set"
print("Set c is",  c)

# Note: The object {} is NOT the empty set. It's the empty "dictionary".
# To create an empty set, use "set()".
d = set()
print("Set d is", d)

# To test set membership, we can use the operator "in":
a = {1, 2, 3}
print(1 in a)  # True
print('1' in a)  # False
print("1" in a)  # False
print(2 in a)  # True
print(3 in a)  # True
print(4 in a)  # False

# The "in" operator can be used also for lists and tuples, but the
# lookup is much slower. The lookup table is used for retrieving values
# from a database. With lookup tables, we extract data from a database
# so as to reduce the computations. Retrieving a value from a lookup
# table is a faster process compared to simple input-output operations.
# In Python, we use dictionaries to perform a lookup table, and a set is
# like a dictionary with keys but no values, and they're both
# implemented using a hash table. So we can use "in" in sets, and it is
# faster than lists and tuples.
b = [1, 2, 3]
print(1 in b)  # "in" used with list
c = (1, 2, 3)
print(1 in c)  # "in" used with tuple

# Python sets implement standart set operations
# (union,intersection,...):
a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
d = a.union(b)
print("a is", a)
print("b is", b)
print("a intersect b is", c)
print("a union b is", d)

# As with lists, we have "set comprehensions" as well. For set2 below,
# please recall that we have said that "sets are items without
# duplicates". So the set2 won't be {0, 0, 1, 1, 2, 2, 3, 3, 4, 4}, but
# instead it will be {0, 1, 2, 3, 4}
set1 = {i/2 for i in range(10)}
print("set1 is", set1)
set2 = {i//2 for i in range(10)}
print("set2 is", set2)

# Python includes a built-in "dictionary" (dict) type, which we will use
# a lot. Dictionaries are objects that allow associating "keys" to
# "values". Think of dicts as sets of pairs "key:value", where keys are
# unique. Keys are required to be immutable (and hashable). We can
# define dictionaries explicity from "key:value" pairs:
a = {"A": 1, "B": 2, "C": 3}
print("The dictionary a is", a)

# We can look-up values in dict:
print("The value of the key 'A' is", a["A"])

# As we have said before, the empty dict is defined as {}. We can assign
# values to keys (overwriting if the key was present):
b = {}
b['A'] = 1
b['B'] = 2
print("The dictionary b is", b)
b["A"] = 3
print("The modified dictionary b is", b)

# The dictionaries can be iterated, the iteration runs over dictionary
# keys. No guarantees on the order in which keys are visited (this was
# recently changed in Python 3.7) - sort the keys (built-in function
# "sorted" or use an "OrderedDict" from the "collection" module:
# "from collections import OrderedDict").
c = {"A": 1, "B": 2, "C": 3}
print(list(c))  # I don't get the list ["A","C","B"] as stated on slides
print([a[i] for i in sorted(a)])

# The collection of keys can be recovered also using the ".keys" method.
# The collection of values can be recovered using the ".values" method.
# Elements can be removed using the "del" keyword:
a = {"A": 1, "B": 2, "C": 3}
print("Dict a is", a)
print("Keys of dict a is", a.keys())
print("Values of dict a is", a.values())
print("Keys of dict a is (in list)", list(a.keys()))
print("Values of dict a is (in list)", list(a.values()))
del a["A"]
print("After deletion a is", a)

# Keyword "del" can also be used to remove elements from lists, or to
# delete variables. Dictionaries can be created using "dict
# comprehensions":
print({i: i**2 for i in range(5)})

# The "dict" construct allows creating dictionaries from sequences of
# key-value pairs
print(dict([("A", 1), ("B", 2)]))

# We can even do something like:
l1 = ["A", "B"]
l2 = (1, 2)
d = dict(zip(l1, list(l2)))
print("Our dictionary will be:", d)
