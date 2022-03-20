# Python allows handling errors at execution time (exceptions). However
# we won't be using them much, so need to worry if you do not know them.
# In the following example, we try to sum a string with an integer,
# which is something we aren't allowed to do. It will create an
# exception, so it will assign 4 to y.
try:
    y = "a"+3
except:
    y = 4
print(y)

# We can specify which exception should be handled by each "except"
# block. Our example of str + int is a TypeError, we expect to see y=5.
try:
    y = "a"+3
except ValueError:
    y = 4
except TypeError:
    y = 5
print(y)

# We can specify code to be executed regardless of whether the "try"
# block incurs (causes) in an exception, with "finally":
try:
    y = "a"+3
except:
    pass
finally:
    y = 3
print(y)
try:
    y = 2
except:
    pass
finally:
    y = 3
print(y)

# Here's a little bit more detailed expection handling example:
try:
    num = int(input("Please enter an integer number for the numerator:"))
    den = int(input("Please enter an integer number for the denominator:"))
    res_div = num/den
    print("Numerator (%d) / denominator (%d) is %d." % (num, den, res_div))
    print("This program has been executed succesfully!")
except ZeroDivisionError:
    print("This program has encountered an error!")
    print("The denominator can't be 0. Please try a different integer number.")
except ValueError:
    print("This program has encountered an error!")
    print("Some non-integer value has been entered.",
          "Please enter numbers that are integers.")
except TypeError:
    pass
finally:
    print("...The program will exit now...")

# We can raise an exception through the "raise" keyword:
# "raise TypeError" will raise a TypeError, and "raise ValueError" will
# raise a ValueError.
