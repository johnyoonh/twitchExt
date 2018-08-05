import random

genres = {"Hip Hop": [11111, 22222, 33333, 44444], "Jazz": [55555, 66666, 77777, 88888, 99999]}
priorities = {"Hip Hop": [.2, .4, .1, .3], "Jazz": [.1, .2, .3, .4]}

artists = {11111: [0000, 1111, 2222, 3333, 4444], 22222: [5555, 6666, 7777, 8888]}

last_10_songs = []

def get_random_genres():
    genre1 = random.choice(list(genres.keys()))
    genre2 = random.choice(list(genres.keys()))
    while genre2 == genre1:
        genre2 = random.choice(list(genres.keys()))
        return genre1, genre2

def get_random_genre(other_genre):
    genre = random.choice(list(genres.keys()))
    while genre == other_genre:
        genre = random.choice(list(genres.keys()))
    return genre

def get_random_artists(genre):
    genre_artists = genres[genre]
    artist1 = random.choice(genre_artists, 2, p=priorities[genre], replace=False)
    artist2 = random.choice(genre_artists, 2, p=priorities[genre], replace=False)
    while artist1 == artist2:
        artist2 = random.choice(genre_artists)
    return artist1, artist2

#def artist_chosen(artist)

def get_random_tracks(artist, last_10_songs):
    track1 = random.choice(artists[artist])
    count = 0
    while track1 in last_10_songs and count < 10:
        track1 = random.choice(artists[artist])
        count += 1

    track2 = random.choice(artists[artist])
    count = 0
    while track2 in last_10_songs and count < 10:
        track2 = random.choice(artists[artist])
        count += 1

    while track1 == track2:
        track2 = random.choice(artists[artist])
    return track1, track2

def track_chosen(track):
    if len(last_10_songs) == 10:
        last_10_songs.pop(0)
    last_10_songs.append(track)
