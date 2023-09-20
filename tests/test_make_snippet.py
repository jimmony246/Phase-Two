import pytest
from lib.make_snippet import *

# Make sure we're returning a string
def test_to_return_a_string():
    test = make_snippet("")
    assert test == ""

# Given an argument (string) of 4 words, return the same string. 
def test_to_return_4_words():
    four_words = make_snippet("Hello how are you?")
    assert four_words == "Hello how are you?"

# Now need to return a ... after five words in a string
def test_to_return_ellipsis_after_five_words():
    longer_text = make_snippet("Hello, how are you? I am very well thanks!")
    assert longer_text == "Hello, how are you? I..."