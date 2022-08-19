import logging


logging.basicConfig(filename='anagram.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def insertion_sort(arr_):
    """
    Function to implement the insertion sort
    """
    try:
        for i in range(1, len(arr_)):
            key = arr_[i]
            j = i - 1

            while j >= 0 and key < arr_[j]:
                (arr_[j + 1]) = arr_[j]
                j -= 1
            arr_[j + 1] = key
        return arr_
    except Exception as e:
        logging.exception(e)


def check(arr1_, arr2_):
    """
    Function to check the given string is anagram are not
    """
    try:
        if insertion_sort(arr1_) == insertion_sort(arr2_):
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
    arr1 = [i for i in s1]
    arr2 = [j for j in s2]
    check(arr1, arr2)


