from socket import gethostname, gethostbyname
#useful shit

class Vec():
    def __init__(self,x=0,y=0):
        #can accept input as two arguments or a single sequence
        if type(x) in (tuple,list):
            self.data = [n for n in x]
        else:
            self.data = [x,y]

    def makeList(self,x):
        if type(x) == Vec:
            x = x.data
        elif type(x) == int or type(x) == float:
            x = [x,x]
        return x

    def __add__(self,vec):
        vec = self.makeList(vec)
        return Vec(map(sum,zip(self.data,vec)))

    def __sub__(self,vec):
        if type(vec) == list or type(vec) == tuple:
            vec = Vec(vec)
        if type(vec) == int or type(vec) == float:
            vec = Vec(vec,vec)
        return Vec(map(sum,zip(self.data,vec*-1)))

    def __mul__(self,vec):
        vec = self.makeList(vec)
        return Vec( [self.data[0]*vec[0],self.data[1]*vec[1]] ) 

    def normalise(self):
        self.setLen(1)

    def setLen(self,c):
        """
        Sets vector length to c
        """
        abRatio = float(c)/self.length()
        self.data[0] *= abRatio
        self.data[1] *= abRatio

    def length(self):
        return (self.data[0]**2+self.data[1]**2)**0.5

    def __eq__(self,vec):
        vec = self.makeList(vec)
        if self.data == vec:
            return True
        else:
            return False

    

    def __getitem__(self,i):
        return self.data[i]

    def __setitem__(self,i,n):
        self.data[i] = n

    def __str__(self):
        return str(self.data)

def distance(vec1,vec2):
    """
    Returns the distance between cartesian coordinates vec1, vec2. Accepts
    lists, tuples and vecs.
    """
    return ( (vec2[1]-vec1[1])**2+(vec2[0]-vec1[0])**2 )**0.5

def asciiTable(headings,rows=None,columns=None):
    if not ((rows and not columns) or (not rows and columns)):
        print "rows or columns (but not both) must be defined"
    if rows:
        columns = azip(rows)
    print columns
        
def azip(sequences):
    """
    Like zip, but accepts an arbitrary length sequence of sequences instead of requiring comma separated arguments.
    """
    return [[s[i] for s in sequences] for i in range(min(map(len,sequences)))]

def dijkstra(graph,dest):
    """
    Accepts a graph as an adjacency matrix, returns the shortest distance from
    node 0 to node dest, taking 0 to represent no connection between nodes
    """
    itterations = 0
    numNodes = len(graph)
    #initiate known node distances
    known = [None]*numNodes
    #initiate tentative node distances
    temp = [0]+[None]*(numNodes-1)
    while None in known and itterations < 50:
        itterations += 1
        #find minimum temp distance and make it permanent
        #minimum = [distance,index]
        minimum = [None,0]
        for i in range(numNodes):
            #if the temporary distance to node i is known but not the minimum
            #distance
            if temp[i] != None and known[i] == None and (temp[i] < minimum[0] or minimum[0] == None):
                minimum = [temp[i],i]
        known[minimum[1]] = minimum[0]
    
        #update temporary distances
        for i in [i for i in range(numNodes) if graph[minimum[1]][i] != 0 and known[i] == None]:
            #itterating through all of the latest permanent node's non-permanent neighbours
            if minimum[0]+graph[minimum[1]][i] < temp[i] or temp[i] == None:
                temp[i] = minimum[0]+graph[minimum[1]][i]

    print known[dest]

def primesunder(n):
    numbers = [1,1]+[1,0]*(n/2)
    numbers[2] = 0
    for i in range(3,n,2):
        if numbers[i] == 0:
            j = i*2
            while j < n:
                numbers[j] = 1
                j += i
    primes = [x for x in range(n) if numbers[x] == 0]
    return primes
    
headings = ["Node","Distance"]
rows = [[1,23],[2,35],[3,53],[4,2]]

localip = gethostbyname(gethostname())

