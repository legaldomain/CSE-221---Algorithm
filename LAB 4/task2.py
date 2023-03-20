from queue import PriorityQueue

output = open('output2.txt', 'w+')


class Graph:
    def __init__(self, num):
        self.vertex = num
        self.edges = [[-1 for i in range(num)] for j in range(num)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, source, end_point):
    parent = [None] * graph.vertex
    distance = [10 ** 10] * graph.vertex
    parent[source] = 'pi'
    distance[source] = 0
    queue = PriorityQueue()
    queue.put((distance[source], source))

    while not queue.empty():
        dist , m = queue.get()
        graph.visited.append(m)

        for j in range(graph.vertex):
            if j not in graph.visited and graph.edges[m][j] != -1:
                if distance[j] > distance[m] + graph.edges[m][j]:
                    distance[j] = distance[m] + graph.edges[m][j]
                    parent[j] = m
                    queue.put((distance[j], j))
    temp = []
    flag = end_point
    temp.append(flag)

    while flag!=source:
        temp.append(parent[flag])

        flag = parent[flag]

    rev = temp[::-1]


    for i, j in enumerate(rev):
        if i == len(rev) - 1:
            output.write(f"{j}\n")
            #print(j)
        else:
            output.write(f"{j} -> ")
            #print(f"{j} -> ", end='')


file2 = open('input2.txt', 'r').read().splitlines()

p = int(file2[0])
vertex = []
edges = []
for i in range(1, len(file2)):
    x = file2[i].split()
    if len(x) == 2:
        vertex.append(x)
    if len(x) > 2:
        edges.append(x)
def call():
    for i in vertex:
        temp = int(i[1])
        end = int(i[0])
        g = Graph(temp + 2)
        for i in range(temp):
            m = edges.pop(0)
            g.add_edge(int(m[0]), int(m[1]), int(m[2]))
        x = dijkstra(g, 1, end)
call()





