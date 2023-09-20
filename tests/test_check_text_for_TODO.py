import pytest
from lib.check_text_for_TODO import * 

"""
Test to see if text parameter is of string data type
return an error if not
"""

def test_for_string_type_in_TODO_text():
    error = check_for_TODO(1234)
    assert error == "Text must be of string data type."


"""
Test to see if function is being passed an empty string
return an error informing user the text can't be empty
"""

def test_for_empty_string_in_TODO():
    empty_string = check_for_TODO("")
    assert empty_string == "Text cannot be an empty string."


# """
# Test to check a text without #TODO
# return False
# """

def test_without_TODO():
    assert check_for_TODO("this does not have todo") == False


"""
Test to see if there is TODO without #
return False
"""
def test_without_hashtag():
    assert check_for_TODO("TODO TODO TODO TODO ##") == False


"""
Test to see if there is #TODO
return True
"""

def test_for_hashtagTODO_in_text():
    assert check_for_TODO("This text will return True #TODO nice") == True

"""
Test to accept lowercase todo following a hashtag
return bool value of True
"""

def test_for_lower_todo():
    assert check_for_TODO("#todo") == True

