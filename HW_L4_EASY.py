import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

first = [random.randint(0, 4) for _ in range(10)]
second = []
for f in first:
    second.append(f*f)
print("Изначальный список: ", first)
print("Новый список: ", second)

# Другой вариант решения
test_first = [random.randint(0, 4) for _ in range(10)]
test_second = [x ** 2 for x in test_first]
print("Изначальный список: ", test_first)
print("Новый список: ", test_second)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_list = ["Яблоко", "Арбуз", "Дыня", "Ананас", "Киви", "Банан", "Манго"]
second_list = ["Яблоко", "Арбуз", "Дыня", "Мандарин", "Апельсин", "Маракуя", "Банан"]
last_list = list(set(first_list) & set(second_list))
print(last_list)

# Не смог подгрузить файл

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

first = [random.randint(-1, 15) for _ in range(10)]
second = []
for f in first:
    if f > 0 and f % 3 == 0 and f % 4 != 0:
        second.append(f)
print("Изначальный список: ", first)
print("Новый список: ", second)

# Другой вариант решения
test_l = [random.randint(-1, 15) for _ in range(10)]
thirtd = [i for i in test_l if i > 0 and i % 3 == 0 and i % 4 != 0]
print("Изначальный список: ", test_l)
print("Новый список: ", thirtd)
