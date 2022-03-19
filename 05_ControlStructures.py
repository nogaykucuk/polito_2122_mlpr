# Conditional execution with: "if", "elif", "else"
x = 3
print("x is", x)
if x < 0:
    print("x is a negative number.")
elif x == 0:
    print("x is zero.")
else:
    print("x is a positive number.")

# Python does not have explicit delimiters for blocks of code. Block are
# represented through "indentation". Be careful!

# The following code will produce the output 3
x = 3
if x < 0:
    x = x+1
    x = x*2
print(x)

# The following code will produce the output 6
if x < 0:
    x = x+1
x = x*2
print(x)

# The condition should be a Boolean (type bool) value. "True" and
# "False" are built-in values (type bool). Comparison operators return
# bool values: ==,<,>,<=,>=,!= Any object can be converted to bool (for
# control flow statements the conversion is automatic). Almost
# everything is converted to "True", except:
# The Boolean value "False"
# The numerical values 0, 0.0
# Empty collections (e.g. empty lists [] or empty strings '')
# The special value "None" (for example print() returns this None value)
# Note: Explicit casting can be achieved invoking bool() over the value.
# The same applies for other types, such as int() or float(). Logical
# operators can be used to form more complex logical expressions: "and",
# "or", "not"
if((2 == 3) or (1 < 3)):
    print(True)
print(not True)

# Boolean operators may be applied to both Boolean and non-boolean
# values (and may return non boolean values). The semantic is:
# not x:   evulate x and yield True if x is false, False otherwise
# x and y: evaluate x; if x is false return its value, else evaluate y
#          and return its value
# x or y:  evaluate x; if x is true return its value, else evaluate y
#          and return its value
# This allows conditional evaluation of y (similar to C).
# Multiple "elif" conditions can be included, they act as compact way to
# express else-if statements and avoid excessive code nesting.
x = 3
print("x=", x)
if x < 3:
    y = 4
else:
    if x > 10:
        y = 5
    else:
        y = 2
print("y=", y)

# So instead of coding like the previous example, we can do:
x = 3
print("x=", x)
if x < 3:
    y = 4
elif x > 10:
    y = 5
else:
    y = 2
print("y=", y)

# The "else" block can be omitted. Blocks cannot be empty - the "pass"
# instruction can be used to do nothing
if x < 3:
    y = 4
print("y=", y)

if x < 3:
    y = 4
else:
    pass
print("y=", y)

# Python allows for conditional expressions, similar to C construct:
# cond ? exp1 : exp2
# In Python the syntax is:
#exp1 if cond else exp2
a = True
x = 1 if a else 2
print("x=", x)
y = 1 if not a else 2
print("y=", y)

# Loops:"while" and "for". The "while" construct behaves like in C,
# repeating a block of code as along as the condition is true.
x = 3
while x < 6:
    print(x)
    x += 1

# The "for" construct behaves differently, it allows iterating over the
# elements of a sequence (e.g. string, list, etc.), following the order
# that they have in the sequence:
for x in [1, 2, 3, 'hello']:
    print(x)

# To avoid unintended behavior, it is better to avoid modifying the
# sequence while iterating. So instead of this:
# l=[1,2,3]
# for x in l:
#   l.append(1)
# ... Here we would actually get an infinite loop, because we are adding
#     one more element with each iteration to the list l.
# Do this (so we create a copy of this list [1,2,3] -so a new list- and
# then we iterate over the copy, and then each time we modify the
# original list, but the copy "list(l)" does not get modified):
l = [1, 2, 3]
for x in list(l):
    l.append(1)
print("The modified original list l", l)

# The "range" function can be used to generate a sequence of numbers on
# the fly (note: range does not create a list, but rather an iterator
# object that can be iterated)
for x in range(3):
    print(x)

# Or:
new_list = list(range(5))
print("The new list is", new_list)

# The range function allows defining also an initial value and a step
# (both are optional; if two values are passed, they are assumed to be
# first and ending element of the range - remember that the ending is
# always excluded)
for x in range(1, 6, 2):
    print(x)
print(list(range(1, 6)))

# "break" and "continue" statements can be used to exit from the
# innermost cycle or to skip to the next iteration. The semantic is the
# same as in C.
for x in range(10):
    print(x)
    if x >= 3:
        break
for x in range(10):
    if x >= 3 and x <= 8:
        continue
    print(x)

# Loop statements allow for an "else" clause as well. We won't use it,
# however if you're interested you can check the Python documentation.
