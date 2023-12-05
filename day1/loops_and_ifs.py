# Conditions - Decide what to do based on X
# Python Module list:
# https://docs.python.org/3/py-modindex.html


name = input("what's your name? ")

if name.startswith("x"):
    print("Wow what a lovely name")
    print("You must be happy all the time")
elif name.endswith("y"):
    print("I don't like your name")
    print("go away")
elif "gh" in name:
    print("that's a special name")
else:
    print(f"Hello {name}")

print("the end")

# Loops - do something multiple times

# 1. While loops
# do something WHILE a condition is true
#
i = 1
while i < 10:
    print(i)
    i += 1

import random
i = random.randint(1, 60)
print(i)
print("---")
while i < 50:
    print(i)
    i = random.randint(1, 60)



while True:
    i = random.randint(1, 60)
    print(i)
    if i < 50:
        break




#
# 2. For loops
# do something X times
#

for i in range(10):
    print(i)

for i in range(5, 100, 2):
    print(i)

for i in range(100, 1, -4):
    print(i)






