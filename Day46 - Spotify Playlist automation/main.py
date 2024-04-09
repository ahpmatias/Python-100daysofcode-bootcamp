import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USER_ID = os.environ.get('SPOTIFY_USER_ID')

sp_scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=sp_scope, client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri='http://example.com'))

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(BILLBOARD_URL + date)
billboard_website_html = response.text
soup = BeautifulSoup(billboard_website_html, 'html.parser')

titles_list = [title.getText() for title in soup.select('li ul li h3')]
stripped_titles_list = []
for item in titles_list:
    stripped_titles_list.append(item.strip())

song_uris = []
year = date.split("-")[0]
for song in stripped_titles_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.user_playlist_create(user=SPOTIFY_USER_ID, name=f'{date} Billboard 100', public=False, collaborative=False)
playlist_id = '3aQpsFum6NNgbuf2s95mV6'

sp.user_playlist_add_tracks(user=SPOTIFY_USER_ID, playlist_id=playlist_id, tracks=song_uris)



