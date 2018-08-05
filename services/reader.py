import sqlite3
from algorithm import algorithm
import pandas as pd

def createSongDb():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute("create table test(id, title, duration, explicitContent, popularity);")
	c.execute("insert into test(id, title, duration, explicitContent, popularity) values ('249248', 'Finale', '350', 'false', '0.1')")
	c.execute("insert into test(id, title, duration, explicitContent, popularity) values ('249258', 'Finale', '350', 'false', '0.3')")
	conn.commit()


def normalize(val):
    vals = [float(x[1]) for x in val]
    return [x[0] for x in val],[x / sum(vals) for x in vals]


createSongDb()
