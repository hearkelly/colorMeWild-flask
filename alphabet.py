import os
from name import Name
from color import Color
import random


# need to implement a color dict for consistent logic


class Alphabet:
    """currently supports Unicode through 255"""
    # string id: unique byteID -> stringID using set_id()
    def __init__(self):
        self.id = self.set_id()
        self.colorDict = self.makeColorFull()
        # we won't create a Color Object until a unicode char is used
        self.histDict = dict()  # letters used
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

    # needs reworking, flawed logic
    # no iterations with empty list,
    # so no letters added
    # def add_letter(self, char):
    #     for lttr in self.usedLetters:
    #        if ord(char) != lttr.uniLetter:
    #            newLetter = Letter(char)
    #            self.usedLetters.append(newLetter)
    #            self.mixer(newLetter)
    #        else:
    #            # send to mixer *twice*
    #            self.mixer(lttr)
    #            self.mixer(lttr)

    # takes a new letter
    # adds its given rgb values, divides by two
    # in order to mix with alphabet current color
    def mixer(self, newLetter):
        self.avgColor[0] = (self.avgColor[0] + newLetter.color.red) / 2
        self.avgColor[1] = (self.avgColor[1] + newLetter.color.green) / 2
        self.avgColor[2] = (self.avgColor[2] + newLetter.color.blue) / 2

    def __str__(self):
        return str(self.colorDict)

    # generates {unicode: RGB} dictionary for 0-255 unicode characters
    # ACCEPTS an alphabet instance
    def makeColorFull(self):
        colorFull = {uni: None for uni in range(256)}
        for uni in colorFull:
            randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            while randColor in colorFull.values():
                randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                if randColor not in colorFull.values():
                    break
            colorFull[uni] = randColor
        return colorFull

    # adds unicode integer and RGB color to colordict
    # to extend beyond 0-255
    # based on user input
    # ACCEPTS an alphabet instance and ord("char"):int
    def addUni(self, uni:int):
        if uni not in self.colorDict:
            randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            while randColor in self.colorDict.values():
                randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                if randColor not in self.colorDict.values():
                    break
            self.colorDict[uni] = randColor


