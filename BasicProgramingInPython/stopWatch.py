from datetime import datetime as dt


def stop_watch(number_):
    start_time = dt.now()
    if number_ == 1:
        stop_time = dt.now()
        elapsed_time = stop_time - start_time
        print("elapsed Time: ", elapsed_time)


if __name__ == '__main__':
    number = int(input("press 1  to stop time:"))
    stop_watch(number)
