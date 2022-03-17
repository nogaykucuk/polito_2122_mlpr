# This is my first python code since 2014! Let's try to print out "Hello
# World". Please also try to run the .py file from the terminal with:
# "> python helloWorld.py" and this will execute the script. From the
# shell you can just call the interpreter with "> python". This would
# allow the interpreter to open an interactive session (shell), where we
# can can write python instructions, which will be interpreted one by
# one, than executed. You can close this interactive session
# (in Windows) by pressing Ctrl+Z, then pressing Enter.


print("Hello World!")
print(3 ** 4)

# The “official” style guide for Python is PEP 8 (Python Enhancement
# Proposal), and I will try to follow this convention. It can be found
# here in details: https://www.python.org/dev/peps/pep-0008/
# I will try to follow these conventions. PEP 8 states to "limit all
# lines to a maximum of 79 characters.For flowing long blocks of text
# with fewer structural restrictions (docstrings or comments), the line
# length should be limited to 72 characters." Also, again according to
# PEP 8:
# joined_lower for functions, methods, attributes, variables
# joined_lower or ALL_CAPS for constants
# StudlyCaps for classes
# camelCase only to conform to pre-existing conventions must be
# followed. For breaking a line, implicit continuation is preferred,
# explicit backslash is to be used only if necessary:
# a = ('1' + '2' + '3' +
#      '4' + '5') is preferred, instead of:
# a = '1' + '2' + '3' + \
#     '4' + '5'
# For breaking in a print statement: An elegant solution would be to use
# two lines of code but only using the print() function once:
# print('Hello how are you',
#       'today?')
# We can just leave the print-parenthesis open and indent nicely, as PEP
# states: "using Python's implicit line joining inside parentheses,
# brackets and braces".

PI = 3.14
cd_radius = 6
list_types = [1, "A", 2.4, 3+4j]
my_areas = [1007.211834]
print("The list that the area of an American dime is:", my_areas)


def circle_area(r):
    return PI*r*r


cd_area = circle_area(cd_radius)
my_areas.append(cd_area)
print("The list that contains the areas of circular shapes that I've",
      "found is the following:", my_areas)


class MyCoinClass:
    def __init__(self, type, radius, year, condition):
        self.type = type
        self.radius = radius
        self.year = year
        self.condition = condition

# Python is a high-level language (HLL), meaning it is a programming
# language with strong abstraction from the details of the computer. A
# high-level language is any programming language that enables
# development of a program in a much more user-friendly programming
# context and has a higher level of abstraction from the computer, and
# focuses more on the programming logic rather than the underlying
# hardware components such as memory addressing and register
# utilization. High-level source code contains easy-to-read syntax that
# is later converted into a low-level language, which can be recognized
# and run by a specific CPU.

# Python is an interpreted language, meaning it is a programming
# language which is interpreted, without compiling a program into
# machine instructions. It is one where the instructions are not
# directly executed by the target machine, but instead read and executed
# by some other program. There is only one step to get from source code
# to execution. While in this language, interpreted programs can be
# modified while the program is running. Interpreters run through a
# program line by line and execute each command. In this languages, all
# the debugging occurs at run-time. Interpreted languages tend to be
# more flexible, and often offer features like dynamic typing and
# smaller program size. Also, because interpreters execute the source
# program code themselves, the code itself is platform independent.
# The most notable disadvantage of interpreted languages is the typical
# execution speed compared to compiled languages. These languages
# deliver relatively slower performance. But, with the development of
# "just-in-time" compilation, that gap is shrinking.

# Python can follow multiple programming paradigms: "Functional",
# "Procedural" or "Object-Oriented".

# Functional programming is a programming paradigm where programs are
# constructed by applying and composing functions. It is a "declarative
# programming paradigm" in which function definitions are trees of
# expressions that map values to other values, rather than a sequence of
# imperative statements which update the running state of the program.
# In functional programming, functions are treated as first-class
# citizens, meaning that they can be bound to names (including local
# identifiers), passed as arguments, and returned from other functions,
# just as any other data type can. This allows programs to be written in
# a declarative and composable style, where small functions are combined
# in a modular manner. Functional programming has its roots in academia,
# evolving from the "lambda calculus", a formal system of computation
# based only on functions. Functional programming has historically been
# less popular than imperative programming, but many functional
# languages are seeing use today in industry and education, including
# Common Lisp, Clojure, Erlang. Functional programming is also key to
# some languages that have found success in specific domains, like
# JavaScript in the Web, R in statistics, J, K and Q in financial
# analysis, and XQuery/XSLT for XML. In addition, many other programming
# languages support programming in a functional style or have
# implemented features from functional programming, such as C++11, C#,
# PHP, Python, Go, Java (since Java 8).


# Procedural Programming is a programming paradigm, derived from
# "imperative programming", based on the concept of the "procedure
# call". Procedures (a type of routine or subroutine) simply contain a
# series of computational steps to be carried out. Any given procedure
# might be called at any point during a program's execution, including
# by other procedures or itself. C is an example of a procedural
# programming language. This paradigm uses a linear top-down approach
# and treats data and procedures as two different entities. It follows
# the "declarative programming model". The focus in Procedural
# Programming is on "What You are Doing".

# Object-oriented programming (OOP) is a programming paradigm based on
# the concept of "objects", which can contain data and code: data in the
# form of fields (often known as attributes or properties), and code,
# in the form of procedures (often known as methods). A feature of
# objects is that an object's own procedures can access and often modify
# the data fields of itself (objects have a notion of this or self).
# In OOP, computer programs are designed by making them out of objects
# that interact with one another. OOP languages are diverse, but the
# most popular ones are class-based, meaning that objects are instances
# of classes, which also determine their types. Many of the most widely
# used programming languages (such as C++, Java, Python, etc.) are
# multi-paradigm and they support object-oriented programming to a
# greater or lesser degree, typically in combination with imperative,
# procedural programming. However it usually follows the imperative
# programming model. The focus in Object-Oriented Programming is on
# "How You are Doing It".
