# Create a MusicPlayer class and subclass Spotify to override play method.

# Base class
class MusicPlayer:
    def __init__(self, device):
        self.device = device

    def play(self, song):
        print(f"[{self.device}]  is Playing '{song}' from local storage.")


# Subclass Spotify inheriting from MusicPlayer
class Spotify(MusicPlayer):
    def play(self, song):
        print(f"[{self.device}]  is Streaming '{song}' online on Spotify.")


# Create objects
player = MusicPlayer("MP3 Player")
spotify = Spotify("Smartphone")

# Demonstrate basic player
print("--- Basic Music Player ---")
player.play("Shape of You")


print("\n--- Spotify Player ---")
spotify.play("Starboy")
