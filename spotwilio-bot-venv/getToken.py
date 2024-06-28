import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
spotify_user = os.environ.get("SPOTIPY_CLIENT_USERNAME")
# print(spotify_user)
spotify_scope = "playlist-modify-private"
oauth = SpotifyOAuth(username=spotify_user, scope=spotify_scope)
user_token = oauth.get_access_token(as_dict=False)
# print(user_token)

spotify = spotipy.Spotify(auth=user_token)
api_results = spotify.search(q="Muse", type="artist")
print(api_results)