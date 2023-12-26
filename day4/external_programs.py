import subprocess
import io

# exxecute program "/sbin/ifconfig" and returns its output
output = subprocess.getoutput("/sbin/ifconfig")
print(output)

# read output line by line
for line in io.StringIO(output):
    print(line, end='')
