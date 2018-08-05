import sqlite3
import algorithm

def getGenres():
	genres = ['classical', 'pop', 'jazz', 'rock']
	return algorithm.get_random_genres(genres)

def getArtists(genre):
	conn = sqlite3.connect('genre.db')
	c = conn.cursor()
	c.execute("SELECT artistID, popularity FROM genre where (genre.genreName = ?)", (genre,))
	x = c.fetchall()
	temp = algorithm.normalize(x)
	return algorithm.get_random_artists(temp[0],temp[1])

for i in range(1000):
	print(getArtists(getGenres()[0]))