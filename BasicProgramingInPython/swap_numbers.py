def swap_numbers(num1_, num2_):
    try:
        if num1_ != 0:
            num1_ = num1_ + num2_
            num2_ = num1_ - num2
            num1_ = num1_ - num2_
            print(num1_, num2_)

    except Exception as e:
        print(e)
    finally:
        print("closed")



if __name__ == '__main__':
    num1 = int(input("enter the number for first swapping "))
    num2 = int(input("enter the number for second swapping "))
    swap_numbers(num1, num2)
