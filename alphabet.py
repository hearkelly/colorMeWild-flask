import os
from letter import Letter


class Alphabet:
    # string id: unique byteID -> stringID using set_id()
    def __init__(self):
        self.id = self.set_id()
        self.usedLetters = []
        self.avgColor = []

    def get_id(self):
        return self.id

    # takes some bytes from the OS
    # converts to alphanumeric string,
    # replacing !alnum with "-"
    def set_id(self):
        byteID = str(os.urandom(4))
        stringID = ""
        for char in byteID:
            if char.isalnum():
                stringID += char
            else:
                stringID += "-"
        return stringID

    def add_letter(self, char):
        for lttr in self.usedLetters:
            if ord(char) != lttr.uniLetter:
                newLetter = Letter(char)
                self.usedLetters.append(newLetter)
                self.mixer(newLetter)
            else:
                # send to mixer *twice*
                self.mixer(lttr)
                self.mixer(lttr)

    # takes a new letter
    # adds its given rgb values, divides by two
    # in order to mix with alphabet current color
    def mixer(self, newLetter):
        self.avgColor[0] = (self.avgColor[0] + newLetter.color.red)/2
        self.avgColor[1] = (self.avgColor[1] + newLetter.color.green)/2
        self.avgColor[2] = (self.avgColor[2] + newLetter.color.blue)/2

    def __str__(self):
        self.usedLetters.sort()
