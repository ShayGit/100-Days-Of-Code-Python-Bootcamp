import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "SPOTIFY_ID"
SPOTIFY_SECRET = "SPOTIFY_SECRET"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
year = date.split('-')[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text,"html.parser")

songs_elements = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
songs_titles = [song.getText() for song in songs_elements]
print(songs_titles)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               cache_path=".cache",
                                               redirect_uri="http://example.com",
                                               scope="user-library-read playlist-modify-private"))

tracks_query = [f"track:{name} year:{year}" for name in songs_titles]
song_uris = []

for query in tracks_query:
    result = sp.search(query, type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{query} not available")


playlist = sp.user_playlist_create(sp.current_user()["id"], f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
print(sp.user_playlists(user=sp.current_user()["id"]))