# Exercises
# Project:
# https://github.com/ynonp/basic-python-innoviz-2023-2
#
# https://projecteuler.net/problem=1
# Answer: 233168
#
# https://projecteuler.net/problem=4
# Hint: "9009" == "9009"[::-1]
# Answer: 906609
#
# https://projecteuler.net/problem=6
# Answer: 25164150
#
# 3, 5, 6, 9
total = 0
for i in range(1_000):
    if (i % 3 == 0) or (i % 5 == 0):
        # print(f"{i} is a multiplication of 3 or 5")
        total += i

print("ex1:")
print(total)

max_product = 0
for i in range(100, 1_000):
    for j in range(100, 1_000):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > max_product:
                max_product = product

print(max_product)






