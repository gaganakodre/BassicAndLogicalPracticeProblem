import math


def power_of_two(number_):
    x = 0

    while x <= number_:
        x += 1
        print(math.pow(2, x))


if __name__ == '__main__':
    number = int(input("enter th power of 2 number You want to find "))
    power_of_two(number)

