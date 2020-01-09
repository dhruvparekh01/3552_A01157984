import math


def calculate_hypotenuse(a, b):
    h = math.sqrt(a**2 + b**2)
    return h


if __name__ == '__main__':
    s1 = float(input('Enter a: '))
    s2 = float(input('Enter b: '))
    s3 = calculate_hypotenuse(s1, s2)
    print('Hypotenuse =', s3)

