
def prime_number_range(a_, b_):
    try:
        for n in range(a_, b_):
            for x in range(a_, n):

                if n % x == 0:
                    print(n, 'equals', x, '*', n // x, "not prime number")
                    break
            else:
                print(n, 'is a prime number')
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    a = int(input("enter the range "))
    b = int(input("enter the range2 "))
    prime_number_range(a, b)
