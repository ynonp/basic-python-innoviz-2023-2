# open file "files.py",
# print all the lines
# and close the file
f = open('files.py', 'r', encoding='utf8')
for line in f:
    print(line)
f.close()

# same, no need to remember f.close() - USE THIS IT'S BETTER
with open('files.py', 'r', encoding='utf8') as f:
    for line in f:
        print(line)

# print only the first line from file
with open('files.py', 'r', encoding='utf8') as f:
    first_line = f.readline()
    print(first_line)










