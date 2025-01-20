import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "7e0441ccf5d94c53a509c175f47b6aa2"
client_secret = "aef2adaec82b47c08194ffcd5c668d58"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="yanendra_jha",
    )
)

# Getting the date as user input
date = (input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD format:"))
(print(date))
year = date.split("-")[0]
print(year)

#
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
songs_data = response.text

soup = BeautifulSoup(songs_data, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

user_id = sp.current_user()["id"]
print(user_id)

# Solving the getting songs uri part
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)