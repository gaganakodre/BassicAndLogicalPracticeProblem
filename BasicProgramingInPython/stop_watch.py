from datetime import datetime as dt


def stop_watch(number_):
    try:
        start_time = dt.now()
        print(start_time)
        if number_ == 1:
            stop_time = dt.now()
            print(stop_time)
            elapsed_time = stop_time - start_time
            print("elapsed Time: ", elapsed_time)
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    number = int(input("press 1  to stop time:"))
    stop_watch(number)
