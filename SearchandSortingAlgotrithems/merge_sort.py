import logging

logging.basicConfig(filename='merge_sort.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def mergeSort(arr):
    try:
        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            mergeSort(L)

            # Sorting the second half
            mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    except Exception as e:
        logging.error(e)

    finally:
        print("closed")


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    logging.debug("Given array is".format(arr))
    logging.debug(arr)
    mergeSort(arr)
    logging.debug("Sorted array is: ".format(arr))
    logging.debug(arr)


