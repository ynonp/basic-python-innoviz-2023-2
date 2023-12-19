class Summer:
    n: int = 0

    def add(self, new_value):
        self.n += new_value

    def __str__(self):
        return str(self.n)


s = Summer()
t = Summer()

s.add(10)
s.add(20)
s.add(30)
t.add(55)

# prints: 60
print(s)

# prints: 55
print(t)

x = s
x.add(40)
print(x)
print(s)





