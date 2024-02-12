import sys
from modules.graph import *
from modules.dijkstra import *

class EdmondsKarpSolver():
    def __init__(self):
        self.g = []
        self.gf = [] #residual graph
        self.maxflow_value = 0
        self.mincut_capacity = 0
        return 0

    def solve(self, g: Graph):
        return 0