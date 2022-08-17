def quotient_remainder(dividend_, divisor_):
    quotient = dividend_ / divisor_
    remainder = dividend_ % divisor_
    print(float(quotient), float(remainder))


if __name__ == '__main__':
    dividend = int(input("enter the dividend "))
    divisor = int(input("enter the divisor "))
    quotient_remainder(dividend, divisor)
