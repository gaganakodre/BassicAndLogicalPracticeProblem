import random


def flip_fun(number_of_flips_):
    head = 0
    tail = 0

    while number_of_flips_ <= 10:
        randon_flip = random.randint(0, 1)
        number_of_flips_ += 1

        if randon_flip == 1:
            head += 1
            continue
        else:
            tail += 1
        head_percentage = head * 100 / number_of_flips_
        tail_percentage = tail * 100 / number_of_flips_
    print('Head percentage', head_percentage)
    print('tail percentage', tail_percentage)


if __name__ == '__main__':
    number_of_flips = int(input("enter the number of times you want to flip "))
    flip_fun(number_of_flips)

