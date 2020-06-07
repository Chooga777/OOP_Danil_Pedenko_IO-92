from Lab6 import *
import operator as op

while True:
    ch = input(
        "1: Записати в альбом композицію\n2: Порахувати тривалість альбому\n3: Визначити за рейтингом\n4: Визначити композицію за певним діапазоном\n0: Вихід\n")
    if ch == "1":
        ch = input(
            "1: 21 Savage - Bank Account\n2: Ludovico Einaudi - Experience\n3: Kendrick Lamar - HUMBLE\n4: Johnny Cash - Hurt\n")
        if ch == "1":
            during = int(input("Задати тривалість в секундах: "))
            rate = int(input("Задати рейтинг: "))
            b = Bank(during, rate)
            l.append(b)
        elif ch == "2":
            during = int(input("Задати тривалість в секундах: "))
            rate = int(input("Задати рейтинг: "))
            b = Experience(during, rate)
            l.append(b)
        elif ch == "3":
            during = int(input("Задати тривалість в секундах: "))
            rate = int(input("Задати рейтинг: "))
            b = Humble(during, rate)
            l.append(b)
        elif ch == "4":
            during = int(input("Задати тривалість в секундах: "))
            rate = int(input("Задати рейтинг: "))
            b = Hurt(during, rate)
            l.append(b)
    elif ch == "2":
        print(sum_during())
    elif ch == "3":
        l.sort(key=op.attrgetter("rate"))
        for i in l:
            print(i)
    elif ch == "4":
        start = int(input("Початкова секунда: "))
        end = int(input("Кінцева секунда: "))
        for i in find_music(l, start, end):
            print(i)
    elif ch == "0":
        break
