import numpy as np
from PIL import Image
from image_tools import image_processing
import time
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

def image_processing_in_python(image):
    output = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] > 500:
                output[i][j] = 2 * image[i][j]
            else:
                output[i][j] = 8 * image[i][j]
    return output

def main():
    avg_time = []
    cycle = 11 # lowest is 2
    for run in range(cycle):
        photo_filepath = "esa_photo.tiff"
        time_start_c = time.time()
        image = read_png_file(photo_filepath)[:,:,0]
        image_processed = image_processing(image)
        np.save("processed_image", image_processed)
        time_end_c = time.time()
        avg_time.append(time_end_c - time_start_c)
    print(f"Avg cython time for {cycle - 1} runs: {np.mean(avg_time)}")
    avg_time = []
    for run in range(cycle):
        photo_filepath = "esa_photo.tiff"
        time_start_py = time.time()
        image = read_png_file(photo_filepath)[:,:,0]
        image_processed = image_processing_in_python(image)
        np.save("processed_image", image_processed)
        time_end_py = time.time()
        avg_time.append(time_end_py - time_start_py)
    print(f"Avg python time for {cycle -1} runs: {np.mean(avg_time)}")

if __name__ == "__main__":
    main()