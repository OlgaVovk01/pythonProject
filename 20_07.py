text = 'hi'
print(isinstance(text, str))
# x = True
# y = False
# print(x or y)

empty_list = []
empty = 'text'
print(bool(empty))
print(bool(empty_list))

seson = input('seson \n- ')
if seson == 'summer':
    print('temperature > 0')
elif seson == 'autumn' or seson == 'spring':
    print('temperature >= 0')
elif seson == 'winter':
    print('temperatur < 0')
else:
    print(f'opps! sezon doesnt exist! {seson}')

x = seson if seson else 'not valid input'
print(x)

q = int(input('q - '))
print(any([q > 0, q > 15, q < 30]))
d, f, g = 1, 0, 0
print(all([d == 0, f == 0, g == 0]))
