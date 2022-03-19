# Python allows defining functions with the "def" keyword, followed by
# the function name and the list of formal parameters in (paranthesis).
# A "return" statement is used to make the function return a value.
# Functions with no return statement still return a default value when
# they reach the end of the function block. The value returned is the
# special value "None". Similar to "Null" in C.
def f(x):
    return x+1


print(f(2))


def f2(y):
    return


print(f2(2))


def f3(z):
    print(z)


print("Above this line we'll see 2 and this line will print 'None': ", f3(2))

# When a function is executed, a local symbol table is created to store
# local variables. Variables that are assigned inside the function are
# stored in the local symbol table. Referenced variables are looked-up
# in the local symbol table, then in the local tables of enclosing
# functions, and finally in the global symbol table. In general, it's
# not possible to directly assing a global variable inside a function
# (there are exceptions, but we will avoid using them to keep things
# simpler). Function arguments are passed by value:
a = 3
print("a is", a)


def f(x):
    x += 1
    print("x is", x)
    return x


f(a)
print("a is still", a)

# However, the value that is copied is the "object reference" (similar
# to passing pointers in C):
l = [2, 3]


def f(x):
    x.append(4)  # So with this method,  we're actually modifying object


print("l is:", l)
f(l)
print("l is now:", l)

# Here we used method "append" to modify the list object whose reference
# is the value of l. Inside the function, x is copy of the list
# reference. However, it refers to the same list. Python functions allow
# for both positional and keyword arguments (arguments with default
# values, e.g. x=4):


def f(x=4):
    print(x)


f()     # It will print 4
f(2)    # It will print 2
f(x=3)  # It will print 3

# Positional arguments must be specified when invoking the function,
# keyword arguments can be omitted (and will use the default value). So
# in the example below, we can't call f(), we have to specify the
# positional argument, always:


def f(a, b=0):
    print(a+b)


f(1)
f(1, b=4)

# However trying to run f() would result the following error: "Exception
# has occurred: TypeError f() missing 1 required positional argument:
# 'a'." When invoking the function, positional arguments may be passed
# via keywords, and optional arguments may be passed as positional
# (following the order in which they are defined). In the example below
# we see that func(1,2) is not the same as func(2,1). So the order of
# positional arguments do matter!


def func(a=2, b=3):
    print(a**b)


func()      # This would work, it will print 8
func(3)     # This also would work, it will print 27
func(2, 1)  # This will print 2
func(1, 2)  # This will print 1

# But we can also pass the arguments in as keyword arguments, then as we
# can see below that the order of the the keyword arguments don't
# matter.
func(a=3, b=4)  # This would print 81
func(b=4, a=3)  # This also would print 81

# Positional arguments must be placed before the keyword ones
func(1, 2)

# func(b=2,1) will result in the following error: "SyntaxError:
# positional argument follows keyword argument". Arguments can be
# restricted to be positional or keyword only - if interested, please
# check the tutorial. Python also allows for arbitrary argument lists
# and arbitrary keyword only argument dictionaries. In the case below,
# the arguments are packed in a "tuple" (more on this later) and passed
# as value for the parameter a:


def f(*a):
    print(a)


f(1, 2, 3)


def f2(*b):
    return b[0]


print("First element of f2 is", f2(1, 2, 3))

# In the case below, the keyword arguments are packed in a "dictionary"
# (more on this later as well) and passed as values for the parameter
# kw. Again, all these are things that are not essential for the course.


def f(**kw):
    print(kw)  # the kw object here will be a dictionary


f(a=1, j=6)


def f(*a, **kw):
    print(kw)


f(a=1, b=2)

# In Python, the functions are objects as well. They can be assigned and
# passed to functions


def fpr(x):
    print(x)


def g(f, a):  # It's essentially def fpr(x): print(x+1);
    f(a+1)


g(fpr, 1)

# Anonymous functions can be created on the fly through the keyword:
# "lambda". The body of the function can only be an expression, and is
# the value returned by the function.
print((lambda x: x+1)(3))  # It will print 4

# ...
# h=lambda y: y+5
# print("h(2) prints:", h(2))
# ...
# This will print 7
# Functions can be defined in nested scopes. The nested function can
# access, but not modify the variables of the enclosing function (unless
# explicitly indicated)


def f(x):
    def g(y):
        return x+y
    print(g(1))


f(3)

# We can do:


def add_two(x):
    return x+2


num = 3
print("This will add 2 to the number", num, ":", add_two(num))


def add_five(x):
    return x+5


num = 42
print("This will add 5 to the number", num, ":", add_five(num))

# This can be useful to create functions with "pre-set" parameters. In
# the example below, we define a generic "add_n" function. So instead of
# writing codes for each function add_2, add_3, add_5 etc., we write a
# generic "add_n" function, that creates add_2, add_3 functions for us.
# When we call "add_n(3)", with n=3 it will go to add_n(3), then it will
# see the def add(x), but it will do nothing for the time being. Then it
# will come to the return statement "return add", so it will enter to
# the function add(x), but since return add didn't have any parameters,
# it will stay as x. Then inside the function it will see the return
# statement: "return x+n" it will return x+3 to the outer function. But
# recall, we were already in a return statement so this will also return
# x+3. In our code we've assigned add_3 to add_n(3), so the return value
# of add_n(3): x+3 will be assigned to add_3. So in fact, we have
# created another function named add_3. We then can use this function to
# add 3 to a given number with: "number=2; add_3(number)", for example.
# With this nested functions scheme we can easily create add_4, add_999
# etc. We will use something like this only once, and there will be an
# alternative that too.


def add_n(n):
    def add(x):
        return x+n
    return add


add_3 = add_n(3)
number = 2
print("When we add 3 to the number", number, "we get:", add_3(number))
