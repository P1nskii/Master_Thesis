import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Set up the Authentication manager
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="2ce4e55ef2df4ef2966532686c370098",
                                               client_secret="6498a02ff7f74753835cc7549289d3d8",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read"))

# Track IDs
track_ids = [
    "4zZ2rPOa8itw3VuusVSicv",
    "3iPOQIKIv6N8bFHA1duhAn",
    "68av1mZz0VsIYXJWATZWUW",
    "1vfTXH0OgN9DQN9ApltfAO",
    "3tu0GkIZwwkmILoD4HemBq",
    "6ILpWIkxZjhRmvlvHPqxKQ",
    "5UTRSgUD07Xir1IsNoYbPQ",
    "4PIyZtdkRBllP7GYu1D7sA",
    "2CHtHSMPci0JTYx2AfMaZk",
    "5ABcMdabdfnrlbhGNT2Ch6",
    "0eeJx68qQPDuiv97Mhozds",
    "6m7htREBCnpPFO8rkuV4Kp",
    "5tapE1gGyABsGFtgeOYchU",
    "2S1LebN6AXXQqJolBxlWgO",
    "6V9doxBqWIdHujB55uxOiL",
    "28etTPWFlXixDmVqnnXqJN",
    "1SccjD8RvJ6vegZLFdgy5a",
    "33g4LmRrWddOvMLnynSktj",
    "0S49TkYtwh4a8HDKQV0Q2K",
    "5rNNZ6fVYxkhwqUfImVhU1",
    "6y8Jzmc4XhyShnHjJmX64l",
    "3IsASNnv8A9dS7GoZy1LY9",
    "0UiGCYGfh6oXBjiBbxgyNn",
    "4iimhn15wHTnsgY0VGNPsm",
    "0THmdEWKzbaJh4LU43fSh2"
]

# List to store track details and audio features
track_data = []

# Iterate over each track ID and retrieve track details and audio features
for track_id in track_ids:
    track_info = sp.track(track_id)
    track_name = track_info['name']
    artist_name = track_info['artists'][0]['name']  # Taking the first artist's name if there are multiple
    release_date = track_info['album']['release_date']
    popularity = track_info['popularity']
    audio_features = sp.audio_features(track_id)[0]  # Only the first audio feature

    # Combine all information into a dictionary
    track_dict = {
        'Track Name': track_name,
        'Artist Name': artist_name,
        'Release Date': release_date,
        'Popularity': popularity,
        'Audio Features': audio_features
    }

    # Append the dictionary to the list
    track_data.append(track_dict)

# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(track_data)

# Display the DataFrame, with a special conditon to ensure full display of values
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Convert the DataFrame to a nicely formatted string
df_str = df.to_string(index=False)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    print(f"Track Name: {row['Track Name']}")
    print(f"Artist Name: {row['Artist Name']}")
    print(f"Release Date: {row['Release Date']}")
    print(f"Popularity: {row['Popularity']}")
    print("Audio Features:")
    for key, value in row['Audio Features'].items():
        print(f"  {key}: {value}")
    print()  # Print an empty line between each track


