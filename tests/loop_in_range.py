def test_loop_range_3():
    for i in range(3):
        print(i)


def test_loop_range_form_10_0_minus_2():
    for i in range(10, 0, -2):
        print(i)


def test_loop_range_5_8_square():
    for i in range(5, 8):
        print(i, i ** 2)
    print('end of loop')


def test_loop_range_square():
    for i in range(2 ** 2):
        print('Hello, world!')


def test_character_hello():
    for character in 'hello':
        print(character)
