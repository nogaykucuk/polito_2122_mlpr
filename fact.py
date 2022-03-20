# This is a small code that finds the factorial of a given number. We've
# created this Python file mainly to use it as an example for
# "09.Modules.py".
def fact_func(n):
    if n == 0:
        return 1
    return n * fact_func(n-1)
