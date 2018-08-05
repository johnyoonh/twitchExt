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
    c.execute("CREATE table genre(genreName1, vote1, genreName2, vote2);")
    temp = gc.getGenres()
    genres1, genres2 = temp[0], temp[1]
    print(temp)
    c.execute("INSERT into genre(genreName1, vote1, genreName2, vote2) values (?,?,?,?)", (genres1, str(0), genres2,  str(0)))
    conn.commit()
    return jsonify({genres1: 0, genres2:0})


@app.route("/genre/<name>", methods = ['GET', 'POST'])
def add_vote(name):
    conn = sqlite3.connect('genreVote.db')
    c = conn.cursor()
    c.execute("SELECT * from genre")
    x = c.fetchone()
    print(x)
    vote = x[0] if x[0] == name else x[2]
    
    return name

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
