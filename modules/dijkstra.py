import sys
import heapq
from modules.graph import *

class DijkstraSolver():
    def __init__(self):
        self.pqueue = []
        heapq.heapify(self.pqueue)

    def findShortestPath(self, g : Graph) -> int: #probably should be graph
        src = None
        tgt = None
        dist = {}
        pred = {}
        for n in g.nodes:
            if n.src: src = n
            if n.tgt: tgt = n
        
        dist[src] = 0
        if src == None or tgt == None:
            print("Both source and target vertices must be given")
            return 1
        
        heapq.heappush(self.pqueue, (0, src))
        while (len(self.pqueue) > 0):
            u = heapq.heappop(self.pqueue) #get min element
            for e in Graph.edges:
                if (e.u.dist + e.weight) < e.v.dist: #an edge u -> v is _tense_ if dist(u) + w(u -> v) < dist(v)
                    relaxEdge(e)

                    return 0
            # TODO
    
def relaxEdge(e : DirEdge):
    e.v.dist = e.u.dist + e.weight
    e.v.pred = e.u
    return 0
            