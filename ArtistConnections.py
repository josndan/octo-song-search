import random
from .Graph import Vertex
from .Queue import Queue

class ArtistConnections:

	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	"""
    Loads the artist connections graph based on a given song database
    Adds the edges based on the last column of the collaborative artists 
    
	"""
	def load_graph(self, songLibaray):

		with open(songLibaray) as database:
			for record in database: # loops through the file with record being a single line in the text file
				tok = record[:-1].split(',') # removes the end of line character
				artist = tok[2] #extracts the artist name
				song = tok[1] # extracts the song namr
				if artist not in self.vertList: # checks if the artist is being read the first time
					self.numVertices+=1
					newArtist = Vertex(artist) # creates a node for the artist if a node for the artist doesn't exist
					self.vertList[artist]=newArtist

				self.vertList[artist].songs.append(song) # adds the songs to the artist song list

				collab = tok[5].split(';') # sperates different collaborater
				for co in collab:
					if co not in self.vertList: # checks if the a node for the collabarater already exists and creates one if it doesn't
						self.numVertices+=1
						self.vertList[co]=Vertex(co)
					if co not in self.vertList[artist].getConnections(): # adds an edge betweent the artist and the collabarator
						self.vertList[artist].addNeighbor(co,1)
					else:
						self.vertList[artist].addNeighbor(co,self.vertList[artist].getWeight(co)+1)

		return self.numVertices

	"""
	Return song libary information
	"""
	def graph_info(self):
		return "Vertex Size: " + str(self.numVertices)

	"""
	Search the information of an artist based on the artist name
	Return a tuple (the number of songs he/she wrote, the collaborative artist list)

	"""
	def search_artist(self, artist_name):

		numSongs = 0;
		artistLst = []

		numSongs = len(self.vertList[artist_name].songs) # initializes number of songs
		artistLst = [a for a in self.vertList[artist_name].getConnections()] # adds all the artists who have collaborated of the given artist
		for k,v in self.vertList.items(): # adds all the artists with whom the given artist collaborated
			if artist_name in v.getConnections():
				if k not in artistLst:
					artistLst.append(k)

		return numSongs, artistLst

	"""returns the weight of an edge betwen two given artists"""
	def findw(self,neig2,art):
		maxw = 0
		if art in self.vertList[neig2].getConnections():
			maxw += self.vertList[neig2].getWeight(art)
		if neig2 in self.vertList[art].getConnections():
			maxw += self.vertList[art].getWeight(neig2)

		return maxw

	"""
	Return a list of two-hop neighbors of a given artist
	"""
	def find_new_friends(self, artist_name):
		two_hop_friends = []
		coll = self.search_artist(artist_name)[1]
		for art in coll: #loops throught the collaboraters of the given artist
			for neig2 in self.search_artist(art)[1]: #loops throught the collaboraters of the given artist's collaboraters
				if neig2 not in coll and neig2 not in two_hop_friends and neig2 != artist_name:
					two_hop_friends.append(neig2) # adds all the two-hop neighbors
		return two_hop_friends

	"""
	Search the information of an artist based on the artist name

	"""
	def recommend_new_collaborator(self, artist_name):

		artist = ""
		numSongs = 0
		fweight = []
		for art in self.find_new_friends(artist_name): #loops through all the two-hop neighbors of the given artist
			w=0
			for art2 in self.search_artist(artist_name)[1]: # loops throrugh all the collaborators of the two-hop neighbors
				w+=self.findw(art,art2) # adds their weight
			fweight.append((art,w))
		artist,numSongs = max(fweight,key=lambda x : x[1]) # finds the artist with maximum weight


		return numSongs,artist

	"""
	Search the information of an artist based on the artist name

	"""
	def shortest_path(self, artist_name):

		path = {}

		# Bredth-first search algorithm implemented on the artist graph
		start = self.vertList[artist_name]
		start.setDistance(0)
		start.setPred(None)
		vertQueue = Queue()
		vertQueue.enqueue(start)
		while (vertQueue.size() > 0):
			currentVert = vertQueue.dequeue() # gets the node which it is going to explore all of its child
			for nbr in [self.vertList[a] for a in self.search_artist(currentVert.getId())[1]]:
				if (nbr.getColor() == 'white') : # if the node is unexplored
					nbr.setColor('gray') # changes its state
					nbr.setDistance(currentVert.getDistance() + 1) #updates the distance
					nbr.setPred(currentVert) # updates the predecessor
					vertQueue.enqueue(nbr) # adds its to the queue
			currentVert.setColor('black')

		for x in self.vertList.values():
			path[x.getId()] = x.getDistance() # initializes the path dictnary with appropriate distances of the node
			x.reset()


		return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
	artistGraph = ArtistConnections()

	#artistGraph.load_graph("TenKsongs_proj22.csv")
	
	ArtistConnections.generate_data("TenKsongs_proj2.csv")
