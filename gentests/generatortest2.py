import testA1shablon #Егор / импортируем шаблоны
import testB1shablon
import testC1shablon
choise1 = str(input("Введите название предмета"))
if choise1 == "Математика": #Егор / В выборе предметов костыли, это можно в будующем опимизировать через лист-шаблон с предметами
    ch1 = int(input("Выбирите вариант"))
    if ch1 == 1:
       testA1shablon.q1()
    elif ch1 == 2:
        testA1shablon.q2()
    elif ch1 == 3:
        testA1shablon.q3()
    else:
        print("Такого варианта нет!")
elif choise1 == "Русский язык":
    ch2 = int(input("Выберите вариант"))
    if ch2 == 1:
        testC1shablon.rq1() #Егор / тут можно было функцию назвать q1 а не rq1, нужно взять на заметку
    elif ch2 == 2:
        testC1shablon.rq2()
    elif ch2 == 3:
        testC1shablon.rq3()
    else:
        print("Такого варианта нет!")
else:
    print("Такого названия нет!")
