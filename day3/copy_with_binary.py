with open('input.txt', 'rb') as fin:
    with open('copy_of_input.txt', 'wb') as fout:
        while block := fin.read(1024):
            print(block)
            fout.write(block)
