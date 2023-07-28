from test_framework import generic_test

import math

def power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0:
        x, power = 1.0 / x, -power
    while power:
        if power & 1:
            result *= x
        power, x = power >> 1, x * x
    return result 


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
