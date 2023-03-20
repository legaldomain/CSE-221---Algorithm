
from collections import defaultdict 

file=open("input4.txt", mode="r")
inputted_file=file.read().split('\n')
li=inputted_file[1::]

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def Edge(self,u,v): 
        self.graph[u].append(v)

    def BFS(self, f, l): 
        dic = [0] * 1000000
        visited = [False] * 1000000
        queue= [] 
        queue.append(f) 
        visited[f] =True
        while queue:
            f = queue.pop(0) 
            for i in self.graph[f]: 
                if visited[i] == False:
                    dic[i] = dic[f]+1     
                    queue.append(i) 
                    visited[i] =True
        return dic[l[0]]
        

output= open("output4.txt", mode="w")
c=0
final=[]
for i in range(int(inputted_file[0])):
    x= li[i+c].split( )             
    l=list(map(int,x))
    g = Graph()
        
    start=i+c
    end= start+ int(x[1])
    new= li[start+1:end+1]
    c+= int(x[1])
        
    for i in new:
        value =list (map(int,i.split()))
        print(value)
        g.Edge(value[0],value[1])
        g.Edge(value[1],value[0]) 
    out=g.BFS(1,l)
    final.append(out)
    

for i in final:
    i= str(i)+ "\n"
    output.write(i)
output.close()





