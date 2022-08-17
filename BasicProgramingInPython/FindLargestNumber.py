def largest_number(num1_, num2_, num3_):
    if num1_ > num2_:

        if num1_ > num3_:
            print(num1_, "is the largest number")
        else:
            print(num3_, "is the largest number")
    elif num2_ > num3_:
        print(num2_, "num2 is largest number")
    else:
        print(num3_, "is the largest number")


if __name__ == '__main__':
    num1, num2, num3 = input("enter the first number ").split()
    largest_number(num1, num2, num3)
