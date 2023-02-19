class Graph:
    def __init__(self):
        self.adjacencList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencList.keys():
            self.adjacencList[vertex] = []
            return True
        return False

    def print(self):
        for vertex in self.adjacencList:
            print(vertex, ":", self.adjacencList[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencList.keys() and vertex2 in self.adjacencList.keys():
            self.adjacencList[vertex1].append(vertex2)
            self.adjacencList[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencList.keys() and vertex2 in self.adjacencList.keys():
            self.adjacencList[vertex1].remove(vertex2)
            self.adjacencList[vertex2].remove(vertex1)
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjacencList.keys():
            for others in self.adjacencList[vertex]:
                self.adjacencList[others].remove(vertex)
            del self.adjacencList[vertex]
            return True
        return False

    def breadthFirstSearch(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for others in self.adjacencList[deqVertex]:
                if others not in visited:
                    visited.append(others)
                    queue.append(others)

    def depthFirstSearch(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deqVertex = stack.pop()
            print(deqVertex)
            for others in self.adjacencList[deqVertex]:
                if others not in visited:
                    visited.append(others)
                    stack.append(others)


custom = Graph()
custom.addVertex("A")
custom.addVertex("B")
custom.addVertex("C")
custom.addVertex("D")
custom.addEdge("A", "B")
custom.addEdge("A", "C")
# custom.addEdge("A", "D")
custom.addEdge("B", "C")
custom.addEdge("C", "D")
custom.print()
print()
custom.depthFirstSearch("A")
# custom.removeVertex("D")
# custom.print()