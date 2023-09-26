import pytest
from lib.music_tracker import * 

"""
Test to make sure song name being passed 
is in string format, throw error if not
"""
def test_to_make_sure_song_name_is_a_string():
    songs_i_like = SongTracker()
    with pytest.raises(Exception) as err:
            songs_i_like.add_song(1234)
    assert str(err.value) == "Name of song must be in string format."


"""
Need to test to ensure we are starting with empty list
"""
def test_to_see_empty_list_at_initialisation():
    songs_i_like = SongTracker()
    assert songs_i_like.song_tracks == []


"""
We need to test that the add method
adds a song to the list of songs
"""
def test_add_appends_song_to_list_of_songs():
    songs_i_like = SongTracker()
    songs_i_like.add_song("Five Years")
    assert songs_i_like.song_tracks == ["Five Years"]



"""
Test to see that we can add multiple songs
and have them appended to the list
"""
def test_for_multiple_songs_with_add():
    songs_i_like = SongTracker()
    songs_i_like.add_song("Five Years")
    songs_i_like.add_song("Sweet thing")
    songs_i_like.add_song("Dans l'univers")
    assert songs_i_like.song_tracks == ["Five Years", "Sweet thing", "Dans l'univers"]

"""
Test a class method that returns the list of songs
added by the user
"""
def test_to_return_list_of_songs():
    songs_i_like = SongTracker()
    songs_i_like.add_song("Five Years")
    songs_i_like.add_song("Sweet thing")
    songs_i_like.add_song("Dans l'univers")
    assert songs_i_like.song_list() == ["Five Years", "Sweet thing", "Dans l'univers"]


"""
Test for when User passes an empty song name
throw an error informing user it cannot be empty
"""
def test_for_empty_string():
    songs_i_like = SongTracker()
    with pytest.raises(Exception) as err:
        songs_i_like.add_song("")
    assert str(err.value) == "Song name cannot be an empty string."

# """
# Test for when user passes multiple song names
# with one call of add method
# """
# def test_for_multiple_songs_one_add():
#     songs_i_like = SongTracker()
#     songs_i_like.add_song("Five Years", "Sweet thing", "Dans l'univers")
#     assert songs_i_like.song_list() == ["Five Years", "Sweet thing", "Dans l'univers"]