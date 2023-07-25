q = input('введіть число: ')
w = int(q[0]) + int(q[1]) + int(q[2])

a = int(q)
s = a // 100
d = a - s * 100
f = d // 10
g = a % 10
h = s + f + g

print(w)
# print(s)
# print(d)
# print(f)
# print(g)
print(h)
