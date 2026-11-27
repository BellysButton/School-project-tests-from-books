import testA1shablon #Егор / импортируем шаблоны
import testB1shablon
choise1 = str(input("Введите название предмета"))
if choise1 == "Математика":
    ch1 = int(input("Выбирите вариант"))
    if ch1 == 1:
       testA1shablon.q1()
    elif ch1 == 2:
        testA1shablon.q2()
    elif ch1 == 3:
        testA1shablon.q3()
    else:
        print("Такого варианта нет!")
else:
    print("Такого названия нет!")
