"""
We have 2 ways to import modules in python

1. import <module_name>
2. from <module_name> import <function> (or *)

The difference is how we use the imported functions
"""

import math
print(math.sqrt(9))

from random import randint
print(randint(1, 10))

from re import *
print(search(r'wow', 'from import wow'))





