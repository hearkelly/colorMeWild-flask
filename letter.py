from color import Color


class Letter:

    def __init__(self, char):
        self.strLetter = char
        self.uniLetter = ord(char)
        self.color = Color()

    def __eq__(self, other):
        if isinstance(self, Letter) & isinstance(other, Letter):
            return self.uniLetter == other.uniLetter
