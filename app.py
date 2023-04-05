from PIL import Image

def letter_value(letter: str):
    try:
        return 'abcdefghijklmnopqrstuvwxyz'.index(letter) + 1
    except ValueError:
        return "ValueError"

def calculating_sum_of_word(word: str):
    try:
        return sum([letter_value(letter) for letter in word])
    except ValueError:
        return "ValueError"

def read_png_file(filepath: str):
    try:
        return Image.open(filepath)
    except FileNotFoundError:
        return "FileNotFoundError"


def main():
    # reading file
    photo_filepath = "esa_photo.tiff"
    image = read_png_file(photo_filepath)
    
    # changing values in C in that picture
    # saving to png file

if __name__ == "__main__":
    main()
