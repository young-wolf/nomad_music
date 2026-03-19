"""
vlc module to pause, resume, next track, previous track, seek, get position.
"""
import time
import vlc
from pathlib import Path
import playlist_loader

class Player:

    def __init__(self):

        self._instance = vlc.Instance('--no-video')
        self._player = self._instance.media_player_new()
        self.current_index = 0
        self.volume = 60
        self.mute = False
        self.shuffle = False
        self.repeat = False

    def load_library(self) -> dict:

        playlist_loader.load_music_library()
        library_dict = {track.name: track for track in playlist_loader.music_library}
        print(library_dict)

        return library_dict
    def load_playlist(self, playlist):
        pass

    def load_track(self, track_path):

        media = self._instance.media_new(track_path)
        self._player.set_media(media)
        print("Track loaded: ", track_path)

    def play(self, track_path):

        self._player.play()
        print("Playing track: ", track_path)
    
    def pause(self):

        self._player.pause()
        print("Track paused")

    def resume(self):

        self._player.play()
        print("Track resumed")

    def next_track(self):
        pass

    def previous_track(self):
        pass

    def seek(self, position):
        pass

    def get_position(self):
        pass

    def set_volume(self, volume):
        pass

    def set_mute(self, mute):
        pass

    def toggle_shuffle(self):
        pass

    def toggle_repeat(self):
        pass

    def get_status(self) -> dict:
        # returns everything the UI needs in one call:
        # current track, position, duration, volume, is_playing, shuffle, etc.
        pass

my_player = Player()

"""
Temporary music path for testing
"""
track_path = Path('./music/Ill Faith Records - Be A Witness (Ft. Shakewell).mp3')
print(track_path.name)

"""
Call class functions for testing. Remove when done
"""

my_player.load_library()

my_player.load_track(track_path.name)




