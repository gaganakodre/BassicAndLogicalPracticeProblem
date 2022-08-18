import logging

logging.basicConfig(filename='anagram.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def check(s1, s2):
    """
    Function to check the given string is anagram are not
    """
    try:
        if sorted(s1) == sorted(s2):
            logging.debug("The strings are anagrams.")
        else:
            logging.debug("The strings aren't anagrams.")

    except Exception as e:
        logging.exception(e)

    finally:
        print("closed")


if __name__ == '__main__':
    s1 = "heart"
    s2 = "earth"
    check(s1, s2)
