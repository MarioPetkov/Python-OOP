from project.song import Song


class Album:
    def __init__(self, name:str, *songs):
        self.name = name
        self.published = False
        self.songs = [songs]

    def add_song(self, song: Song):

        self.songs.append(song)
        return f"Song {song} has been added to the album {self.name}."