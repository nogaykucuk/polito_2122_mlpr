# Complex data can be "serialized" (i.e. transformed to a string that
# can be written to a file) in different ways: "json" and "pickle"
# Using "json" (more portable, less powerful):
import pickle
import json
l = [1, ("Hello", "World"), 3]
f = open("out", "w")
json.dump(l, f)
f.close()
f = open("out", "r")
print(json.load(f))    # It will print [1, ["Hello", "World"], 3]
f.close()

# Using Python "pickle" (less portable, supports more complex data):
l = [1, ("Hello", "World"), 3]
f = open("out", "wb")  # Binary mode
pickle.dump(l, f)
f.close()
f = open("out", "rb")
print(pickle.load(f))  # It will print [1, ('Hello', 'World'), 3]
f.close()
