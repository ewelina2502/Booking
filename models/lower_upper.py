import random
import string

random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
prefix_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
example_name = ''.join(random.choices(string.ascii_uppercase, k=1)) + \
               ''.join(random.choices(string.ascii_lowercase, k=5))

print(example_name)
