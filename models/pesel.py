import random

year = random.randint(1901, 1998)
month = random.randint(9, 11)
day = random.randint(9, 30)
five_numer = random.randint(10000, 99998)
two_numer = random.randint(10, 98)
one_no = random.randint(0, 8)
even_number = random.choice([2, 4, 6, 8])
odd_number = random.choice([1, 3, 5, 7, 9])


pesel_for_men = f'{year}' + f'{month}' + f'{day}' + f'{two_numer}' + f'{one_no}' + f'{odd_number}' + f'{one_no}'
pesel_for_women = f'{year}' + f'{month}' + f'{day}' + f'{two_numer}' + f'{one_no}' + f'{even_number}' + f'{one_no} '
pesel = f'{year}' + f'{month}' + f'{day}' + f'{five_numer}'

print(pesel_for_men)
print(pesel_for_women)
