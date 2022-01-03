import random

men = 5

pesel_list = []

for m in range(men):
    year = random.randint(1901, 1998)
    month = random.randint(10, 11)
    day = random.randint(10, 30)
    five_numer = random.randint(10000, 99998)
    two_numer = random.randint(10, 98)
    one_no = random.randint(0, 8)
    even_number = random.choice([2, 4, 6, 8])
    odd_number = random.choice([1, 3, 5, 7, 9])
    pesel_for_men = f'{year}' + f'{month}' + f'{day}' + f'{two_numer}' + f'{one_no}' + f'{odd_number}' + f'{one_no}'
    pesel_list.append({'pesel_for_men': pesel_for_men})


for person_pesel in pesel_list:
    print("{pesel_for_men}".format(**person_pesel))
