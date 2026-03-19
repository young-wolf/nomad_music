from pathlib import Path

"""
Create a list of all songs in the music directory and its subdirectories and create a list.
In the future we will need to get the music directory from a config file.
Ideally we should use a music specific module to load playlists, possibly mutagen.
Also, playlist loader is not an accurate name anymore. We should rename it to music_library_loader or something similar.
"""

# For testing, get the music directory from a config file.
music_folder = Path('../music/')

# Create a list with all songs from music folder

def load_music_library() -> list:

    music_library = []

    for song in music_folder.rglob('*.mp3'):
        music_library.append(song)
        print(song.name)
    
    return music_library


