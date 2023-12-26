import io
import re
# Link To Exercise: https://adventofcode.com/2023/day/1

demo_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
calibration_value = 0

for line in io.StringIO(demo_input):
    first_digit = re.search(r'\d', line).group(0)
    last_digit = re.search(r'\d', line[::-1]).group(0)
    calibration_value_in_line = int(f"{first_digit}{last_digit}")
    calibration_value += calibration_value_in_line

print(calibration_value)

