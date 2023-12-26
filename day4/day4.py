import io
import re

demo_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

for line in io.StringIO(demo_input):
    game_id, winning_numbers, my_numbers = (
        re.search(r"Card\s+(\d+):\s+([\d\s]+)\|\s+([\d\s]+)", line).groups())

    winning_numbers = set(winning_numbers.split())
    my_numbers = set(my_numbers.split())
    intersection = winning_numbers.intersection(my_numbers)
    if len(intersection) > 0:
        score = 2 ** (len(intersection) - 1)
    else:
        score = 0

    print(f"Line = {line}, Score = {score}")


