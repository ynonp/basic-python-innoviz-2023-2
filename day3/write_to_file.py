# modes:
# r - read
# w - write
# a - append
# for logs:
# https://docs.python.org/3/library/logging.html
with open('output.txt', 'w', encoding='utf8') as f:
    f.write("it's my file\n")
    f.write("and I'll cry if I want to\n")


