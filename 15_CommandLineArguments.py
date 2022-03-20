# Command line arguments can be accessed from the attribute "argv" of
# module "sys". "argv" is a list of strings, each element corresponds to
# one argument. For example, if we type:
# "python 15_CommandLineArguments.py 1 aaa 42" in terminal we will get
# the result:
# The number of arguments (including the file name is:) 4
# 15_CommandLineArguments.py
# 1
# aaa
# 42
import sys
print("The number of arguments (including the file name is:)", len(sys.argv))
for arg in sys.argv:
    print(arg)
