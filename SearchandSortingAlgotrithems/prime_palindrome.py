import logging

logging.basicConfig(filename='prime_palindrome.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def palindromic_prime(n):
    try:
        reverse = int(str(n)[::-1])
        if n == reverse:
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        logging.debug(" it is not a prime number, also not palindrome number! {} ".format(n))
                        break
                else:
                    logging.debug("This is a prime and palindrome number!")
        else:
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        logging.debug(n, " This is not a prime and not a palindrome number.")
                        break
                else:
                    logging.debug("This is a prime number but not a palindrome number!")
    except Exception as e:
        logging.debug(e)
    finally:
        print("closed")


if __name__ == '__main__':
    n = int(input("enter the number You want to find"))
    palindromic_prime(n)
