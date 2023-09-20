import pytest
from lib.estimate_reading_time import *

"""
If given an empty string text
return an error that tells the user you cannot have an empty text.
"""
def test_time_reading_estimate():
    with pytest.raises(Exception) as e:
        time_reading_estimate("")
    error = str(e.value)
    assert error == "You cannot give an empty text!"


"""
If given a data type other than string
Throw an error that tells the user the text must be in string format
"""
def test_if_not_string():
    with pytest.raises(Exception) as e:
        time_reading_estimate(1234)
    error = str(e.value)
    assert error == "Text must be in string format."


"""
If passed a text of 200 words
return 1.0 representing minutes to read the text
"""
def test_time_reading_estimate_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = time_reading_estimate(text)
    assert result == 1.0


"""
If passed a text of 300 words
return a float value of 1.5
"""
def test_time_reading_estimate_300_words():
    text = " ".join(["word" for i in range(0, 300)])
    result = time_reading_estimate(text)
    assert result == 1.5