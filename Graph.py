import sys
class Vertex:
    def __init__(self, artist):
        self.id = artist
        self.songs = []
        self.coArtists = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0


    """resets a node to do search algorithms again"""
    def reset(self):
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    """Sets the color"""
    def setColor(self, color):
        self.color = color

    """Sets the distance"""
    def setDistance(self, d):
        self.dist = d

    """Sets the the predecessor node"""
    def setPred(self, p):
        self.pred = p

    """Sets the discovery time"""
    def setDiscovery(self, dtime):
        self.disc = dtime

    """Sets the finish time"""
    def setFinish(self, ftime):
        self.fin = ftime

    """Returns the finish time"""
    def getFinish(self):
        return self.fin

    """returns the discovery time"""
    def getDiscovery(self):
        return self.disc

    """returns the predecessor node """
    def getPred(self):
        return self.pred

    """returns the distance"""
    def getDistance(self):
        return self.dist

    """returns the color of the node"""
    def getColor(self):
        return self.color

    """creates an edge"""
    def addNeighbor(self, nbr, weight=0):
        self.coArtists[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in self.coArtists])
    
    """returns the connectes nodes list"""
    def getConnections(self):
        return self.coArtists.keys()

    """returns the node id"""
    def getId(self):
        return self.id

    """returns the weight of an edge"""
    def getWeight(self, nbr):
        return self.coArtists[nbr]

