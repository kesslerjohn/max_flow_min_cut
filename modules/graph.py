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
        return 0

class DirEdge(object):
    def __init__(self, u : Vertex, v : Vertex, cpc : int = 5, weight : int = 0):
        # e is a directed edge from u to v
        # all edges initialized with 0 flow
        self.flow = 0
        self.capacity = cpc
        self.u = u
        self.v = v
        self.weight = weight
        return 0

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
        return 0

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges
    
class PQueue(object):
    def __init__(self, priority : str = "lowest") -> int:
        self.items = {}
        self.highest = False
        if priority == "highest":
            self.highest = True
        return 0

    def pop(self) -> Vertex:
        if self.highest:
            return self.items[max(self.items.keys)]
        return self.items[min(self.items.keys)]

    def push(self, item : (int, Vertex)) -> int:
        if self.items[item[0]] == None:
            self.items[item[0]] = [item[1]]
        return 0
    
    def updateKey(self, v : Vertex, val : int) -> int:
        return 0