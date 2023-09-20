1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

def check_for_TODO():
    Parameters: 
        string text (maybe a list but come back)
    return Value:
        Bool value of either True or False, depending on if there #TODO is in the text
    Side effects:



3. Create Examples as Tests

Make a list of examples of what the function will take and return.

<!-- """
Test to see if text parameter is of string data type
return an error if not
"""

def test_for_string_type_in_TODO_text():
    return an error instructing the user to pass a string text to the function. -->


"""
Test to see if function is being passed an empty string
return an error informing user the text can't be empty
"""

def test_for_empty_string_in_TODO(""):
    return an error "String text cannot be empty."


"""
Test to check a text without #TODO
return False
"""

def test_without_TODO():
    return False

"""
Test to see if there is TODO without #
return False
"""

"""
Test to see if there is #TODO
return True
"""



Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
