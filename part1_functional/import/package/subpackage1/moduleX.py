import sys


# from subpackage2.moduleZ import class_name
# print(class_name)

# ------------------ We can import moduleA
for x in sys.path:
    print(x)
import package.moduleA as a 
print(dir(a))

from package import moduleA
print(moduleA.foo)

# ------------------ We can import subpackage2.moduleZ.eggs

# from subpackage2.moduleZ import eggs
# print(eggs)


# import sys 
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

# from . import moduleY
# print(moduleY.spam)