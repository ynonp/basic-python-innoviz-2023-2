"""
Ex 1 - Create a text file and write to it all the numbers
from 1 to 100, each number in its own line
"""

with open('numbers.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 101):
        print(i, file=f)


with open('files.py', 'r', encoding='utf-8') as fin:
    with open('copy_of_files.py', 'w', encoding='utf-8') as fout:
        for line in fin:
            fout.write(line)


