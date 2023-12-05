# Create a list with [...]
digits = [7, 4, 2]
names = ["Bill", "Luke", "Jane", "Tim"]
mixed = [12, "Bill", 19, [1, 2, 3], False]

# Create a list from characters of string
chars = list("hello") # chars = ["h", "e", "l", "l", "o"]

# Create a list iteratively
items = []
items.append("book")
items.append("table")
items.append("chair")
# items == ["book", "take", "chair"]

# create a list of words from a string
# words == ["one", "two", "three"]
words = "one two three".split()

print(sum(digits))
print(max(digits))

number = input("please type a number: ")
digits_as_strings = list(number)
digits_as_ints = [int(i) for i in digits_as_strings]


print(digits_as_ints)
print(digits_as_strings[0])
# last item in list
print(digits_as_strings[-1])
# len - how many items are there in the list
print(len(digits_as_strings))

# create new list from existing list
[10, 20, 30, 40][1:]

# get index of value
[10, 20, 30, 40].index(20)

grades = [99, 95, 100, 92, 89]
avg = sum(grades) / len(grades)
