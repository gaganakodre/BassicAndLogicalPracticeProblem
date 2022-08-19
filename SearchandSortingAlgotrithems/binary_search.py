import logging

logging.basicConfig(filename='binarysearch_algorithem.log',level='DEBUG',format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def binary_search(arr_, x_):
    """
    The function is used to implement the binary search
    """
    try:
        left = 0
        right = len(arr_)

        while left <= right:
            mid = left + ((right - left) // 2)

            result = (x_ == arr_[mid])

            if result == 0:
                return mid - 1

            if result > 0:
                left = mid + 1

            else:
                right = mid - 1

        return -1

    except Exception as e:
        logging.error(e)

    finally:
        print("closed")


if __name__ == '__main__':
    arr = ['apple', 'banana', 'grapes', 'orange']
    x = 'grapes'
    res = binary_search(arr, x)
    if res == -1:
        logging.debug("element not found")
    else:
        logging.debug("element  present at the index : {}".format(res))

    help(binary_search)
