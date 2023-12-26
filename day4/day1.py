import io

demo_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

for line in io.StringIO(demo_input):
    print(line, end="")

