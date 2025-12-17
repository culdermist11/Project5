# Zadanie 6

import math

def pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    except:
        return "Błędne dane"


print(pole_trojkata(3, 4, 5))
