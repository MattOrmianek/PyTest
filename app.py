

def letter_value(letter: str) -> int:
    try:
        return 'abcdefghijklmnopqrstuvwxyz'.index(letter) + 1
    except ValueError:
        return "ValueError"

def calculating_sum_of_word(word: str) -> int:
    try:
        return sum([letter_value(letter) for letter in word])
    except ValueError:
        return "ValueError"



def main():
    # reading file
    # saving to npz file
    # loading npz file
    # changing values in C in that picture
    # saving to png file

if __name__ == "__main__":
    main()