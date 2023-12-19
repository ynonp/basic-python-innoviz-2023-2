def digits(n: int):
    return [int(x) for x in str(n)]


def threes_and_fives(n: int):
    s = [i * 3 for i in range(n // 3 + 1)]
    t = [i * 5 for i in range(n // 5 + 1)]
    return set(s).union(set(t))


def longer_than(n: int, items: list[str]):
    return [t for t in items if len(t) > n]


def check_credentials(user: str, password: str):
    valid_credentials = {
        "admin": "1234",
        "user": "password",
        "db": "st0r@g3"
    }
    # Exception Handling
    try:
        return valid_credentials[user] == password
    except KeyError:
        return False
            


assert(digits(123) == [1, 2, 3])
assert(digits(724) == [7, 2, 4])
print(threes_and_fives(10))
print(longer_than(3, ['one', 'two', 'three']))
assert(check_credentials("admin", "admin") == False)
print(check_credentials("admin", "1234"))

# assert(result in [5, 6, 10])

print(check_credentials("ynon", "ynon"))







