import math


def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(math.ceil(number_of_cans))


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(test_h, test_w, coverage)
