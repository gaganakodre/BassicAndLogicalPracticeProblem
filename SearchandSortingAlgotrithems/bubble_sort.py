import logging

logging.basicConfig(filename='bubble_sort.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def bubble_sort(arr_):
    try:
        swapped = False
        for n in range(len(arr_) - 1, 0, -1):
            for i in range(n):
                if arr_[i] > arr_[i + 1]:
                    swapped = True
                    arr_[i], arr_[i + 1] = arr_[i + 1], arr_[i]
            if not swapped:
                return

    except Exception as e:
        logging.exception(e)

    finally:
        print("closed")


if __name__ == '__main__':
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    logging.debug("Unsorted list is,")
    logging.debug(arr)
    bubble_sort(arr)
    logging.debug("Sorted Array is, ")
    logging.debug(arr)
