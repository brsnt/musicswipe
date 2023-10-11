import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#MIKE DIMES ARTIST CODE
lz_uri = 'spotify:artist:6rIaHuCIUu32uj2CjlEBN3'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
    
    #use spotipy
