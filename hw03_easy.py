# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number*(10**ndigits)+0.4
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
    ticket_number = str(ticket_number)
    if len(ticket_number) != 6:
        return False

    ticket_num1 = ticket_number[:3]
    ticket_num2 = ticket_number[3:]
    ticket_num1_sum = 0
    ticket_num2_sum = 0
    for i in ticket_num1:
        ticket_num1_sum = ticket_num1_sum + int(i)

    for i in ticket_num2:
        ticket_num2_sum = ticket_num2_sum + int(i)

    if ticket_num1_sum == ticket_num2_sum:
        return True
    else:
        return False
    
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))