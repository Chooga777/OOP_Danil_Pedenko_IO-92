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


text = "Привет! Андрей, интерес, волшебство. Оля? Анон, Алексей, вадик."
l = Laba(text)
