import sys

class Vertex(object):
    def __init__(self, src : bool, tgt : bool):
        self.src = src
        self.tgt = tgt
        self.dist = 0
        if not src:
            self.dist = sys.maxsize
        self.pred = None #in-neighbor on tentantive shortest path
        self.next = None #out-neighbor on tentative shortest path

class DirEdge(object):
    def __init__(self, u : Vertex, v : Vertex, cpc : int = 5, weight : int = 0):
        # e is a directed edge from u to v
        # all edges initialized with 0 flow
        self.flow = 0
        self.capacity = cpc
        self.u = u
        self.v = v
        self.weight = weight

    def updateFlow(self, f : int):
        self.flow = f
        return 0
    
    def updateWeight(self, w : int):
        self.weight = w
        return 0

class Graph(object):
    def __init__(self, V: list[Vertex], E: list[DirEdge]):
        self.nodes = V
        self.edges = E

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges
    
class PQueue(object):
    def __init__(self, priority : str = "lowest") -> int:
        self.items = {} #items must be tuples (priority, item)
        self.highest = False
        if priority == "highest":
            self.highest = True

    def pop(self) -> Vertex:
        #how to ensure correctness?
        #this is when Haskell Maybe Vertex would be nice
        # TODO try returning the tuple
        try:
            if self.highest:
                return self.items[max(self.items.keys())]
            return self.items[min(self.items.keys())]
        except ValueError:
            return Vertex(True, True)

    def push(self, item : tuple[int, Vertex]) -> int:
        try: 
            self.items[item[0]].append(item[1])
        except KeyError:
           self.items[item[0]] = item[1]
        return 0
    
    