# Import packages

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Set client ID, client secret, and redirect URI as environment variables

    # In terminal write: export SPOTIPY_CLIENT_ID='my client id'
        # To check this, type: echo $SPOTIPY_CLIENT_ID
    # Do the same for the client secret: export SPOTIPY_CLIENT_SECRET='my client secret'
        # To check this, type: echo $SPOTIPY_CLIENT_SECRET
    # Do the same for redirect URI: export SPOTIPY_REDIRECT_URI='my redirect uri'
        # To check this, type: echo $SPOTIPY_REDIRECT_URI

cid = 'my client id'
secret = 'my client secret'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

# Connect spotify variable to my credentials and authorization

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
scope = "user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
auth_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(auth_manager=auth_manager)

########## Return dijon's albums (for just singles, add "album_types='singles'"" in the parentheses directly below)

"""
dijon_uri = 'spotify:artist:0knGpCTbmG4ctl1wzYRZs4'

results = spotify.artist_albums(dijon_uri)
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
"""

########## Print the playlists on my Spotify account

"""
user = spotify.user('31ow4u7cgcrkckqyfp4ulsyxvbri')
playlists = spotify.user_playlists('31ow4u7cgcrkckqyfp4ulsyxvbri')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None
"""

########## Print the playlists on my old Spotify account

"""
user = spotify.user('gerock2')
playlists = spotify.user_playlists('gerock2')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None
"""

# or without the numbered list or URI

"""
user = spotify.user('gerock2')
playlists = spotify.user_playlists('gerock2')
for playlist in playlists['items']:
    print(playlist['name'])
"""