
"""
This script is used to play music for the nomad-mp3 project
"""
import vlc
import time
from pathlib import Path
import random

p = Path('Music/')

def get_music_items(artist=None) -> list:

    if artist == None:
        items = []
        for item in p.iterdir():
            items.append(item.name)
            print(items[-1])

    else:
        items = []
        for item in p.rglob(f'{artist}/*'):
            items.append(item.name)
            print(items[-1], "\n")
            print("\t Track List ::\n")

            if items is not None:
                for track in p.rglob(f'{artist}/*/*'):
                    items.append(track.name)
                    print(f"\t \t{items[-1]}")
                    
    return items

def queue_track(user_selected_track):
    
    matches = p.rglob(f'{user_selected_track}')
    selected_path = next(matches, None)
    if selected_path:
        return str(selected_path)

    return None

def play_track():
    
    player = vlc.MediaPlayer(queue_track(user_selected_track))
    player.play()
    time.sleep(1) # Wait for the player to start

    while player.is_playing():
        time.sleep(1)

get_music_items()

selected_artist = input('\nPlease select an artist from the list above: ')
print(f"\nYou have selected :: {selected_artist}\n")

get_music_items(selected_artist)

user_selected_track = input("\n Please select a track from the list above: ")
