import pytest
from lib.count_words import *

# Check that we are being given a string
def test_to_see_if_being_given_a_string():
    with pytest.raises(Exception) as e:
        count_words(1234)
    error = str(e.value)
    assert error == "Text must be a string"

# Making sure the user doesn't pass an empty string
def test_check_string_is_not_empty():
    with pytest.raises(Exception) as e:
        count_words("")
    error = str(e.value)
    assert error == "Cannot use an empty string!"

# Test to see we are getting back the correct number of words
def test_to_check_correct_number_of_words():
    num_words = count_words("This is a test to count the words")
    assert num_words == 8
    