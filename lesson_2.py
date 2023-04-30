print('Соревнования по Python')
count = int(input('Введите количество участников: '))
members = []
while count > 0:
    name = input(f'Кто занял {count} место: ')
    members.append(name)
    count -= 1


print(f'В соревновании участвовали {sorted(members)}')

members.reverse()

result = members[:3]
print(result)

# Удалите из первого списка элементы присутствующие во втором списке. ВАЖНОЖ: числа не повторяются

my_list_1 = [2, 5, 8, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)

result = list(my_list_1 - my_list_2)
print(result)



# удаляет только значение. Один только элемент.
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_2:
    if number in my_list_1:
        my_list_1.remove(number)

print(my_list_1)


# удаляет все значения и дубли
for number in my_list_2:
    while number in my_list_1:
        my_list_1.remove(number)

print(my_list_1)

# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

for i in my_list_1:
    while i in my_list_1:
        if i == i:
            my_list_1.remove(i)

print(my_list_1)

# Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

date = '02.11.2013'
day, month, year = date.split('.')
print(day,month, year)

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
days ={
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое'
}

print(f'{days[day]} {months[month]} {year} года')


# Метод .count() - это метод, который вызывается у списка (list), кортежа (tuple) или строки (string) в Python,
# и он используется для подсчета количества вхождений элемента в контейнере.

my_list_1 = [2, 2, 5, 12, 8, 2, 12]

result = []

for number in my_list_1:
    if my_list_1.count(number) == 1:
        result.append(number)

print(result)
