import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID') # Client ID, as provided by the respective Spotify Developer Dashboard
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET') # Client Secret, as provided by the respective Spotify Developer Dashboard
SPOTIFY_USER_ID = os.environ.get('SPOTIFY_USER_ID') # The respective Spotify User ID, composed of only numbers

sp_scope = 'playlist-modify-private' # defined scope as per Spotify Web API doc - https://developer.spotify.com/documentation/web-api/concepts/scopes

# Create Spotify object, including authentication flow
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=sp_scope, client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri='http://example.com'))

# Web scrape date out of Billboard Webpage based on a specific date
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(BILLBOARD_URL + date)
billboard_website_html = response.text
soup = BeautifulSoup(billboard_website_html, 'html.parser')

# Generate list of top 100 songs out of Billboard Webpage HTML
titles_list = [title.getText() for title in soup.select('li ul li h3')]
stripped_titles_list = []
for item in titles_list:
    stripped_titles_list.append(item.strip())

# Generate the song URIs based on stripped_titles_list, which are required for querying through Spotify API
song_uris = []
year = date.split("-")[0]
for song in stripped_titles_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create Playlist through API call
sp.user_playlist_create(user=SPOTIFY_USER_ID, name=f'{date} Billboard 100', public=False, collaborative=False)
playlist_id = '3aQpsFum6NNgbuf2s95mV6'

# Update created playlist with all songs contained in stripped_titles_list, if available on Spotify
sp.user_playlist_add_tracks(user=SPOTIFY_USER_ID, playlist_id=playlist_id, tracks=song_uris)



