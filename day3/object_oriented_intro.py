"""
Object Oriented is a coding paradigm that focuses on
the <object + methods> it has
"""


class SumOfThreesAndFives:
    # member fields
    n: int = 0
    sum: int = 0

    def reset(self, n):
        self.n = n
        self.sum = 0
        for i in range(n):
            if (i % 3 == 0) or (i % 5 == 0):
                self.sum += i

    def __sub__(self, other):
        return SumOfThreesAndFives(self.n - other.n)

    def __str__(self):
        return f"Sum of 3s and 5s until {self.n} = {self.sum}"

    def __init__(self, n):
        self.reset(n)
        print("inside function __init__()")


s = SumOfThreesAndFives(1_000)
print(s)



#
# def sum_3_and_5_until_n(n):
#     total = 0
#     for i in range(n):
#         if (i % 3 == 0) or (i % 5 == 0):
#             total += i
#     return total
#
#
result = SumOfThreesAndFives(1000)
print(result)

print(result.sum + 5)

x = SumOfThreesAndFives(5)
y = SumOfThreesAndFives(10)

print(x.sum)
print(y.sum)


print(dir(x))

# I want this to print:
# sum of 3s and 5s until 900 is: ...
print(SumOfThreesAndFives(1_000) - SumOfThreesAndFives(100))

print(x)
x.reset(50)
print(x)












