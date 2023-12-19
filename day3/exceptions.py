def numeric_input():
    try:
        return int(input())
    except ValueError:
        print("Please type numbers only")
        return numeric_input()


x = numeric_input()
print(f"{x} is a number, and x * 2 is {x * 2}")

#
# def print_numbers(n):
#     if n > 0:
#         print(n)
#         print_numbers(n - 1)
#
# print_numbers(1000)
#
