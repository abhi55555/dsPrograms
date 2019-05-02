import sys


def bellmanFord(G, source):
    destination = {}
    predecessor = {}
    for node in G:
        destination[node] = sys.maxsize
        predecessor[node] = None

    destination[source] = 0

    for i in range(len(G) - 1):
        for u in G:
            for v in G[u]:   # for each neighbour of u
                if destination[v] > destination[u] + G[u][v]:
                    destination[v] = destination[u] + G[u][v]
                    predecessor[v] = u

    for u in G:
        for v in G[u]:
            assert destination[v] <= destination[v] + G[u][v]

    print('final distances\n', destination, '\nand predecessor table is\n', predecessor)


if __name__ == '__main__':
    G = {
        'A': {'B': 45, 'C': 56},
        'B': {'C': 33, 'D': 23, 'E': 12},
        'C': {},
        'D': {'B': 1, 'C': 51},
        'E': {'D': 23}
    }

    bellmanFord(G, 'A')
