import sqlite3
import algorithm

def getGenres():
	genres = ['classical', 'pop', 'jazz', 'rock']
	return algorithm.get_random_genres(genres)

def getArtistsIds(genre):
	conn = sqlite3.connect('genre.db')
	c = conn.cursor()
	c.execute("SELECT artistID, popularity FROM genre where (genre.genreName = ?)", (genre,))
	x = c.fetchall()
	temp = algorithm.normalize(x)
	artistID1, artistID2 = algorithm.get_random_artists(temp[0],temp[1])
	return artistID1, artistID2

def getArtistNames(artistId1, artistId2):
	conn = sqlite3.connect('genre.db')
	c = conn.cursor()
	c.execute("SELECT artistName from genre where (genre.artistId = ?)", (artistId1,))
	artist1 = c.fetchone()
	c.execute("SELECT artistName from genre where (genre.artistId = ?)", (artistId2,))
	artist2 = c.fetchone()
	return artist1,artist2

def getArtistIdsFromNames(artistName1):
	conn = sqlite3.connect('genre.db')
	c = conn.cursor()
	c.execute("SELECT artistId from genre where (genre.artistName = ?)", (artistName1,))
	artist1 = c.fetchone()
	return artist1

def getSongs(artist, last10):
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	c.execute("SELECT artistid from songs where (songs.artistid = ?", (133,))
	x = c.fetchall()
	print(x)
	c.execute("SELECT id, popularity FROM songs where (songs.artistid = ?)", (artist,))
	x = c.fetchall()
	temp = algorithm.normalize(x)
	print(x)
	track1, track2 = algorithm.get_random_tracks(temp[0], temp[1], last10)
	c.execute("SELECT title from songs where (songs.id = ?)", (track1,))
	song1 = c.fetchone()[0]
	c.execute("SELECT title from songs where (songs.id = ?)", (track2,))
	song2 = c.fetchone()[0]
	return song1, song2

def getSongIdFromName(songName):
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	c.execute("SELECT id from songs where (songs.title = ?)", (songName,))
	song1 = c.fetchone()[0]
	return song1

def getSongNameFromId(songid):
	conn = sqlite3.connect('song.db')
	c = conn.cursor()
	c.execute("SELECT title from songs where (songs.id = ?)", (songid,))
	song1 = c.fetchone()[0]
	return song1



getSongs(1448, [])