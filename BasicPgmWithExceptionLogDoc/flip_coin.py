import random
import logging

logging.basicConfig(filename='flip_coin.log', level='DEBUG',
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def flip_fun(number_of_flips_):
    """
    The function to calculate percentage of head and tail
    """
    try:
        head = 0
        tail = 0

        while number_of_flips_ <= 10:
            randon_flip = random.randint(0, 1)
            number_of_flips_ += 1

            if randon_flip == 1:
                head += 1
                continue
            else:
                tail += 1
            head_percentage = head * 100 / number_of_flips_
            tail_percentage = tail * 100 / number_of_flips_
        logging.debug('Head percentage: {} '.format(head_percentage))
        logging.debug('tail percentage: {} '.format(tail_percentage))
        # print('tail percentage', tail_percentage)
    except Exception as e:
        print(e)
    finally:
        print("closed")


print(flip_fun.__doc__)
if __name__ == '__main__':
    number_of_flips = int(input("enter the number of times you want to flip "))
    flip_fun(number_of_flips)
