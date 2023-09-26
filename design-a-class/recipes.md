1. Describe the Problem

Put or write the user story here. Add any clarifying notes you might have:

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.




2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.


class SongTracker():
    def __init__(self):
    self.song_tracks = []


    def add_song(self, name_of_song)
    #Parameters: self, song title in string format 
    #Returns: Nothing
    #Side-effects: It appends the list of tracks 

    def song_list(self):
    #Parameters: None
    #Returns: List of songs that have been added
    #Side-effects: None



3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Test to make sure song name being passed 
is in string format
"""
def test_to_make_sure_song_name_is_a_string():
    => Raises an error if song name is not a string


"""
Need to test to ensure we are starting with empty list
"""
def test_to_see_empty_list_at_initialisation():
    => Return an empty list 


"""
We need to test that the add method
adds a song to the list of songs
"""
def test_add_appends_song_to_list_of_songs():
    => return the list of songs expecting the passed name to be added 


"""
Test a class method that returns the list of songs
added by the user
"""
def test_to_return_list_of_songs():
    => Return list of songs





Encode each example as a test. You can add to the above list as you go.
4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.