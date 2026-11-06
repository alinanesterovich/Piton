import math


def square(side):
    area = side * side
    if area == int(area):
        return int(area)
    return math.ceil(area)


result = square(3.2)
print(result)
