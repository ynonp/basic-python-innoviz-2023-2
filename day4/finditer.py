"""
Getting multiple matches from regular expressions
with finditer
"""

import subprocess
import io
import re

ip_addresses = set()
output = subprocess.getoutput("/sbin/ifconfig")
for line in io.StringIO(output):
    if m := re.search(r'\b\d+\.\d+\.\d+\.\d+\b', line):
        print("Find All: ", re.findall(r'\b\d+\.\d+\.\d+\.\d+\b', line))
        print("Search: ", m.group(0))
        for match in re.finditer(r'\b\d+\.\d+\.\d+\.\d+\b', line):
            print("Find Iter: ", match.group(0))
            ip_addresses.add(match.group(0))

print(ip_addresses)



