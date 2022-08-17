import logging

logging.basicConfig(filename='harmonic_series.log', level='DEBUG',
                    format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def harmonic_series(number_):
    """
    Function to implement the harmonic series and to find the sum of it
    """
    try:
        result_harmonic = 0.0
        i = 1

        while i < number_:
            result_harmonic = result_harmonic + 1 / i
            i += 1
            logging.debug('harmonic sum: {} '.format(result_harmonic))

        return result_harmonic
    except Exception as e:
        print(e)
    finally:
        print("closed")


print(harmonic_series.__doc__)
if __name__ == '__main__':
    number = int(input("enter the number "))
    harmonic_series(number)
    # result = round(harmonic_series(number), 6)
    # logging.debug('Addition of series: {} '.format(result))
