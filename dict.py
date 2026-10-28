# men={
#     "name":"Abdulla",
#     "age":25,
#     "city":"Kara-balta"
# }
# # print(men)
# # Бардык keyлерди чыгаргыла.
# # print(men.keys())
#
# # Бардык valueларды чыгаргыла.
# # print(men.values())
#
# # key жана valueларды чогуу чыгаргыла.
# # print(men.items())
#
# # get() менен "name" маалыматтарын алгыла.
# # print(men.get("name"))
#
# # Dictionaryге "phone" кошкула.
# # men["phone"]="+996 507 688 005 "
# # print(men)
#
# # "age" маанисин өзгөрткүлө.
# # men["age"] = 26
# # print(men)
#
# # "city" элементин pop() менен өчүргүлө.
# # men.pop("city")
# # print(men)
#
# # Dictionaryде "name" барбы, текшергиле.
# if "name" in men:
#     print("name bar")

# 1. Dictionary түзгүлө:
# student={
# "name": "Aibek",
# "age": 20,
# "city": "Bishkek"
# }
# for key in student:
#     print(key)

# for колдонуп бардык keyлерди чыгаргыла.
# for value in student.values():
#     print(value)
# 2. Ошол эле Dictionaryнин бардык valueлерин values() аркылуу чыгаргыла.
# 3. items() колдонуп key жана valueлерди бирге чыгаргыла.
# for key, value in student.items():
#     print(key, value)
# # 4. Сандардан турган Dictionary түзгүлө:
# num = {
# "a": 10,
# "b": 25,
# "c": 8,
# "d": 40
# }
# for key,value in num.items():
#     if value >= 20:
#         print(value)
# for + if колдонуп 20дан чоң сандарды гана чыгаргыла.
# 5. Студенттердин баалары берилген:
# students = {
# "Ali": 85,
# "Bek": 60,
# "Aibek": 95,
# "Nurbek": 70
# }
# for name, grade in students.items():
#     if grade >= 80:
#         print(name)
# 80ден жогору баа алган студенттерди чыгаргыла.
# 6. Товарлардын баалары берилген:
# fruits ={
# "apple": 50,
# "banana": 80,
# "orange": 120
# }
# for fruit, price in fruits.items():
#     if price >= 100:
#         print(fruit)
# 100дөн кымбат товарларды чыгаргыла.
# 7. Dictionary берилген:
# languages = {
# "Python": 3,
# "JavaScript": 5,
# "C++": 2,
# "Java": 4
# }
# for language, value in languages.items():
#     if value > 2:
#         print(language, value)
# 2ден көп болгон маанилерди чыгаргыла.
# 8. Колдонуучудан 3 студенттин атын жана жашын алып, Dictionaryге сактагыла.
# Андан кийин for + if колдонуп 18 жаштан улуу студенттерди чыгаргыла.
# students = {}
#
# for i in range(3):
#     name = input("Студенттин аты: ")
#     age = int(input("Жашы
#     улуу студенттер:")
# for name, age in students.items():
#     if age > 18:
#         print(name, age)
# d = {
#     "name" : "Abdullah",
#     "age" : 25 ,
#     "student" : 3
# }
# print(input(d))
num = 1
while num <= 10 :
    print(num)
    num += 1