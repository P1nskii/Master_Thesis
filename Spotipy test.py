import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Your credentials
client_id = '2ce4e55ef2df4ef2966532686c370098'
client_secret = '6498a02ff7f74753835cc7549289d3d8'

# audio features for Creepin by Metro Boomin

# Set up client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Track ID (from your provided link)
track_id = '2dHHgzDwk4BJdRwy9uXhTO'

# Fetch the audio features
try:
    audio_features = sp.audio_features(track_id)
    print(audio_features)
except spotipy.exceptions.SpotifyException as e:
    print(f"An error occurred: {e}")


# https://open.spotify.com/track/7vggqxNKwd6xdRoYS0pQtM?si=348b0682261f4a8a
#
# https://open.spotify.com/track/75FYqcxt1YEAtqDLrOeIJn?si=76cebc554ac947f5
# Process the audio features as needed

# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
#
# # Your new credentials
# client_id = 'd4e2233e2d794bb48837a1f89ced1ff8'
# client_secret = '3bc5453bba07433b89ca6d6a45463fe8'
# redirect_uri = 'https://cursusplanner.uu.nl/course/ECB3OKVECO/2022/4'  # Your new Redirect URI
#
# # Set up OAuth
# scope = 'user-library-read'
# sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
# sp = spotipy.Spotify(auth_manager=sp_oauth)
#
# # Track ID
# track_id = '2dHHgzDwk4BJdRwy9uXhTO'
#
# # Fetch the audio features
# try:
#     audio_features = sp.audio_features(track_id)
#     print("Audio Features:", audio_features)
# except spotipy.exceptions.SpotifyException as e:
#     print(f"An error occurred: {e}")
#
# # Fetch available genre seeds
# try:
#     genre_seeds = sp.recommendation_genre_seeds()
#     print("Available Genre Seeds:", genre_seeds)
# except spotipy.exceptions.SpotifyException as e:
#     print(f"An error occurred while fetching genre seeds: {e}")
#
# # Process the audio features and genre seeds as needed


