def vowels_consonants(alphabets_):
    try:
        if alphabets_ == 'a':
            print("vowel")
        elif alphabets_ == 'e':
            print("vowel")
        elif alphabets_ == 'i':
            print("vowel")
        elif alphabets_ == 'o':
            print("vowel")
        elif alphabets_ == 'u':
            print("vowel")
        else:
            print("consonants")
    except Exception as e:
        print(e)
    finally:
        print("closed")


if __name__ == '__main__':
    alphabets = input("enter the alphabets ")
    vowels_consonants(alphabets)








