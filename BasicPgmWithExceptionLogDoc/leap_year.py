import logging

logging.basicConfig(filename='leap_year.log',level='INFO',
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def leap_year(year_):
    """
    Function to calculate the leap year
    :param (number) input entered  from the user year_:
    :return:the year if that is leap year
    """
    try:
        if year_ % 400 == 0 and (year % 100 == 0):
            # print(year_, "leap year")
            logging.info('Leap year: {}'.format(year_))
        elif year_ % 4 == 0 and year_ % 100 != 0:
            # print(year_, "leap year")
            logging.info('Leap year: {}'.format(year_))
        else:
            # print(year_, "not a leap year")
            logging.info(' not a Leap year: {}'.format(year_))
    except Exception as e:
        print(e)
    finally:
        print("closed")


print(leap_year.__doc__)
if __name__ == '__main__':
    year = int(input("enter the year u want to check "))
    leap_year(year)

