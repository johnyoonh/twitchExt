from numpy.random import choice
import random

genres = {"Hip Hop": [11111, 22222, 33333, 44444], "Jazz": [55555, 66666, 77777, 88888, 99999]}
artist_priorities = {"Hip Hop": [.2, .4, .1, .3], "Jazz": [.1, .2, .3, .2, .2]}

artists = {11111: [0000, 1111, 2222, 3333, 4444], 22222: [5555, 6666, 7777, 8888]}
track_priorities = {11111: [.1, .2, .3, .2, .2], 22222: [.1, .1, .4, .4]}
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
    artist1 = choice(genre_artists, 1, p=artist_priorities[genre], replace=False)
    artist2 = choice(genre_artists, 1, p=artist_priorities[genre], replace=False)

    while artist1 == artist2:
        artist2 = choice(genre_artists, 1, p=priorities[genre], replace=False)
    return artist1[0], artist2[0]
    
#def artist_chosen(artist)

def get_random_tracks(artist, last_10_songs):
    track1 = random.choice(artists[artist])
    count = 0
    while track1 in last_10_songs and count < 10:
        track1 = choice(artists[artist], 1, p=track_priorities[artist], replace=False)
        count += 1

    track2 = choice(artists[artist], 1, p=track_priorities[artist], replace=False)
    count = 0
    while track2 in last_10_songs and count < 10:
        track2 = choice(artists[artist], 1, p=track_priorities[artist], replace=False)
        count += 1

    while track1 == track2:
        track2 = choice(artists[artist], 1, p=track_priorities[artist], replace=False)
    return track1, track2[0]

def track_chosen(track):
    if len(last_10_songs) == 10:
        last_10_songs.pop(0)
    last_10_songs.append(track)

def test_frequency():
    tracks = []
    for i in range(500):
        track1, track2 = get_random_tracks(11111, [])
        tracks.append(track1)
        tracks.append(track2)
        track_chosen(random.choice([track1, track2]))
    print(tracks.count(0000))
    print(tracks.count(1111))
    print(tracks.count(2222))
    print(tracks.count(3333))
    print(tracks.count(4444))