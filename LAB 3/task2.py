file=open("input2.txt", mode="r")
inputted_file=file.read().split('\n')
nodes= int(inputted_file[0])
graph={}

for i in range(1,len(inputted_file)):
    l = inputted_file[i].split(" ")

    key = l[0]
    value = l[1::]
    graph[key]=value
print(graph)

#task 2 part begin#
output2= open("output2.txt", mode="w")
visited = [0]* nodes
queue = []    

def BFS(visited, graph, node, end_point): 
    visited[int(node)-1] =1
    queue.append(node)
    while queue:         
        vw = queue.pop(0)
        s = str(vw)+" "
        output2.write(s)
        if vw == end_point:
            break
        for neighbour in graph[vw]:
            if visited [int(neighbour)- 1]==0:
                visited [int(neighbour) -1]=1
                queue.append ( neighbour)

BFS(visited, graph, "1", "12")
output2.close()