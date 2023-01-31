from alphabet import Alphabet
from color import Color
from letter import Letter

newLetter = Letter("M")
assert newLetter.uniLetter == ord("M")
# assert newLetter.uniLetter == ord("N")  # fail
print(newLetter.color)

mLetter = Letter("M")

assert mLetter == newLetter

mLowercase = Letter("m")
# assert mLowercase == mLetter *** M not equal to m ***

# our alphabet won't create a Letter instance
# if letter in alphabet list
print(mLetter.__dict__)
print(mLowercase.__dict__)
print(newLetter.__dict__)
