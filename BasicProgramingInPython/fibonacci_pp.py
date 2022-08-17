def fibonacci(a_, b_):
    try:
        while a_ < 10:
            print(a_, end=',')  # The keyword argument end can be used to avoid
            # the newline after the output, or end the output with a different string:
            _a, _b = _b, _a + _b

    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    a, b = 0, 1
    fibonacci(a, b)
