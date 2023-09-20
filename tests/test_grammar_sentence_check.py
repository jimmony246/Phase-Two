import pytest
from lib.grammar_sentence_check import * 

"""
Given a data type that isn't a string return an error
that tells the user it needs to be a string
"""

def test_if_text_is_string():
    error = grammar_check(1234)
    assert error == "Text needs to be of string data type."

"""
Given an empty string text return an error saying the text cannot be empty
"""
def test_grammar_with_empty_string():
    error = grammar_check("")
    assert error == "Text cannot be an empty string."

"""
Given a sentence with a fullstop but no capital letter
"""

def test_fullstop_no_capital():
    result = grammar_check("this is not a correct sentence.")
    assert result == False

"""
Given a sentence with a capital letter but no fullstop
"""
def test_capital_but_no_fullstop():
    result = grammar_check("This is an incorrect sentence")
    assert result == False


"""
Given a valid sentence with a capital letter and a fullstop
returns True
"""
def test_grammar_check_valid_sentence():
    result = grammar_check("This is a valid sentence.")
    assert result == True

"""
Given a sentence with a capital letter at first index
and an exclamation point at end return True
"""
def test_grammar_with_capital_and_exclamation_mark():
    result = grammar_check("This is also a valid sentence!")
    assert result == True


"""
Given a sentence with no capital letter but a question mark at the end
Return False
"""
def test_grammar_no_capital_with_exclamation():
    result = grammar_check("this ain't gonna work!")
    assert result == False

