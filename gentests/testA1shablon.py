#Егор / Тест шаблона который будет импортироваться в основной файл через import test1shablon
def q1():
    qq1 = int(input("1+1=..."))
    while qq1 != 2:
        print("Неправильно, попробуй ещё раз")
        qq1 = int(input("1+1=..."))
    print("Правильно")

def q2():
    qq2 = int(input("2+2=..."))
    while qq2 != 4:
        print("Неправильно, попробуй ещё раз")
        qq2 = int(input("2+2=..."))
    print("Правильно")
    
def q3():
    qq3 = int(input("3+2=..."))
    while qq3 != 5:
        print("Неправильно, попробуй ещё раз")
        qq3 = int(input("3+2=..."))
    print("Правильно")