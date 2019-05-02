# A Python program for Dijkstra's shortest path algorithm for adjacency list representation of graph

import heapq


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def addEdge(self, src, dest):

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def dijkstra(G, source):
    print('Dijkstra shortest path ')
    source.setDistance(0)
    unvisitedQueue = [(v.getDistance(), v) for v in G]  # putting tuple pair (distance, vertex) in priority queue
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        uv = heapq.heappop(unvisitedQueue)
    current = uv[1]
    current.setVisited()

    for next in current.adjacent:
        if next.visited:
            continue
        newDist = current.getDistance() + current.getWeight(next)

        if newDist < next.getDistance():
            next.setDistance(newDist)
            next.setPrevious(current)
            print(f'Updated current = {current.getVertexID} next = {next.getVertexID} newDist = {next.getDistance}')
        else:
            print('No updation')


gg = Graph(4)
gg.addEdge(0, 1)
gg.addEdge(0, 2)
gg.addEdge(1, 3)
gg.addEdge(3, 2)

dijkstra(gg, [0])
