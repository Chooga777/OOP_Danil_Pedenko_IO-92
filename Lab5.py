class Laba:
    """Початковий код з лаби №3."""

    def __init__(self, tex):
        self.lett = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]
        self.tex = tex
        self.punct = "? ,.!"
        self.texwoutp = ""
        self.glas = []
        """Алгоритм для розбиття тексту на слова"""
        for self.i in range(len(self.tex)):
            if self.tex[self.i] not in self.punct:
                self.texwoutp += self.tex[self.i]
            if self.tex[self.i] == " ":
                self.texwoutp += " "
        """Алгоритм для додавання слів які починаються на голосну літеру"""
        for self.j in range(len(self.texwoutp.split())):
            """Перевірка чи починається слово на голосну літеру"""
            if self.texwoutp.split()[self.j][0] in self.lett:
                self.glas.append(self.texwoutp.split()[self.j])
        """Сортуування слів за другою літерою"""
        self.sorter = sorted(self.glas, key=lambda x: x[1])
        print(self.sorter)


class Texts:
    """Класс для розбиття тексту на масив речень."""

    def __init__(self, teh):
        self.teh = teh
        self.punctuation = "?.!"
        self.enrid = ""
        self.tewisen = []
        """Алгоритм розбиття тексту на речення."""
        for self.i in range(len(self.teh)):
            self.enrid += self.teh[self.i]
            """Перевірка, яка говорить, коли закінчується речення."""
            if self.teh[self.i] in self.punctuation:
                """Перевірка, щоб нове речення починалося не з пробіла."""
                if self.enrid[0] == " ":
                    self.tewisen.append(self.enrid[1:])
                else:
                    self.tewisen.append(self.enrid)
                self.enrid = ""


class Sentences:
    """Класс для розбиття речень на слова."""

    def __init__(self, teh):
        self.teh = teh
        self.te = Texts(self.teh)
        self.cu = "?.!,"
        self.senwiwor = []
        self.enpu = ""
        """Алгоритм розбиття речень на слова."""
        for self.i in range(len(self.te.tewisen)):
            self.senwiwor.append([])
            for self.j in range(len(self.te.tewisen[self.i])):
                """Перевірка чи є елемент знаком пунктуації, щоб відокремити знак зі словом. 
                Друга перевірка, щоб відокремити слова, які не пов'язані зі знаками пунктуації."""
                if self.te.tewisen[self.i][self.j] in self.cu:
                    self.enpu += self.te.tewisen[self.i][self.j]
                    self.senwiwor[self.i].append(self.te.enrid)
                    self.senwiwor[self.i].append(self.enpu)
                    self.te.enrid = ""
                    self.enpu = ""
                elif self.te.tewisen[self.i][self.j] != " ":
                    self.te.enrid += self.te.tewisen[self.i][self.j]
                else:
                    if self.te.enrid != "":
                        self.senwiwor[self.i].append(self.te.enrid)
                        self.te.enrid = ""


class Word:
    """Класс для розбиття слів на літери"""

    def __init__(self, teh):
        self.teh = teh
        self.sen = Sentences(self.teh)
        self.worwilet = []
        """Алгоритм, який розбиває слова на літери."""
        for self.i in range(len(self.sen.senwiwor)):
            self.worwilet.append([])
            for self.j in range(len(self.sen.senwiwor[self.i])):
                self.worwilet[self.i].append([])
                for self.k in range(len(self.sen.senwiwor[self.i][self.j])):
                    self.sen.te.enrid += self.sen.senwiwor[self.i][self.j][self.k]
                    self.worwilet[self.i][self.j].append(self.sen.te.enrid)
                    self.sen.te.enrid = ""


text = "Привет! Андрей, интерес, волшебство. Оля? Анон, Алексей, вадик."
l = Laba(text)
t = Texts(text)
s = Sentences(text)
w = Word(text)
print(t.tewisen)
print(s.senwiwor)
print(w.worwilet)
