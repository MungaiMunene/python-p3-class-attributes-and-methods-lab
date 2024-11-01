class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.add_song_to_count()

        # Add genre and artist to class-level lists and dictionaries
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Ensure genre is added only once
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Ensure artist is added only once
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Update genre count dictionary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Update artist count dictionary
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
if __name__ == "__main__":
    # Create example instances to check the implementation
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("Hotline Bling", "Drake", "Rap")

    # Print statements to verify results
    print("Total songs:", Song.count)           # Expected: 3
    print("Artists:", Song.artists)             # Expected: ['Jay-Z', 'Beyonce', 'Drake']
    print("Genres:", Song.genres)               # Expected: ['Rap', 'Pop']
    print("Genre count:", Song.genre_count)     # Expected: {'Rap': 2, 'Pop': 1}
    print("Artist count:", Song.artist_count)   # Expected: {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}