def quotient_remainder(dividend_, divisor_):
    try:
        quotient = dividend_ / divisor_
        remainder = dividend_ % divisor_
        print(float(quotient), float(remainder))
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    dividend = int(input("enter the dividend "))
    divisor = int(input("enter the divisor "))
    quotient_remainder(dividend, divisor)
