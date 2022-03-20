# We have seen the concept of namespaces when discussing modules and
# nested functions. In Python, a "namespace" is a mapping from names
# (variables, functions, ...) to objects. Examples of namespace include:
# The set of built-in names ( sum , print , ...)
# The global variables of a module
# The local variables of a function
# Names in different namespace are independent. Scopes define which
# names can be directly accessed. Scopes are searched in the following
# order:
# Innermost scope, containing the local names
# Scopes of enclosing functions (starting from the innermost)
# The current module, containing the module global names
# The outermost scope, containing the built-in names
# We can access names in a different namespace through the dot "."
# operator. We have already seen this when accessing methods of built-in
# types, or variables in a module. In general, we refer to the element
# after the dot as an attribute of the object on the left. Attributes
# can be read-only or writable:
import mod
mod.b = 8
print(mod.b)
