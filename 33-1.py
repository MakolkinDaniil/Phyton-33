import math;

print("Часть 1:")
print(424+2*(-2))
print("")

print("Часть 2:")
print(9**19 - int(float(9**19)))
print("")

print("Часть 3:")
end = 0
while end == 0:
    x = int(input("Введите количество часов: "))
    y = int(input("Введите количество минут: "))
    minutes = x*60 + y;
    print("Тимофей спит ", minutes, " минут")
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 4:")
end = 0
while end == 0:
    x = int(input("Введите количество минут: "))
    print("Часов: ", x//60)
    print("Минут: ", x%60)
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 5:")
end = 0
while end == 0:
    h = end = 0
    int(input("Введите количество часов: "))
    m = int(input("Введите количество минут: "))
    x = int(input("Введите количество минут для сна: "))
    y = h*60+m+x
    print("Часов: ", y//60)
    print("Минут: ", y%60)
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 6:")
end = 0
while end == 0:
    a = int(input("Введите минимальное количество часов: "))
    b = int(input("Введите максимальное количество часов: "))
    while b < a:
        print("Максимальное количество часов не может быть меньше минимального. Повторите попытку")
        b = int(input("Введите максимальное количество часов: "))
    h = int(input("Введите сколько часов спит Аня: "))
    y = h*60+m+x
    if h >= a and h <= b:
        print("Это нормально")
    elif h < a:
        print("Недосып")
    else:
        print("Пересып")
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 7:")
end = 0
while end == 0:
    year = int(input("Введите год в промежутке от 1900 до 3000: "))
    while year < 1900 or year > 3000:
        print("Введённое число выходит за рамки интервала. Повторите попытку")
        year = int(input("Введите год в промежутке от 1900 до 3000: "))
    if year // 4 == 0:
        if year // 100 != 0:
            print(year, " является високосным годом")
        else:
            print(year, " не является високосным годом")
    elif year // 400 == 0:
        if year // 100 != 0:
            print(year, " является високосным годом")
        else:
            print(year, " не является високосным годом")
    else:
        print(year, " не является високосным годом")
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 8:")
end = 0
while end == 0:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    c = input("Операция (+, -, /, *, mod, pow, div): ")
    if a / b == 0:
        print("Деление на 0!")
    if c == "+":
        print(a, "+", b, ' = ', a+b)
    if c == "-":
        print(a, "-", b, ' = ', a-b)
    if c == "/":
        print(a, "/", b, ' = ', a/b)
    if c == "*":
        print(a, "*", b, ' = ', a*b)
    if c == "mod":
        print(a, "mod", b, ' = ', a%b)
    if c == "pow":
        print(a, "pow", b, ' = ', a**b)
    if c == "div":
        print(a, "div", b, ' = ', a//b)
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 9:")
end = 0
while end == 0:
    figure = input("Выберете фигуру (треугольник, прямоугольник, круг): ")
    if figure == "треугольник":
        aTr = int(input("Сторона 1: "))
        bTr = int(input("Сторона 2: "))
        cTr = int(input("Сторона 3: "))
        perimetr = (aTr+bTr+cTr)/2
        print("Площадь треугольной комнаты: ", math.sqrt(perimetr*(perimetr-aTr)*(perimetr-bTr)*(perimetr-cTr)))
    if figure == "прямоугольник":
        aPr = int(input("Сторона 1: "))
        bPr = int(input("Сторона 2: "))
        print("Площадь прямоугольной комнаты: ", aPr*bPr)
    if figure == "круг":
        r = int(input("Радиус круглой комнаты: "))
        p = 3.14
        print("Площадь круглой комнаты: ", p*(r**2))
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 10:")
end = 0
while end == 0:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    c = int(input("Третье число: "))
    s = a + b + c;
    print(max(a,b,c))
    print(min(a,b,c))
    print(s - max(a,b,c) - min(a,b,c))
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 11:")
end = 0
while end == 0:
    a = int(input("Количество программистов: "))
    b = ""
    if a%10 == 1 and a%10 != 11:
        b = ""
    if a%10 == 2 and a%10 != 12:
        b = "а"
    if a%10 == 3 and a%10 != 13:
        b = "а"
    if a%10 == 4 and a%10 != 14:
        b = "а"
    if a%10 == 0:
        b = "ов"
    if a%100 == 14 or a%100 == 13 or a%100 == 12 or a%100 == 11:
        b = "ов"
    if a%10 == 5 or a%10 == 6 or a%10 == 7 or a%10 == 8 or a%10 == 9:
        b = "ов" 
    print(a, "программист" + b)
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

print("Часть 12:")
end = 0
while end == 0:
    a = int(input("Введите номер билета: "))
    a1 = a//100000
    print("a1: ",a1)
    a2 = (a//10000)%10
    print("a2: ",a2)
    a3 = (a//1000)%10
    print("a3: ",a3)
    a4 = (a//100)%10
    print("a4: ",a4)
    a5 = (a//10)%10
    print("a5: ",a5)
    a6 = a%10
    print("a6: ",a6)
    if (a1+a2+a3)==(a4+a5+a6):
        print("Счастливый")
    else:
        print("Обычный")
    end = int(input("Для остановки программы введите 1. Для продолжение вычислений введите 0: "))
print("")

