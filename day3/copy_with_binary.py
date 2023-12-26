"""
Python has 2 modes of working with files: text and binary
When working with text files we need to know the file's encoding (we'll usually
use utf8), and each line is converted to python's "str" object automatically

When working with binary files no conversion is made and python saves the
data as bytes buffers

This example shows how to copy a file in binary mode, using a buffer size of 1024.
Each iteration we read 1024 bytes from file "input.txt" and write the data to
the file "copy_of_input.txt"
"""
with open('input.txt', 'rb') as fin:
    with open('copy_of_input.txt', 'wb') as fout:
        while block := fin.read(1024):
            print(block)
            fout.write(block)
