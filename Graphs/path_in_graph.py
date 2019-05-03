# Program to find if there is a path from source to destination in given graph


class Graph():
    def __init__(self, graph_dict={}):
        self.graphDictionary = graph_dict

    def vertices(self):
        return list(self.graphDictionary.keys())

    def edges(self):
        return list(self.graphDictionary.values())

    def addVertex(self, vertex):
        if vertex not in self.graphDictionary:
            self.graphDictionary[vertex] = []

    def addEdge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self.graphDictionary:
            self.graphDictionary[vertex1].append(vertex2)
        else:
            self.graphDictionary[vertex1] = [vertex2]

    def checkForPath(self, source, destination, path=[]):
        graph = self.graphDictionary
        path = path + [source]
        if source == destination:
            return path
        if source not in graph:
            return None
        for vertex in graph[source]:
            if vertex not in path:
                extendedPath = self.checkForPath(vertex, destination, path)
                if extendedPath:
                    return extendedPath
        return None


if __name__ == '__main__':
    g = {'a': ['b', 'c'],
         'b': ['d', 'e'],
         'c': ['d', 'e'],
         'd': ['e'],
         'e': ['a'],
         'f': []
         }
    graph = Graph(g)
    print('Vertices are ')
    print(graph.vertices())
    print('Edges are ')
    print(graph.edges())

    pathResult = graph.checkForPath('a', 'd')
    if pathResult == None:
        print('No path')
    else:
        print(pathResult)
