
# int=1 jonokoy sandar
# float=1,2 bolchok sandar
# str="argen2001" tyrmakchaga alyngan sozdor/sandar
# boolean=True , False
# print=(3+4) maalymat chygaruuchu comanda


# Жашың
# age деген өзгөрмө түзүп, ага жашыңды жаз. Экранга чыгар.

# age=25
# print(age)


# Атың
# name деген өзгөрмө түзүп, ага атыңды жаз. print() менен чыгар.
#
# name=('Abdulla')
#
# print(name)

# Эки сан
# # a = 10, b = 5 деген эки өзгөрмө түз. Алардын суммасын экранга чыгар.
# a=10; b=5
#
# print(a+b)


# Баасы
# price = 99.5 деген өзгөрмө түзүп, экранга чыгар.
# price=120.50
#
# print(price)

# Атың жана жашың
# name жана age өзгөрмөлөрүн түзүп, экөөнү тең экранга чыгар.





# Боюң
# height = 1.75 деген өзгөрмө түзүп, экранга чыгар.
# height = 1.74
# print(height)



#
# Boolean
# is_student = True жана is_working = False деген эки өзгөрмө түзүп, экранга чыгар.
# Үч тип
# is_student = True
# is_working = False
# print(is_student)
# print(is_working)

# +    сложение
# -    вычитание
# *    умножение
# /    деление
# //   деление без остатка
# %    остаток
# **   степень


# # a = 15, b = 5 деген эки өзгөрмө түзүп, алардын суммасын чыгаргыла.
# a=15
# b=5
# print(a+b)
#
#
# # a = 8, b = 6 берилген. Көбөйтүндүсүн тапкыла.
# a=8
# b=6
# print(a*b)
#
#
#
# # a = 20, b = 4 берилген. Бөлүндүсүн тапкыла.
# a=20
# b=4
# print(a/b)
#
#
#
# # a = 17, b = 5 берилген. Бөлгөндөгү калдыгын тапкыла.
# a=17
# b=5
# print(a//b)
#
# # a = 20, b = 7 берилген. Айырмасын тапкыла
#
# a=20
# b=7
# print(a-b)
#
#
# name=('Abdulla')
# print(name)
#
# height = 1.74
# print(height)
# input() - mmalymat aluu uchun koldulat

# name = input("atyndy jaz: ")
# print(name)
#
#
# jashaganjer = input("jashagan jerindy jaz: ")
# print(jashaganjer)

# age = input("age: ")  <class 'str'> str = "mirbek" , "45"
# print(type(age))

# age = int(input("jasgyndy jaz : "))
# # age = float(age)
# print("senin jashyn: ",age)

# age = int(input("jasgyndy jaz : "))
# print(age * 6)

# height = float(input("boyndu jaz: "))
# print(height)
# Колдонуучудан атын сурап, экранга:
# Салам, [аты]! деп чыгаргыла.

#
# # Колдонуучудан жашын сурап, 5 жылдан кийинки жашын чыгаргыла.
# age=int(input("Enter your age: "))
# print(age+5)
#
# # Колдонуучудан эки сан алып, алардын суммасын чыгаргыла.
# Эки сан алып, алардын:
# айырмасын
# көбөйтүндүсүн
# бөлүндүсүн чыгаргыла.
# Колдонуучудан бир сан алып, анын квадратын чыгаргыла.
# sum=int(input("enter your sum "))
# print(sum +15)
# print(sum -15)
# print(sum *15)
# print(sum /15)
# print(sum ** 15)
# 'mirbek', "nurbek"
#
#
# name = 'Mirbek'
# print(len(name))

# word = "Python"
# Python
# 012345
# print(word[0])
# print(word[2])
# print(word[5])
# P   y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# print(word[-1])
# print(word[-3])
# print(word[-5])

# word = "Python"
#         012
#         123
# print(word[0:3])        [start : stop]

# print(word[:3]) Pyt
# print(word[2:])
# print(word[:])

# word = "Python"
# print(word[0:6:2])  [start : stop : step ]
# print(word[::2])
# print(word[::-2])

# escape posledovatelnost

# \n newline - janysap
# \t Tab/ boshtuk aralyk
# \" kosh tyrmakkcha
# \' jalgyz tyrmakcha
# \\ slesh belgisi
# \b backspace

# print("Hello\tWorld\tis\tthe ")
# print("Hello \nWorld\nis\nthe ")
# print("He said: \"Hello\"")
# print("He said: \'Hello\'")
# print("Hello \\Mirbek\\")
# # print("Hello\b\b\bMirbek") HeMirbek
#
# Срездер жана Escape-последовательностор боюнча тапшырмалар
#
# 1. "Python" деген сап берилген. Индекс аркылуу "P" тамгасын чыгаргыла.
#
# 2. "Python" деген сап берилген. Индекс аркылуу акыркы "n" тамгасын чыгаргыла.
#
# 3. "Python" деген саптан "Pyt" бөлүгүн срез аркылуу чыгаргыла.
#
# 4. "Python" деген саптан "hon" бөлүгүн срез аркылуу чыгаргыла.
#
# 5. "Programming" деген саптан "gram" сөзүн срез аркылуу чыгаргыла.
#
# 6. "Programming" деген саптан биринчи 5 символду чыгаргыла.
#
# 7. "Programming" деген саптан 4-индекстен баштап аягына чейинки символдорду чыгаргыла.
#
# 8. "Hello World" деген сапты толугу менен тескери чыгаргыла.
#
# 9. "Python Programming" деген саптагы ар бир экинчи символду чыгаргыла.
#
# 10. "JavaScript" деген саптын биринчи 4 символун чыгаргыла.
#
# 11. "JavaScript" деген саптын акыркы 4 символун чыгаргыла.
#
# 12. "Computer" деген саптан "put" бөлүгүн срез аркылуу чыгаргыла.
#
#
# ESCAPE-ПОСЛЕДОВАТЕЛЬНОСТОР
#
# 13. \n колдонуп төмөнкүдөй чыгара турган программа жазгыла:
#
# Hello
# World
#
# 14. \n колдонуп үч сап чыгаргыла:
#
# Python
# JavaScript
# HTML
#
# 15. \t колдонуп төмөнкүдөй маалымат чыгаргыла:
#
# Name:    Mirbek
# Age:     20
# City:    Bishkek
#
# 16. \t колдонуп төмөнкүдөй таблица түзгүлө:
#
# Name    Age    City
# Ali     20     Osh
# Bek     21     Bishkek
#
# 17. \" колдонуп төмөнкү текстти чыгаргыла:
#
# He said: "Python is easy"
#
# 18. \" колдонуп төмөнкү текстти чыгаргыла:
#
# My teacher said: "Study Python every day"
#
# 19. \\ колдонуп төмөнкү жолду чыгаргыла:
#
# C:\Users\Mirbek\Python
#
# 20. \n жана \t экөөнү тең колдонуп төмөнкүдөй маалымат чыгаргыла:
#
# Student:
#     Name: Mirbek
#     Age: 20
#     Course: Python
#
# 21. Колдонуучудан input() аркылуу атын алгыла жана төмөнкүдөй чыгаргыла:
#
# Hello!
#     Mirbek
# Welcome to Python!
#
# 22. "Python" деген сөздү срез жана \n колдонуп төмөнкүдөй чыгаргыла:
#
# P
# y
# t
# h
# o
# n
#
# 23. "Python Programming" деген саптын биринчи 6 символун алып, \n аркылуу эки сапка бөлүп чыгаргыла.
#
# 24. Өзүңөр каалаган сап түзүп, анын:
# - биринчи символун;
# - акыркы символун;
# - биринчи 3 символун;
# - акыркы 3 символун;
# - тескери вариантын
#
# чыга
# for жана range() колдонуп 1ден 10го чейинки сандарды чыгаргыла.
# for i in range(1, 11):
#     print(i)
# 10дон 1ге чейинки сандарды тескери чыгаргыла.
# for i in range(10, 1, -1):
#     print(i)
# 1ден 20га чейинки жуп сандарды чыгаргыла.
# for i in range(2, 22, 2):
#     print(i)
# # 1ден 20га чейинки так сандарды чыгаргыла.
# for i in range(1, 21, 1):
#     print(i)
# 1ден 50гө чейинки 5ке бөлүнгөн сандарды чыгаргыла.
# for i in range(1, 51,):
#     if i % 5 == 0:
#         print(i)
# # 1ден 10го чейинки сандардын квадраттарын чыгаргыла.
# for i in range(1, 11,):
#     print(i ** 2)
# 1ден 100гө чейинки 10го бөлүнгөн сандарды чыгаргыла.
# for i in range(1, 101):
#     if i % 10 == 0:
#         print(i)
# 1ден 30га чейинки сандардын ичинен 3кө да, 2ге да бөлүнгөндөрүн чыгаргыла.
# for i in range(1, 31):
#     if i % 3== 0 and i % 2 == 0:
#             print(i)
# number = 1 while number <= 3:
#     print(number)
#     number += 1

