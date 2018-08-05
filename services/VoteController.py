from statistics import mode
import operator
import genreController as gc

class GenreVoteGetter:
    database = {}
    def add_vote(name):
        if name in self.database:
            self.database[name] += 1
        else:
            self.database[name] = 0

    def determine_winning_genre_artists():
        winner = max(self.database.iteritems(), key=operator.itemgetter(1))[0]
        artistID1, artistID2 = gc.getArtistsIds(winner)
        return getArtistNames(artistID1, artistID2)

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
