def add(x, y=8):
    print(x + y)


add(5)

default_y = 3


def add2(x, y=default_y):
    sum = x + y
    print(sum)


add2(2)

add2(2, 8)
