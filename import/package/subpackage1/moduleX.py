

# from subpackage2.moduleZ import class_name
# print(class_name)

# ------------------ We can import moduleA

# import moduleA
# print(moduleA.foo)


# ------------------ We can import subpackage2.moduleZ.eggs

# from subpackage2.moduleZ import eggs
# print(eggs)


import sys 
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .moduleY import spam
print(spam)
print(__name__)
print(__package__)