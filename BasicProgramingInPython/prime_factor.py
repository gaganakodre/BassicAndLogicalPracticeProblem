def prime_factor(number_):
    try:
        for i in range(2, number_ + 1):
            if number_ % i == 0:
                print(i)

        return i
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    number = int(input("enter the number you want to find the prime factors "))
    prime_factor(number)
