import pytest
import numpy as np
from PIL import Image

from app import letter_value, calculating_sum_of_word, read_png_file

def test_letter_value():
    assert letter_value('a') == 1

def test_use_case_letter_value():
    assert letter_value('z') == 26

def test_use_case_type_check_letter_value():
    assert type(letter_value('z')) == int

def test_edge_case_letter_value():
    with pytest.raises(ValueError):
        letter_value('!')

def test_edge_case_letter_value():
    with pytest.raises(ValueError):
        letter_value('!')

def test_sum_of_word():
    assert calculating_sum_of_word('abc') == 6

def test_use_case_sum_of_word():
    assert calculating_sum_of_word('apple') == 50

def test_edge_case_sum_of_word():
    with pytest.raises(ValueError):
        calculating_sum_of_word('!')

def test_use_case_type_check_sum_of_word():
    assert type(calculating_sum_of_word('apple')) == int

def test_read_png_file_use_case():
    file = "test_first.tif"
    assert type(read_png_file(file)) == type(np.array(Image.open(file)))

def test_read_png_file_filenotfounderror():
    file = "not_existing_file.tif"
    assert read_png_file(file) == "FileNotFoundError"