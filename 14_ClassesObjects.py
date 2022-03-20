# Python classes and objects allow writing code in an object-oriented
# way. To define a class, we use the "class" keyword, followed by a
# block of statements. These statements are executed in a "local
# namespace" associated to the class. Note: classes are themselves
# objects. We can access class attributes with the dot "." operator
from script import AClass as DClass
from script import AClass as CClass
from script import AClass as BClass


class AClass:
    x = 3

    def f(self):
        print("Hello World")


if __name__ == "__main__":
    print(AClass.x)  # "3"
    print(AClass.f)  # "<function AClass.f at 0x00000231A62C2050>" etc.

# Class instances (called objects) can be created by “calling” the class
# object. We'll use: "from script import AClass as BClass". We don't
# have to use the "as BClass" part, but we had already defined a class
# names AClass, so we won't want them to clash. Then:
obj = BClass()
print(obj.x)  # "3"
print(obj.f)  # "... <function AClass.f at 0x00000231A62C2050>" etc.
obj.f()       # "Hello World"

# The instantiated object allows for attribute look-up. Attributes can
# be either "data" attributes (similar to variables, like "x=3" in our
# example) or "methods" (like def "f(self): print("Hello World")" in our
# example). Similar to variables, data attributes are not declared, but
# are created on assignment.
obj = CClass()
obj.z = 1
print("obj.z is", obj.z)
obj = DClass()
obj.f()        # Will print "Hello World"
DClass.f(obj)  # Will print "Hello World"

# When a class is instantiated, its special method __init__ is invoked
# (if not present, it’s inherited from the built-in ’object’ class). We
# can use the method to initialize the object attributes:


class Point:
    name = "2D Point"

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Note: x and y are "object" attributes that are created on the new
# object when it’s instantiated. Class attributes (e.g. name) are
# "shared" by all instances. Class attributes are used in place of
# object attributes whenever a given attribute is not found on an
# object:


class A:
    x = 3

    def __init__(self, y):
        self.y = y


a = A(1)
print(a.x)  # Will print 3

# Note: Class attributes are shared among all instances of the class,
# but can be masked by object attributes. In the example below, a.x = 4
# creates a "new" attribute called x on the object a. (My further
# explanation: "so the object attribute of a (a.x) overrides the class
# attribute of B (B.x). If we than change the attribute of B again
# (B.x=5), a.x won't be affected, because as we've said before, a.x=4
# created a 'new' attribute.")


class B:
    x = 3


a = B()
b = B()
print(a.x, b.x)
a.x = 4
print(a.x, b.x)
B.x = 5
print(a.x, b.x)

# However in the example below, doing "c.z.append(4)", not only modifies
# c.z, but also modifies d.z too. This is because, in this case c.z is
# not "assigned", but is "accessed". Since c has no attribute z, class C
# is searched, and its z attribute is used. We then call a method of the
# object "C.z". Its modifications are visible to all objects that do not
# specify a local attribute z.


class C:
    z = [3]


c = C()
d = C()
print(c.z, d.z)
c.z.append(4)
print(c.z, d.z)

# Python classes can define "special" (or "magic") methods. These
# methods, whose names start and end with a double underscore, allow
# defining how the object should behave in particular cases, such as
# when it appears in an expression. For example, the method "__add__"
# allows defining how to compute the result of a sum ("+") of two
# objects.


class PointClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PointClass(self.x+other.x, self.y+other.y)


p1 = PointClass(1, 2)
p2 = PointClass(5, 5)
p3 = p1+p2
print(p3.x, p3.y)

# Other methods allow "overriding" different operators (arithmetic,
# logical, slicing, getting and setting items, ...). For example, the
# "__str__" method defines how an object is converted to a string:


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point( % .2f, % .2f)" % (self.x, self.y)


p = Point2(1, 2)
print(p)

# Python allows a class to inherit from a different one. The syntax
# requires specifying a comma-separated sequence of base classes:
# class DerivedClass(Base1, Base2, Base3):
#   <statements>
# Attribute look-up becomes more complex. For this course, we will
# mainly use classes and objects to simulate C-style structures, i.e. as
# containers of data. If you’re interested, you can learn more on Python
# objected oriented programming on the Python tutorial and on the Python
# documentation.
