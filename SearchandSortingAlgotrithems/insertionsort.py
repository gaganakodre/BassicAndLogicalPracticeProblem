import logging

logging.basicConfig(filename='insertionsort.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def insertionSort(arr_):
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

    # finally:
    #     print("closed")


if __name__ == '__main__':
    value="python"

    arr = [i for i in value]
    result=insertionSort(arr)
    lst = []
    logging.debug("Sorted array is : ")
    print(result)
    # for i in range(len(arr)):
    #     lst.append(arr[i])
    # logging.debug(lst)

