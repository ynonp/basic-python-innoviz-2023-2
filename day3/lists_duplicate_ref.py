def clone_last_item(l: list):
    l.append(l[-1])
    return l

l = [10, 20, 30, 40]
g = l
clone_last_item(l)
print(g)


