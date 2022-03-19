# Python natively supports several data types. For example Numerical
# types such as int, float,etc. Please also notice that we are not
# defining any variable types explicity like "int a, float c" etc. like
# how we do in C. This is because in Python, variables do not have
# types, instead values always have a type.
a = 2
b = 6
c = 7.48
d = 3+4j
print("a is: ", a)
print("Type of a is: ", type(a))
print("b is: ", b)
print("Type of b is: ", type(b))
print("c is: ", c)
print("Type of c is: ", type(c))
print("d is: ", d)
print("Type of d is: ", type(d))
print("a times b is: ", a * b)
print("a times c is: ", a * c)

# We can also do another operation, which is different from C, and that
# is computing powers with the ** operator.
print("a to the power b is: ", a**b)

# Division with / always result in float, while integer division is
# obtained through //
d = 4
print("d is: ", d)
print("(Float) division of b over d is: ", b / d)
print("(Integer) division of b over d is: ", b // d)

# There is also the remainder operator, and it works like how it is in C
print("Remainder of b over d is: ", b % d)

# There is also the the String data type in Python. We can use both
# '...' or "..." for enclosing the strings. There is no difference.
print("Hello World!")
print("Hello World!")

# String are immutable(cannot be modified), but new strings can be
# obtained from the existing ones
print("This " + "is " + "a string.")

# Single quotes are allowed as characters in double-quoted strings, and
# vice-versa.
print("'Hello' World!")
print('"Hello" World')

# \ allows escaping quotes
print('This a " in string where the string is enclosed in double-quotes in',
      'the print().')
# Strings can be indexed (indexes start from 0 as in C language). Please
# note though: In C, an element of a string is of type char. In Python,
# indexing a string works differently - s[0] is still a string.
str = "Hello"
print("String str is: ", str)
print("First element of str is: ", str[0])
print("Second element of str is: ", str[1])
print("Type of str is: ", type(str))

# Negative indices can be used to index from the end, but -0 is equal to
# 0 again, so it is the index of the first element.
print("First element of str is: ", str[-0])
print("First element of str from the end is: ", str[-1])
print("Second element of str from the end is: ", str[-2])

# As we've said before strings are immutable, so we cannot assign a
# value to an element of a string (like it is an element of an array).
# So trying to run the  code below will result an error with the message
# "Exception has occurred: TypeError 'str' object does not support item
# assignment":
# ...
# str[0]="Y";
# print(str);
# ...

# The built-in operator "len" allows computing the lenght of of a string
print("Length of the string str", str, "is:", len(str))

# Strings can be sliced, but be aware that the last element (i.e. the
# ending point) is always excluded. In MATLAB this is not the case, it
# is included. However here, it is not!
print("The first 3 letters of str is: ", str[0:3])
print("The first 5 letters of str is: ", str[0:5])

# The first and/or last elements can be omitted, and are implicitly
# assumed to be written.
print("The first 3 letters of str is: ", str[:3])
print("The last 3 letters of str is: ", str[2:5])
print("The last 3 letters of str is: ", str[2:])

# Negative indices can also be used in slices
print("str[-3:-1] is: ", str[-3:-1])

# We may ask to ourselves why the last element is omitted. This might be
# related to the ease of readability of the code. First of all it is
# easy to find the length of the slice this way. For example let's say
# we do: str[0:3]; 3-0=3, the length of the "hel" will be 3. Also
# consecutive slices can be represented as, for example: str[0:2] and
# str[2:5] and we can see that it is easy to read the meaning of this:
# first two element "he" and start from the third letter to for 3
# elements, "llo". Also accessing a slice of length n can be found by:
# s[i:i+n]. For example, slice with 2 elements, starting from the fourth
# letter can be found as: i=3, n=2, then: s[3:3+2]=s[3:5]="lo".

# The slicing operator allows also providing a "step value".
print("For the string", str, "Let's try str[0:5:2]", str[0:5:2])

# Slice start and end can be omitted (implicitly assumed to be the
# beginning and end of the iterable)
print("For the list", str, "str[::2] will print", str[::2])

# The step can be negative -useful to traverse the iterable in reverse.
print("str[::-1] will print the list in reverse: ", str[::-1])

# Pay attention when providing start or end with negative steps
print("str[0:5:-1] will print nothing: ", str[0:5:-1])
print("str[5:0:-1] will not print the first element, i.e. H:", str[5:0:-1])

# If we want to slice and reverse, better to do both steps separately
print("str[0:3][::-1] means take the first 3 elements of the list, and then",
      "reverse them: ", str[0:3][::-1])

# Python supports C-style string interpolation. String interpolation (or
# variable interpolation, variable substitution, or variable expansion)
# is the process of evaluating a string literal containing one or more
# placeholders, yielding a result in which the placeholders are replaced
# with their corresponding values. The placeholder may be a variable
# name, or in some languages an arbitrary expression, in either case
# evaluated in the current context. The syntax is: "string" % values,
# where values is either a single value or a tuple of values. Format
# specifiers are similar to those of C "printf", like %d for integers
# etc. Python supports more advanced string formatting, you can refer to
# the tutorial.
print("%d is %s than %d." % (2, "lower", 3))

# Some other useful string methods (they return new strings, check the
# documentation for the explanations of their parameters):
# lower, upper:          convert a string to lower or upper case
# lstrip, rstrip, strip: remove leading/trailing/both whitespaces from a
#                        string
# replace:               replace occurencies of text
# split:                 returns a list of words of a given string,
#                        separated using a second string as delimiter
