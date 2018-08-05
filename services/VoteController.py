from statistics import mode
import operator
import genreController as gc
from flask import Flask
from flask.json import jsonify
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/genre", methods = ['GET'])
def init_db():
    conn = sqlite3.connect('genreVote.db')
    c = conn.cursor()
    c.execute("drop table if exists genre")
    c.execute("CREATE table genre(idnum, genreName1, vote1, genreName2, vote2);")
    temp = gc.getGenres()
    genres1, genres2 = temp[0], temp[1]
    print(temp)
    c.execute("INSERT into genre(idnum, genreName1, vote1, genreName2, vote2) values (?,?,?,?,?)", ('test',genres1, str(0), genres2,  str(0)))
    conn.commit()
    return jsonify({genres1: 0, genres2:0})


@app.route("/genre/<name>", methods = ['GET', 'POST'])
def add_vote(name):
    conn = sqlite3.connect('genreVote.db')
    c = conn.cursor()
    c.execute("SELECT * from genre")
    x = c.fetchone()
    vote1 = int(x[2])
    vote2 = int(x[4])
    if x[1] == name:
        vote1 += 1
    else:
        vote2 += 1
    c.execute("UPDATE genre set vote1 = (?), vote2 = (?) where idnum = 'test'", (str(vote1), str(vote2)))
    conn.commit()
    return jsonify({x[1]:vote1, x[3]:vote2})

@app.route("/genre/winner", methods = ['GET'])
def determine_winner():
    conn = sqlite3.connect('genreVote.db')
    c = conn.cursor()
    c.execute("SELECT * from genre")
    x = c.fetchone()
    vote1 = int(x[2])
    vote2 = int(x[4])
    winner = x[1] if vote1 > vote2 else x[3]
    artistID1, artistID2 = gc.getArtistsIds(winner)
    artist1, artist2 = gc.getArtistNames(artistID1, artistID2)
    conn2 = sqlite3.connect('artistVote.db')
    c = conn2.cursor()
    c.execute("drop table if exists artist")
    c.execute("CREATE table artist(idnum, artist1, vote1, artist2, vote2);")
    c.execute("INSERT into artist(idnum, artist1, vote1, artist2, vote2) values (?,?,?,?,?)", ('test',artistID1, str(0), artistID2,  str(0)))
    conn2.commit()
    return jsonify({artistID1:artist1, artistID2:artist2})

@app.route("/artist/<vote>", methods = ['GET'])
def init_db_artist(vote):
    conn = sqlite3.connect('artistVote.db')
    c = conn.cursor()
    c.execute("SELECT * from artist")
    x = c.fetchone()
    vote1 = int(x[2])
    vote2 = int(x[4])
    if x[1] == vote:
        vote1 += 1
    else:
        vote2 += 1
    c.execute("UPDATE artist set vote1 = (?), vote2 = (?) where idnum = 'test'", (str(vote1), str(vote2)))
    conn.commit()
    return jsonify({x[1]:vote1, x[3]:vote2})

@app.route("/artist/winner", methods = ['GET'])
def determine_artist_winner():
    conn = sqlite3.connect('artistVote.db')
    c = conn.cursor()
    c.execute("SELECT * from artist")
    x = c.fetchone()
    vote1 = int(x[2])
    vote2 = int(x[4])
    winner = x[1] if vote1 > vote2 else x[3]
    print(winner)
    song1, song2 = gc.getSongs(winner,[])
    songName1 = gc.getSongNameFromId(song1)
    songName2 = gc.getSongNameFromId(song2)
    conn2 = sqlite3.connect('songVote.db')
    c = conn2.cursor()
    c.execute("drop table if exists song")
    c.execute("CREATE table song(idnum, song1, vote1, song2, vote2);")
    c.execute("INSERT into song(idnum, artist1, vote1, artist2, vote2) values (?,?,?,?,?)", ('test',song1, str(0), song2,  str(0)))
    conn2.commit()
    return jsonify({song1:songName1, song2:songName2})

class GenreVoteGetter:
    database = {}

    def __init__(self):
        self.database = {}
    def add_vote(name):

        if name in self.database:
            self.database[name] += 1
        else:
            self.database[name] = 0

    def determine_winning_genre_artists():
        winner = max(self.database.iteritems(), key=operator.itemgetter(1))[0]
        artistID1, artistID2 = gc.getArtistsIds(winner)
        return flask.jsonify({getArtistNames(artistID1, artistID2)})

class ArtistVoteGetter:
    database = {}
    def add_vote(name):
        if name in self.database:
            self.database[name] += 1
        else:
            self.database[name] = 0

    def determine_winning_artist_tracks():
        winner = max(self.database.iteritems(), key=operator.itemgetter(1))[0]
        winnerID = gc.getArtistIdsFromNames(winner)
        trackID1, trackID2 = gc.getArtistsIds(winnerID)
        return getSongs(trackID1, trackID2)

class SongVoteGetter:
    database = {}
    def add_vote(name):
        if name in self.database:
            self.database[name] += 1
        else:
            self.database[name] = 0

    def determine_winning_track():
        winner = max(self.database.iteritems(), key=operator.itemgetter(1))[0]
        winnerID = gc.getSongIdFromName(winner)
        return winnerID
