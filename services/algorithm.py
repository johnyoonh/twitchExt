from numpy.random import choice
import random

def get_random_genres(genres):
    genre1 = random.choice(genres)
    genre2 = random.choice(genres)
    while genre2 == genre1:
        genre2 = random.choice(genres)
    return genre1, genre2

def get_random_genre(genres, other_genre):
    genre = random.choice(genres)
    while genre == other_genre:
        genre = random.choice(genres)
    return genre

def normalize(val):
    vals = [float(x[1]) for x in val]
    return [x[0] for x in val],[x / sum(vals) for x in vals]

def get_random_artists(artists, priorities):
    artist1 = choice(artists, 1, p=priorities, replace=False)
    artist2 = choice(artists, 1, p=priorities, replace=False)

    while artist1 == artist2:
        artist2 = choice(artists, 1, p=priorities, replace=False)
    return artist1[0], artist2[0]

#def artist_chosen(artist)

def get_random_tracks(tracks, priorities, last_10_songs):
    track1 = random.choice(tracks)
    count = 0
    while track1 in last_10_songs and count < 10:
        track1 = choice(tracks, 1, p=priorities, replace=False)
        count += 1

    track2 = choice(tracks, 1, p=priorities, replace=False)
    count = 0
    while track2 in last_10_songs and count < 10:
        track2 = choice(tracks, 1, p=priorities, replace=False)
        count += 1

    while track1 == track2:
        track2 = choice(tracks, 1, p=priorities, replace=False)
    return track1, track2[0]

def track_chosen(track, last_10_songs):
    if len(last_10_songs) == 10:
        last_10_songs.pop(0)
    last_10_songs.append(track)

def test_frequency():
    tracks = []
    for i in range(500):
        track1, track2 = get_random_tracks(11111,[.1] ,[])
        tracks.append(track1)
        tracks.append(track2)
        track_chosen(random.choice([track1, track2]))
    print(tracks.count(0000))
    print(tracks.count(1111))
    print(tracks.count(2222))
    print(tracks.count(3333))
    print(tracks.count(4444))
