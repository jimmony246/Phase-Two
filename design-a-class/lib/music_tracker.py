class SongTracker():
    def __init__(self):
        self.song_tracks = []


    def add_song(self, name_of_song):
        #Parameters: self, song title in string format 
        #Returns: Nothing
        #Side-effects: It appends the list of tracks 
        if type(name_of_song) != str:
            raise Exception("Name of song must be in string format.")
        elif name_of_song == "":
            raise Exception("Song name cannot be an empty string.")
        self.song_tracks.append(name_of_song)

    def song_list(self):
    #Parameters: None
    #Returns: List of songs that have been added
    #Side-effects: None
        return self.song_tracks