class Graph:
    def __init__(self, graphDict=None):
        if graphDict is None:
            graphDict = {}
        self.graphDict = graphDict

    def addEdge(self, vertex, edge):
        self.graphDict[vertex].append(edge)

    def breadthFirstSearch(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for others in self.graphDict[deqVertex]:
                if others not in visited:
                    visited.append(others)
                    queue.append(others)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "f"]
}

custom = Graph(customDict)
custom.addEdge("e", "c")

custom.breadthFirstSearch("a")