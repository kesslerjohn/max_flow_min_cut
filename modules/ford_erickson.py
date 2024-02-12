import numpy as np 
import sys
import heapq
from modules.graph import *
from modules.dijkstra import DijkstraSolver

class FordEricksonSolver():
    def __init__(self):
        self.g = []
        self.gf = [] #residual graph
        self.maxflow_value = 0
        self.mincut_capacity = 0

    def makeResidual(self):
        #g will be a list of (V, E) tuples
        return 0
    
    def solve(self, g):
        self.g = g
        self.gf = self.makeResidual()

class EdmondsAndKarpSolver():
    def __init__(self):
        self.g = []
        self.gf = [] #residual graph
        self.maxflow_value = 0
        self.mincut_capacity = 0

u = Vertex(src = True, tgt = False)
v = Vertex(src = False, tgt = True)
e = DirEdge(u, v, cpc = 10)

ds = DijkstraSolver()
ds.findShortestPath(u, v)
print(ds.pqueue)

pq = []
heapq.heapify(pq)
heapq.heappush(pq, (1, u))
heapq.heappush(pq, (0, v))
print(pq[0])