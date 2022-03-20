# Files can be accessed using the function "open":
# f = open(’filename’, ’r’)
# The first argument is the filename. The second argument is the mode.
# Text modes are similar to C: ’r’, ’w’, ’a’, ’r+’. Binary encoding is
# represented by ’b’ appended to the mode. In this case, I/O operations
# do not return strings, but byte sequences (we won’t use explicitly the
# binary encoding)
f = open("helloWorld.txt", "r")
f.close()

# To avoid data loss on writing, files should be always closed when I/O
# is finished. We can let the file object handle this automatically
# using the "with" keyword:
# with open(’filename’, ’r’) as f:
#   ... do something with f here ...
# The "with" statement takes care of closing the file when the block is
# finished (this is done automatically by calling some methods of the
# file object when the "with" statement starts and ends). To read an
# entire file, we can use the method read(size) size is an optional
# parameter specifying the maximum number of characters or bytes to
# read:
f = open("helloWorld.txt")
print(f.read())
f.close()

# We can read a file line by line using the "readline" method. An empty
# string denotes that the end of file has been reached:
f = open("helloWorld.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# A file object can be iterated, and can thus be used in a for loop. The
# file is read line by line (remember, lines can end with ’\n’). In the
# example below, we will be using the ".rstrip()" method, which returns
# a copy of the string with trailing whitespace removed.
f = open("helloWorld.txt", "r")
for line in f:
    print(line.rstrip())
f.close()

# To write a file, we can use the method "write":
# f = open("helloWorld.txt", "w")
# f.write("Hello")
# f.close()
# However, the operation above will overwrite to whole file, which we
# don't want to do at the moment. We can also use print, providing an
# argument for parameter file:
# f = open("helloWorld.txt", "w")
# print("Hello", file=f)
# f.close()
# However, the operation above will, again, overwrite to whole file, so
# we commented out this part for the moment. Also please note that,
# print adds a newline at the end of the string, unless we pass end=''
