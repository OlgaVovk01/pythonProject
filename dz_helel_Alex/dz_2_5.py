# TS = 'Taras Shevcenko*1814-03-09*1861-03-10'
TS = input('Введіть : Ім\'я Прізвище*Дату народження(____-__-__)*Дату смерті(____-__-__)\n: ')
TS_mas = TS.split('*')
TS_1dat = TS_mas[1].split('-')
TS_2dat = TS_mas[2].split('-')
age = int(TS_2dat[0]) - int(TS_1dat[0])
print(f'Name: {TS_mas[0]}\nAge: {age} years')
