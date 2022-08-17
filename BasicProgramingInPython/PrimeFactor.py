def prime_factor(number_):
    for i in range(2, number_+1):
        if number_ % i == 0:
            print(i)

    return i


if __name__ == '__main__':
    number = int(input("enter the number you want to find the prime factors "))
    prime_factor(number)
