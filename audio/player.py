"""
vlc module to pause, resume, next track, previous track, seek, get position.
"""
import time
import vlc

class Player:
    def __init__(self):
        self.vlc.media_player_new()
        self.current_index = 0
        self.volume = 60
        self.mute = False
        self.shuffle = False
        self.repeat = False

    def queue_track(self, track_path):
        pass

    def load_playlist(self, playlist):
        pass

    def load_track(self, track_path):
        media = self.

    def play(self, track_path):
        
    
    def pause(self):
        pass

    def resume(self):
        pass

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








