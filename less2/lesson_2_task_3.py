import math

def square(side):
    if isinstance(side, int):
        return side * side
    elif isinstance(side, float):
        return math.ceil(side * side)
    else:
        raise ValueError("Side length should be a number.")
side_length = 3.5
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равна {area}")