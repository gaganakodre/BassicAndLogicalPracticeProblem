import math
import logging

logging.basicConfig(filename='power_of_2.log', level='DEBUG',
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def power_of_two(number_):
    """
    function to find the 2 power

    :param number_:
    :integer: integer values those are the powers of 2
    """
    try:
        x = 0

        while x <= number_:
            x += 1
            logging.debug('the values : {} '.format(math.pow(2, x)))
    except Exception as e:
        print(e)
    finally:
        print("closed")


print(power_of_two.__doc__)
if __name__ == '__main__':
    number = int(input("enter th power of 2 number You want to find "))
    power_of_two(number)

