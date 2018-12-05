# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number*(10**ndigits) + 0.41
    number = number//1
    return number/(10**ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    :param ticket_number: Номер билета
    :list_ticket:Переводим наш номер в строку для дальнейшего условия
    :if len(list_ticket) != 6: return False# Узнаем длину билета.Если билет не равен 6 то возращаем False.
    :first_number,second_number: Задаем переменные для сравнения цифр в билете.
    :for i in range(3):Запускаем цикл на растоянии 3 чисел.И узнаем суммы первых и последних трех чисел.
    :return: Возращает True если сумма первых и последних чисел равны
    """
    list_ticket = str(ticket_number)
    if len(list_ticket) != 6:
        return False
    first_numbers = 0
    second_numbers = 0
    for i in range(3):
        first_numbers += int(list_ticket[i])
        second_numbers += int(list_ticket[-i -1])
    return first_numbers == second_numbers

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))