def createGraph(arr):
    myDict = {}
    for i in range(len(arr)):
        x = arr[i].split()
        key = int(x[0])
        val = int(x[1])
        weight = int(x[2])
        if key not in myDict.keys():
            if val == key and len(arr) == 1:
                myDict[key] = []
            else:
                if val != key:
                    myDict[key] = [[val, weight]]
        else:
            p = [val, weight]
            myDict[key].append(p)
    return myDict


def dijkstra(graph, source, visited, vertexCount):
    parent = [None] * (1 + vertexCount)
    distance = [-1] * (1 + vertexCount)
    parent[source] = 'pi'
    distance[source] = 0
    queue = []
    queue.append((distance[source], source))
    queue.sort(reverse=True)
    while len(queue) > 0:
        dist, m = queue.pop()
        if visited[m] == 1:
            continue
        visited[m] = 1
        if m in graph.keys():
            for i in graph[m]:
                temp = [i][0]
                alt = dist + temp[1]
                place = temp[0]
                if alt > distance[place]:
                    distance[place] = alt
                    parent[place] = m
                    queue.append((distance[place], place))


    temp = []
    x = vertexCount
    temp.append(x)

    while x != source:
        temp.append(parent[x])
        x = parent[x]
    maxPath = temp[::-1]
    return graph, maxPath, vertexCount

outFile = open('output5.txt', 'w+')


def countMinPath(graph, path, vertexCount, source):
    temp = 10 ** 10

    if len(path) < vertexCount:
        outFile.write('-1 ')
        #print(-1, end=' ')

    for i in range(0, path.index(source)):
        if path[i] == source:
            outFile.write('0 ')
            #print(0, end=' ')
        if path[i] in graph.keys() and i + 1 < len(path) - 2:
            if graph[path[i]][i + 1][1] < temp:
                temp = graph[path[i]][i + 1][1]
        elif path[i] in graph.keys():
            if graph[path[i]][0][1] < temp:
                temp = graph[path[i]][0][1]

    if temp == 10 ** 10:
        temp = 0
    if source == vertexCount:
        outFile.write(f'{temp}\n')
        #print(temp)
    else:
        outFile.write(f'{temp} ')
        #print(temp, end=' ')


inputFile5 = open('input5.txt').readlines()
p = int(inputFile5[0])
source = []
vertex = []
edges = []

for i in range(1, len(inputFile5)):
    x = inputFile5[i].split()
    if len(x) == 1:
        source.append(x)
    elif len(x) == 2:
        vertex.append(x)
    elif len(x) > 2:
        edges.append(x)

def call():
    for i in vertex:
        n = int(i[0])
        m = int(i[1])
        newSource = source.pop(0)
        temp = ""
        temp2 = []
        for j in range(m):
            x = edges.pop(0)
            for k in x:
                temp += k + " "
            temp2.append(temp)
            temp = ''
        g = createGraph(temp2)
        visit = [0] * (len(g) + 2)
        newGraph, newPath, count = dijkstra(g, int(newSource[0]), visit, n)
        spath = sorted(newPath)

        for i in spath:
            countMinPath(newGraph, newPath, count, i)

call()
