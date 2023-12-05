# https://github.com/ynonp/basic-python-innoviz-2023-2

# def - define a new function
# def function-name():
#   body
#   body
def euler6(last_number_in_sum: int):
    total = 0
    total_squares = 0
    for i in range(1, last_number_in_sum + 1):
        total += i
        total_squares += i ** 2

    square_total = total ** 2
    return square_total - total_squares


x = euler6(10)
print(x)
print(f"The big answer is: {euler6(100)}")
euler6(1000)
