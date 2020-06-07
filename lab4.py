import operator as op


class Aircraft(object):
    def __init__(self, places, speed, height, mass, fly):
        self.places = places
        self.height = height
        self.speed = speed
        self.mass = mass
        self.fly = fly
        self.name = "Літак: "

    def __str__(self):
        return str(
            "Літак: {0}, Кількість місць: {1}, Швидкість: {2}, Висота польоту: {3}, Злітна маса: {4}, Дальність польоту: {5}").format(
            self.name, self.places, self.speed, self.height, self.mass, self.fly)


class T134(Aircraft):
    def __init__(self, places, speed, height, mass, fly):
        Aircraft.__init__(self, places, speed, height, mass, fly)
        self.name = "Туполєв Ту-134"


class T154(Aircraft):
    def __init__(self, places, speed, height, mass, fly):
        Aircraft.__init__(self, places, speed, height, mass, fly)
        self.name = "Туполєв Ту-154"


class T204(Aircraft):
    def __init__(self, places, speed, height, mass, fly):
        Aircraft.__init__(self, places, speed, height, mass, fly)
        self.name = "Туполєв Ту-204"


class S100(Aircraft):
    def __init__(self, places, speed, height, mass, fly):
        Aircraft.__init__(self, places, speed, height, mass, fly)
        self.name = "Сухий Суперджет-100"


l = []
while True:
    ch = input("1: Вибрати літаки\n2: Відсортувати за швидкістю\n3: Відсортувати за кількістю місць\n0: Вихід\n")
    if ch == "1":
        ch = input("1: Туполєв Ту-134\n2: Туполєв Ту-154\n3: Туполєв Ту-204\n4: Сухий Суперджет-100\n")
        if ch == "1":
            places = int(input("Задати кількість місць: "))
            speed = int(input("Задати швидкість: "))
            height = int(input("Задати висоту польоту: "))
            mass = int(input("Задати злітну массу: "))
            fly = int(input("Задати дальність польоту: "))
            t = T134(places, speed, height, mass, fly)
            l.append(t)
        elif ch == "2":
            places = int(input("Задати кількість місць: "))
            speed = int(input("Задати швидкість: "))
            height = int(input("Задати висоту польоту: "))
            mass = int(input("Задати злітну массу: "))
            fly = int(input("Задати дальність польоту: "))
            t = T154(places, speed, height, mass, fly)
            l.append(t)
        elif ch == "3":
            places = int(input("Задати кількість місць: "))
            speed = int(input("Задати швидкість: "))
            height = int(input("Задати висоту польоту: "))
            mass = int(input("Задати злітну массу: "))
            fly = int(input("Задати дальність польоту: "))
            t = T204(places, speed, height, mass, fly)
            l.append(t)
        elif ch == "4":
            places = int(input("Задати кількість місць: "))
            speed = int(input("Задати швидкість: "))
            height = int(input("Задати висоту польоту: "))
            mass = int(input("Задати злітну массу: "))
            fly = int(input("Задати дальність польоту: "))
            t = S100(places, speed, height, mass, fly)
            l.append(t)
    elif ch == "2":
        l.sort(key=op.attrgetter("speed"), reverse=True)
        for i in l:
            print(i)
    elif ch == "3":
        l.sort(key=op.attrgetter("places"), reverse=False)
        for i in l:
            print(i)
    elif ch == "0":
        break