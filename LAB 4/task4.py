from queue import PriorityQueue

inputFile = open('input4.txt').read().splitlines()
outFile = open('output4.txt', 'w+')
placeList = ['Motijheel', "A", "B", "C","D","E","F", "G","H", "I","J","K","L","MOGHBAZAR"]


def createGraph(arr):
    myDict = {}
    for i in range(len(arr)):
        x = arr[i].split()
        key = placeList.index(x[0])
        val = x[1]
        weight = x[2]
        if key not in myDict.keys():
            if val == key and len(arr) == 1:
                myDict[key] = []
            else:
                if val != key:
                    myDict[key] = [[val, int(weight)]]
        else:
            p = [val, int(weight)]
            myDict[key].append(p)
    return myDict

def dijkstra(graph, source, destination, visited):
    newSource = placeList.index(source)
    newDestination = placeList.index(destination)
    parent = [None] * len(placeList)
    distance = [10 ** 10] * len(placeList)
    parent[newSource] = 'pi'
    distance[newSource] = 0
    queue = PriorityQueue()
    queue.put((distance[newSource], newSource))

    while not queue.empty():
        dist, m = queue.get()
        if visited[m] == 1:
            continue
        visited[m] = 1
        if m in graph.keys():
            for i in graph[m]:
                temp = [i][0]
                alt = dist + temp[1]
                place = placeList.index(temp[0])
                if alt < distance[place]:
                    distance[place] = alt
                    parent[place] = m
                    queue.put((distance[place], place))
    temp = []
    x = placeList.index(destination)
    temp.append(x)
    print("shortest path is: ", end='')
    outFile.write(f"shortest path: ")
    while x != placeList.index(source):
        temp.append(parent[x])
        x = parent[x]
    rev = temp[::-1]
    for i, j in enumerate(rev):
        if i == len(rev) - 1:
            print(placeList[j])
            outFile.write(f"{placeList[j]}\n")
        else:
            print(f"{placeList[j]} -> ", end='')
            outFile.write(f"{placeList[j]} -> ")
    return distance[newDestination]


g = createGraph(inputFile)
visit = [0] * (len(g) + 2)
myDijkstra = dijkstra(g, "Motijheel", "MOGHBAZAR", visit)
print(f"Sum of traffic levels form Motijheel to MOGHBAZAR {myDijkstra}")
outFile.write(f"Sum of traffic levels form Motijheel to MOGHBAZAR {myDijkstra}")
