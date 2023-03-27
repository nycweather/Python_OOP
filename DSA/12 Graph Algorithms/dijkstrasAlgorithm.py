import heapq


class Edge:
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def add_edge(self, weight, destination):
        edge = Edge(weight, self, destination)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start):
        start.min_distance = 0
        heapq.heappush(self.heap, start)
        while self.heap:
            actual = heapq.heappop(self.heap)
            if actual.visited:
                continue
            for edge in actual.neighbors:
                start = edge.start
                target = edge.target
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predacessor = start
                    heapq.heappush(self.heap, target)
            actual.visited = True

    def get_shortest_path(self, vertex):
        print(f"the shortest path to the vertex is: {vertex.min_distance}")
        actual = vertex
        while actual is not None:
            print(actual.name, end=' ')
            actual = actual.predecessor


# Step 1 creating nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")


# Step 2 Add edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(5, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(13, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

custom = Dijkstra()
custom.calculate(nodeA)
custom.get_shortest_path(nodeB)