"""
This program runs /sbin/ifconfig
and prints only the names of the network interfaces using
regular expressions

WARNING: It won't work on windows because you don't have ifconfig
"""

import subprocess
import io
import re

output = subprocess.getoutput("/sbin/ifconfig")
for line in io.StringIO(output):
    m = re.search(r"^[a-zA-Z0-9]+", line)
    if m is not None:
        print(m.group(0))

# New Syntax - python 3.8
# for line in io.StringIO(output):
#     if m := re.search(r"^[a-zA-Z0-9]+:", line):
#         print(m.group(0))
