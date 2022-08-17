import math


def power_of_two(number_):
    try:
        x = 0

        while x <= number_:
            x += 1
            print(math.pow(2, x))
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    number = int(input("enter th power of 2 number You want to find "))
    power_of_two(number)

