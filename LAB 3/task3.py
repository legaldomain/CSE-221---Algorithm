import sys

sys.stdin = open("input3.txt", 'r')
sys.stdout = open("output3.txt", 'w')

v = int(input())
graph = {}

for i in range(v):
    s = input().split(' ')
    graph[s[0]] = s[1:]

visited = [0] * v
stack = []


def visit(start):
    visited[int(start) - 1] = 1
    stack.append(start)
    for node in graph[start]:
        if int(node) not in visited:
            visit(node)

def DFS(finish):
    for node in graph:
        if int(node) not in visited:
            visit(node)
    for x in stack:
        print(x, end=' ')
        if x == finish:
            break

print("Places: ", end=' ')
DFS('12')