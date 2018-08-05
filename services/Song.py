class Song(object):
	def __init__(self, id, title, duration, explicitContent, popularity):
		self.id = id
		self.title = title
		self.duration = duration
		self.explicitContent = explicitContent
		self.popularity = popularity

	def __str__(self):
		return str(self.id)