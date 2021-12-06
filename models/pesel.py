import random

year = random.randint(1901, 1998)
month = random.randint(9, 11)
day = random.randint(9, 30)
five_numer = random.randint(10000, 99998)

pesel = f'{year}' + f'{month}' + f'{day}' + f'{five_numer}'

print(pesel)

