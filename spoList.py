import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import time
import json

config = open("config.json")
data = json.load(config)

auth_manager = SpotifyClientCredentials(
    client_id= data["ID"], 
    client_secret= data["SECRET"])
sp = spotipy.Spotify(auth_manager=auth_manager)

playlistURL = input("Playlist URL'ini giriniz: ")
playlistUserURL = input("Playlist sahibinin URL'ini giriniz: ")

def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist["tracks"]["items"]:
        track = item["track"]
        track_ids.append(track["id"])
    return track_ids

track_ids = getTrackIDs(playlistUserURL, playlistURL)

def getTrackArtist(id):
    track_info = sp.track(id)
    artist = track_info["album"]["artists"][0]["name"]
    return artist
black_list = ["Sanatçı İsmi 1", "Sanatçı İsmi 2", "Sanatçı İsmi 3"] #İstediğiniz kadar sanatçı eklenebilir
for i in range(len(track_ids)):
    time.sleep(.3)
    track_artist = getTrackArtist(track_ids[i])
    for j in black_list:
        if track_artist == j:
            print("\nBu playlist dinlenmez")
            exit()
