import pytest
import numpy as np
from image_tools import image_processing
from app import read_png_file

def test_use_case_one():
    photo_test_filepath = "test_first.tif"
    image = read_png_file(photo_test_filepath)[:,:,0]
    image_processed = image_processing(image)
    assert image_processed.shape == (12, 12)

def test_use_case_two():
    photo_test_filepath = "test_first.tif"
    image = read_png_file(photo_test_filepath)[:,:,0]
    image_processed = image_processing(image)
    sum_array = []
    for i in range(image_processed.shape[0]):
        for j in range(image_processed.shape[1]):
            sum_array.append(image_processed[i][j])
    assert np.sum(sum_array) == 0

def test_use_case_three():
    photo_test_filepath = "test_second.tif" #all white
    image = read_png_file(photo_test_filepath)[:,:,0]
    image_processed = image_processing(image)
    sum_array = []
    for i in range(image_processed.shape[0]):
        for j in range(image_processed.shape[1]):
            sum_array.append(image_processed[i][j])
    assert np.sum(sum_array) == image.shape[0] * image.shape[1] * 254