# In Python everything is an object: int,float,str are built-in objects.
# We can "bind" values(objects) to names. A variable is merely a name
# bounded to a value actually. In practice, the variable contains a
# reference (pointer) to the object. Python is a strongly and
# dynamically typed language. It is a strongly typed language, because
# all the values in Python have a type. For example, from the previous
# code, the type of "Hello" is string. It is a dynamically typed
# language, because the values have types always. Dynamically typed also
# means type-checking happens at runtime. Variables do not have types.
# This is another aspect that separates Python from C. Because of this,
# we do not have to specify a variable type, like how we do it in C.
# Variables can be bounded to values with different types.
a = 3
print("a is: ", a)
a = "Hello World!"
print("The new value of a is: ", a)

# No need to declare variables in advance like: "int a, float b etc.".
# However, variables should be assigned to a value before being used.
# Value type determines the operations that can be performed. Python
# allows "duck-typing", i.e. rather than checking the type of a value,
# we check whether it implements specific functionalities
# (i.e. methods). Duck-typing allows us to use polymorphism, but without
# actually having the whole inheritance bit - more on this later.
# However in this course, we won't be using object-orinted programming
# much. So if you know it good, but if you don't know it, you don't need
# to learn it.
