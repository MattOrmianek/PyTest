import pytest

from app import letter_value, calculating_sum_of_word

def test_letter_value():
    assert letter_value('a') == 1

def use_case_letter_value():
    assert letter_value('z') == 26

def use_case_type_check_letter_value():
    assert type(letter_value('z')) == int

def edge_case_letter_value():
    with pytest.raises(ValueError):
        letter_value('!')

def edge_case_letter_value():
    with pytest.raises(ValueError):
        letter_value('!')

def test_sum_of_word():
    assert calculating_sum_of_word('abc') == 6

def use_case_sum_of_word():
    assert calculating_sum_of_word('apple') == 50

def edge_case_sum_of_word():
    with pytest.raises(ValueError):
        calculating_sum_of_word('!')

def use_case_type_check_sum_of_word():
    assert type(calculating_sum_of_word('apple')) == int

