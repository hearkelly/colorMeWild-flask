from name import Name
from alphabet import Alphabet
import random

name = Name("\"Fannie Mae\" Branch")
secondName = Name("Justin Branch")
print(name.__doc__)
assert isinstance(name, Name)

print(name.chars)
print(secondName.chars)
print(name.names)
print(secondName.names)
unique = name.qChars
unique2 = secondName.qChars
print(unique, unique2)

newAlpha = Alphabet()
print(newAlpha.colorDict)
print(newAlpha.colorDict)
