# Python allows using functionalities defined in different files. Each
# file is called a "module", and modules can be "imported" in other
# modules or in an interactive session. Importing a module allows
# accessing functions and variables defined in the file. For this
# example, we will be importing the "10.Factorial.py" file and use the
# function here, "09.Modules.py"
from mod import b
from modNew import b as b_better
import modFinal as lastModule
import modNew
import mod
import fact
result = fact.fact_func(4)
print("4! is equal to", result)

# The "import" statement allows importing a module. Remember that the
# imported file name extension should be .py , but the extension should
# not be specified when importing the module (Notice that we have
# written "fact" instead of "fact.py"). The symbols defined in the
# module are placed in a private symbol table associated to the module,
# and can be accessed through the dot "." operator. When a module is
# imported, it is actually executed (multiple imports are allowed,
# but the module is executed only the first time):
print(mod.b)  # We will also see the "Hello World" message as an output

# Inside a module, its own name is accessible through the variable
# "__name__". The main module (the module we pass to the interpreter at
# launch) has the special name "__main__". These variables can be used
# to execute parts of a script only when it's in the main module, but
# not when it's imported. So when we write "import modNew", it will
# execute the whole module but, we won't see the "Hello World" being
# executed since its not in the main module for "modNew.py". Since we're
# in the main module for "09_Modules.y", "if __name__ = "__main__":"
# will be "True" and it will "print(modNew.b)" here:
if __name__ == "__main__":
    print(modNew.b)

# Assigning a different name to a module when importing: use the "as"
# keyword: For example "import mod as mymodule". Then we can do
# "mymodule.y" for example.
print(lastModule.y)

# We can import module symbols in the current local symbol table:
# from mod import b, for example:
print("b is", b)

# We can also use "as" here too: "from modNew import b as b_better"
print("b_better is", b_better)

# We can import all module symbols in the local symbol table with:
# "import *". Pay attention that you do not accidentally overwrite a
# local variable or a function. Suggestion: Avoid using "import *".
# Libraries can be treated as modules (they are in general packages, but
# we won't go into details). Library modules sometimes have sub-modules.
# In some cases, these need to be imported as well before their content
# is accessible (but this depends on the library implementation). We
# will see some examples when introducing the numerical libraries.
