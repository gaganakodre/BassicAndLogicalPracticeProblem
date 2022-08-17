def swap_numbers(num1_, num2_):
    if num1_ != 0:
        num1_ = num1_ + num2_
        num2_ = num1_ - num2
        num1_ = num1_ - num2_
        print(num1_, num2_)


if __name__ == '__main__':
    num1 = int(input("enter the number for first swapping "))
    num2 = int(input("enter the number for second swapping "))
    swap_numbers(num1, num2)
