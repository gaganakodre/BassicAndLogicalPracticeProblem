import math


def perfect_number(num):
    result_1 = math.pow(2, num-1)
    result_2 = math.pow(2, num)-1
    perfect_num = result_1*result_2
    if perfect_num == 6 or 28 or 496:
        print("it's a perfect number")


if __name__ == '__main__':
    n = int(input("enter the number below 5 to check the perfect number "))
    perfect_number(n)

