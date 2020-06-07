class Composes(object):
    def __init__(self, during, rate):
        self.during = during
        self.rate = rate
        self.name = "Композиція: "
        self.genre = "Жанр: "

    def __str__(self):
        return str("Композиція: {0}, Тривалість: {1}, Жанр: {2}, Рейтинг: {3}.").format(self.name, self.during,
                                                                                        self.genre, self.rate)

    def get_during(self):
        return self.during

    def get_rate(self):
        return self.rate


class Bank(Composes):
    def __init__(self, during, rate):
        Composes.__init__(self, during, rate)
        self.name = "21 Savage - Bank Account"
        self.genre = "Реп"


class Experience(Composes):
    def __init__(self, during, rate):
        Composes.__init__(self, during, rate)
        self.name = "Ludovico Einaudi - Experience"
        self.genre = "Неокласика"


class Humble(Composes):
    def __init__(self, during, rate):
        Composes.__init__(self, during, rate)
        self.name = "Kendrick Lamar - HUMBLE"
        self.genre = "Реп"


class Hurt(Composes):
    def __init__(self, during, rate):
        Composes.__init__(self, during, rate)
        self.name = "Johnny Cash - Hurt"
        self.genre = "Кантрі"


l = []

"""Функція для тривалості альбому"""


def sum_during():
    during = 0
    for i in l:
        during += i.get_during()
    return during


"""Функція для пошуку музики певної довжини"""


def find_music(l, start, end):
    correctm = []
    for i in l:
        if (i.get_during() >= start) and (end >= i.get_during()):
            correctm.append(i)
    return correctm
