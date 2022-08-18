import logging

logging.basicConfig(filename='pallindrome.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def palindrome(num):
    """
    Function to implement the palindrome
    """
    try:
        val = int(num)
        if num == str(num)[::-1]:
            logging.debug('The given number is PALINDROME')
        else:
            logging.debug('The given number is NOT a palindrome')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    num = input('Enter any number : ')
    palindrome(num)
