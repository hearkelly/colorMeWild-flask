
class Name:
    """a pythonic solution to colorName.js"""

    def __init__(self, aName: str):
        self.chars = aName.strip()
        self.names = self.parse(self.chars)
        self.qChars = {char for name in self.names for char in name}

    def parse(self, chars):
        if "\"" in chars:
            nameList = chars.split("\"")
            nameList = [name.strip() for name in nameList if len(name) >= 1]
            return nameList
        else:
            return chars.split()

