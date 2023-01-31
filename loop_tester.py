import random

dictionary = {x:None for x in range(0, 256)}
assert len(dictionary) == 256

for x in dictionary:
    num = random.randint(0, 10000000000)
    while num in dictionary.values():
        num = random.randint(0,1000000000)
        if num not in dictionary.values():
            break
    dictionary[x] = num

print(dictionary)
