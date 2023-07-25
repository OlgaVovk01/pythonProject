q = input('Введіть данні snake_case: ')

q_s = q.split('_')
s = len(q_s)
a = list(range(s))

while s >= 0:
    s = s - 1
    a[s] = q_s[s].title()

# a = [q_s[0].title(), q_s[1].title(), q_s[2].title()]
print(''.join(a))
