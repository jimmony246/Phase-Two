1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


2. Design the Function Signature

    def time_reading_estimate(text):
        #Parameters:
            Here we have a string parameter called text which is going to represent the text the user is wanting to read
        #return:
            We want this function to return a value representing the time spent reading, a float? 


3. Create Examples as Tests

Make a list of examples of what the function will take and return.

"""
If given an empty string text
return an error that tells the user you cannot have an empty text.
"""
time_reading_estimate("")
    => "You cannot have an empty text!"


"""
If passed a text of 200 words
return 1.0 representing minutes to read the text
"""
time_reading_estimate(200 words):
    =>1.0


"""
If passed a text of 300 words
return a float value of 1.5
"""
time_reading_estimate(300 words)
    =>1.5



Encode each example as a test. You can add to the above list as you go.
4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

Ensure all test function names are unique, otherwise pytest will ignore them!