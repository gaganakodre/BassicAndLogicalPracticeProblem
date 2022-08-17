def addition(a_, b_):
    c = a_ + b_
    print('add: ', c)


def Subtraction(a_, b_):
    c = a_ - b_
    print('sub: ', c)


def multiplication(a_, b_):
    c = a_ * b_
    print('mul: ', c)


def division(a_, b_):
    c = a_ / b_
    print('div: ', c)


if __name__ == '__main__':
    a = int(input("enter the number "))
    b = int(input("enter the number "))
    try:
        print("resource opened")
        addition(a, b)
        Subtraction(a, b)
        multiplication(a, b)
        division(a, b)
    except ZeroDivisionError as e:
        print("some error occurred please entre the parameter in correct way", e)

    except ValueError as e:
        print("Invalid input ", e)

    except Exception as e:
        print("something went wrong")

    finally:
        print("resource closed")


