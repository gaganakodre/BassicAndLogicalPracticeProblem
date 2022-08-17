def harmonic_series(number_):
    try:
        result_harmonic = 0.0

        for i in range(1, number_ + 1):
            result_harmonic = result_harmonic + 1 / i

        return result_harmonic
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    number = int(input("enter the number "))
    print(round(harmonic_series(number), 6))

