lst1 = [1, 2, 3]

lst = [3, True, 1>4, lst1, 'text', None]

print(lst)
print(type(lst))
print(lst[2])
lst.append('last')
lst.append('last')
lst[5:] = '5'
del lst[0]
lst.remove(lst1)

print(lst)
print(len(lst))
#print(lst*2)
print(lst[1:])


lst_2 = lst.copy()
lst_3 = lst
lst_2.append('list_2_element')

print('list', lst)
print('lst3', lst_3)
print('lst2', lst_2)

print(id(lst))
print(id(lst_2))  #кортеж нормально копируется через равно или нет??????
print(id(lst_3))

numbers = [1, 2, 3, 4, 43]
print(max(numbers))

if 10 in numbers:
    print('True')
else:
    print('false')

print(numbers.count(4))

numbers.extend([6,7,8])
print(numbers)

numbers.insert(2, 100)
print(numbers)


