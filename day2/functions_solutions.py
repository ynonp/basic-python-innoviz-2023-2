def sum_three_numbers(x=0, y=0, z=0):
    return x + y + z


# TypeError
# print(sum_three_numbers(10, 20, 30, 40))
print(sum_three_numbers(10, 20, 30))
print(sum_three_numbers(10, 20))
print(sum_three_numbers())

def sum_digits(n):
    total = 0
    while n > 0:
        right_digit = n % 10
        total += right_digit
        n = n // 10
    return total


def sum_digits_until_one_digit_number(n):
    result = sum_digits(n)
    while result >= 10:
        result = sum_digits(result)

    return result


print(sum_digits_until_one_digit_number(1254))


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


assert(is_prime(17) == True)
assert(is_prime(4) == False)
assert(is_prime(21) == False)
assert(is_prime(23) == True)
assert(is_prime(13) == True)
assert(is_prime(3) == True)
assert(is_prime(2) == True)

count = 0
for i in range(2, 1_000_000):
    if is_prime(i):
        count += 1
print(count)

