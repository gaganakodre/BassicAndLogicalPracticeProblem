def reverse_number(num_):
    while num_ != 0:
        digit = num_ % 10
        reversed_num = reversed_num * 10 + digit
        num_ //= 10
    print("Reversed Number: " + str(reversed_num))


if __name__ == '__main__':
    num = int(input("enter number"))
    reverse_number(num)
