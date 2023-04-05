import numpy as np
from PIL import Image
from image_tools import image_processing

def letter_value(letter: str):
    try:
        return 'abcdefghijklmnopqrstuvwxyz'.index(letter) + 1
    except ValueError:
        raise ValueError

def calculating_sum_of_word(word: str):
    try:
        return sum([letter_value(letter) for letter in word])
    except ValueError:
        raise ValueError

def read_png_file(filepath: str):
    try:
        return np.array(Image.open(filepath))
    except FileNotFoundError:
        return "FileNotFoundError"


def main():
    photo_filepath = "esa_photo.tiff"
    image = read_png_file(photo_filepath)[:,:,0]
    image_processed = image_processing(image)
    np.save("processed_image", image_processed)

if __name__ == "__main__":
    main()
