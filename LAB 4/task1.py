from queue import PriorityQueue

class Graph:
    def __init__(self, num):
        self.vertex = num
        self.edges = [[-1 for i in range(num)] for j in range(num)]
        self.visited = []
    #adding vals
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, source):

    distance = [10 ** 10] * graph.vertex
    distance[source] = 0
    queue = PriorityQueue()
    queue.put((distance[source], source))
    #check if queue not empty

    while not queue.empty():
        dist, m = queue.get()
        graph.visited.append(m)
        for j in range(graph.vertex):
            if j not in graph.visited and graph.edges[m][j] != -1:
                if distance[j] > distance[m] + graph.edges[m][j]:
                    distance[j] = distance[m] + graph.edges[m][j]
                    queue.put((distance[j], j))
    return distance[m]


file1 = open('input1.txt', 'r').read().splitlines()

p = int(file1[0])
vertex = []
edges = []



for i in range(1, len(file1)):
    x = file1[i].split()
    if len(x) == 2:
        vertex.append(x)
    if len(x) > 2:
        edges.append(x)
output = open('output1.txt', 'w+')
def call():
    for i in vertex:
        temp = int(i[1])
        g = Graph(temp+2)

        for i in range(temp):
            m = edges.pop(0)
            g.add_edge(int(m[0]), int(m[1]), int(m[2]))

        x = dijkstra(g, 1)
        #print(x)
        output.write(f"{x}\n")
call()
