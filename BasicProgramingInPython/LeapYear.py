def leap_year(year_):
    if year_ % 400 == 0 and (year % 100 == 0):
        print(year_, "leap year")
    elif year_ % 4 == 0 and year_ % 100 != 0:
        print(year_, "leap year")
    else:
        print(year_, "not a leap year")


if __name__ == '__main__':
    year = int(input("enter the year u want to check "))
    leap_year(year)

