def Sum(a, b):
    return a+b


def multiply(a, b):
    return a*b


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    finally:
        exit(0)


def subtract(a, b):
    return a-b


if __name__ == '__main__':
    try:
        n1 = int(input('Enter first number: '))
        n2 = int(input('Enter second number: '))

        temp = int(input('1 to add \n2 to subtract \n3 to multiply \n4 to divide \n'))

    except ValueError:
        print('Invalid value')

    finally:
        exit(0)

    if temp == 1:
        print(Sum(n1, n2))
    elif temp == 2:
        print(subtract(n1, n2))
    elif temp == 3:
        print(multiply(n1, n2))
    elif temp == 4:
        print(divide(n1, n2))
    else:
        print('Invalid number entered')


