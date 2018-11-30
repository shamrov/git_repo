import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
sor = len(fruits[0])
index = 0

for index, fruit in enumerate(fruits):
    print('{} {:>{}}'.format(str(index + 1) + ".", fruit, sor))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first = [random.randrange(0, 10) for i in range(10)]
second = [random.randrange(0, 10) for i in range(10)]

set_first = set(first)
set_second = set(second)

del_list = set_first - set_second

print("Первый список : {}".format(first))
print("Второй список : {}".format(second))
print("Окончательный список: {}".format(del_list))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [random.randrange(0, 10) for i in range(10)]
new_a = []
print(a)
for i in a:
    if i % 2 == 0:
        new_a.append(int(i / 4))
    else:
        new_a.append(int(i * 2))
print(new_a)