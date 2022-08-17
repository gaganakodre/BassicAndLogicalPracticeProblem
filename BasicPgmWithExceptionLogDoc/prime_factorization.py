import logging

logging.basicConfig(filename='prime_factorization.log', level='DEBUG',
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def prime_factor(number_):
    """
    Function to write the prime factors for given number
    """
    try:
        for i in range(2, number_ + 1):
            if number_ % i == 0:
                logging.debug('prime factors: {}'.format(i))

        return i
    except Exception as e:
        print(e)
    finally:
        print("closed")


print(prime_factor.__doc__)
if __name__ == '__main__':
    number = int(input("enter the number you want to find the prime factors "))
    prime_factor(number)