class Graph:
    def __init__(self, graphDict=None):
        if not graphDict:
            graphDict = {}
        self.graphDict = graphDict

    def bfs(self, start, end):
        queue = [start]
        while queue:
            # print(f"Q {queue}")
            path = queue.pop(0)
            node = path[-1]
            # print(f"Node: {node}, Current Path: {path}")
            if node == end:
                print()
                return path
            for adjacent in self.graphDict.get(node, []):
                newPath = list(path)
                newPath.append(adjacent)
                queue.append(newPath)

customDict = {  
    "a" : ["b", "c"],
    "b" : ["d", "g"],
    "с" : ["d", "e"],
    "d" : ["f"],
    "e": ["f"],
    "g": ["f"]
}
g = Graph(customDict)
print(g.bfs("a", "c"))