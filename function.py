# hello() деген функция түзүп, "Hello Python" чыгар.
#
# welcome() деген функция түзүп, "Python курсуна кош келиңиз!" чыгар.
#
# name() деген функция түзүп, өзүңдүн атыңды чыгар.
#
# numbers() деген функция түзүп, 1ден 10го чейинки сандарды for менен чыгар.
#
# even_numbers() деген функция түзүп, 1ден 20га чейинки жуп сандарды чыгар.
#
# Функция түзүп, "Мен Python үйрөнүп жатам" деген текстти 3 жолу чыгар.
# def name():
#     print("Abdulla")
# name()
# def num(a,b):
#     print(a+b)
# num(5,7)
# def san(a,b):
#     if a>b:
#        print(a)
#     elif a<b:
#         print(b)
# san(12,11)
# name параметрин алган функция түз. Функция адамдын атын чыгарышы керек.
# def name():
#     print("Abdulla")
# name()
# Эки сан кабыл алган функция түзүп, алардын суммасын чыгар.
# def num(a,b):
#     print(a+b)
# num(5,7)
# Эки сан кабыл алган функция түзүп, чоң санды чыгар.
# def san(a,b):
#     if a>b:
#        print(a)
#     elif a<b:
#         print(b)
# san(12,11)


# Эки сан кабыл алган add() функциясын түз. Функция алардын суммасын return кылсын.
# def add(a,b):
#     return a+b
# print(add(3,4))
# Эки сан кабыл алган multiply() функциясын түз. Функция алардын көбөйтүндүсүн return кылсын.
# def multiply(a,b):
#     return a*b
# print(multiply(10,4))
# square() функциясын түз. Бир сан кабыл алып, анын квадратын return кылсын.
# def square(num  ):
#     return num * num
# print(square(3))
# print(square(4))
# Эки сан кабыл алган max_number() функциясын түз. Чоң санды return кылсын.
# def max_number(a,b):
#     return max(a,b)
# print(max_number(10,20))
# number_status() функциясын түз. Сан оң болсо "Оң сан", терс болсо "Терс сан", 0 болсо "Нөл" деген маанини return кылсын.
# def number_status(number):
#     if number > 0:
#         return "Оn сан"
#     elif number < 0:
#         return "Терс сан"
#     else:
#         return "Нoл"
#
# print(number_status(5))   # Оn сан
# print(number_status(-3))  # Терс сан
# print(number_status(0))   # Нoл
# is_even() функциясын түз. Сан жуп болсо True, так болсо False кайтарсын.
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(4))
# print(is_even(7))
# get_full_name() функциясын түз. name жана surname кабыл алып, толук аты-жөнүн return кылсын.
# def get_full_name(name, surname):
#     return name + " " + surname
#
# print(get_full_name("Абдулла", "Рашидов"))
# calculate_age() функциясын түз. Туулган жылды кабыл алып, адамдын жашын return кылсын.
# def calculate_age(birth_year):
#     return 2026 - birth_year
# print(calculate_age(2001))
# Үч сан кабыл алган average() функциясын түз. Үч сандын орточо маанисин return кылсын.
# def average(a, b, c):
#     return (a + b + c) / 3
# print(average(10, 20, 30))
# Эки сан жана операция кабыл алган calculate() функциясын түз. Мисалы: calculate(10, 5, "+") → 15 calculate(10, 5, "-") → 5 calculate(10, 5, "*") → 50 calculate(10, 5, "/") → 2
# def calculate(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         return a / b
# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "-"))
# print(calculate(10, 5, "*"))
# print(calculate(10, 5, "/"))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]#. #Жуп сандарды filter() аркылуу тап.
# result = (filter(lambda x : x %  2 == 0,numbers))
# print(list(result))
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]. Так сандарды filter() аркылуу тап.
# result = (filter(lambda x : x %  2 != 0,numbers))
# print(list(result))
# numbers = [5, 12, 3, 20, 15, 7]  #. 10дон чоң сандарды тап.
# # result = filter(lambda x: x > 10, numbers)
# # print(list(result))
# # numbers = [5, 12, 3, 20, 15, 7]. 10дон кичине сандарды тап.
# result = filter(lambda x: x < 10, numbers)
# print(list(result))
# numbers = [-5, 10, -3, 7, -1, 8] #. Оң сандарды гана танда.
# result = filter(lambda x: x > 0 , numbers)
# print(list(result))
# # numbers = [-5, 10, -3, 7, -1, 8]. Терс сандарды гана танда.
# result = filter(lambda x: x < 0 , numbers)
# print(list(result))
# ages = [12, 17, 18, 20, 15, 25] #. 18 жаштан чоң же барабар болгон жаштарды тап.
# result = filter(lambda x: x >= 18, ages)
# print(list(result))
# names = ["Ali", "Bek", "Azamat", "Aibek", "Nur"] #. Узундугу 4төн чоң болгон аттарды тап.
# result = filter(lambda name: len(name) >4 , names )
# print(list(result))
# numbers = [10, 15, 20, 25, 30, 35] #. 5ке бөлүнгөн сандарды filter() менен тап.
# result = filter(lambda x: x % 5 == 0, numbers)
# print(list(result))
# numbers = [1, 2, 3, 4, 5] #. Алгач filter() менен жуп сандарды тандап, андан кийин map() менен аларды 2ге көбөйт.
# result = filter(lambda x: x % 2 == 0, numbers)
# result_x = map(lambda x: x * 2, result)
# print(list(result_x))
numbers=[i for i in range(1,6)]
print(numbers)