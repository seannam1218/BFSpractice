from Vertex import *
import copy

A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")
H = Vertex("H")
I = Vertex("I")
J = Vertex("J")

class Graph():
    def __init__(self):
        self.ADJ = {}

    def setADJ(self, ADJ):
        self.ADJ = ADJ

    # root is the reference to vertex (e.g. A, B, C)
    # dest is also reference to vertex (e.g. A, B, C)
    def shortestPath(self, root, dest):
        root.level = 0
        root.parent = "root"

        frontier = [root]
        level = 0
        output = []

        while dest not in frontier:
            next = []
            for i in range(0, len(frontier)):
                for v in self.ADJ[frontier[i]]:
                    if v.parent == None:
                        v.parent = frontier[i]
                next = next + self.ADJ[frontier[i]]
            level += 1
            for v in next:
                if v.level == None:
                    v.level = level
            frontier = copy.copy(next)

        for i in range(dest.level + 1):
            output = output + [dest.name]
            dest = dest.parent
        return output

adj = {
    A: [B, C],
    B: [A, I, J],
    C: [A, D, G],
    D: [C, F],
    E: [F, J],
    F: [D, E, I],
    G: [C, H, I],
    H: [G],
    I: [B, G, F, J]
}

graph = Graph()
graph.setADJ(adj)
print(graph.shortestPath(D, J))
