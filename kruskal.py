from operator import itemgetter

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

namearr = ["춘천","서울",'속초','대전','광주','부산']
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


#그래프 구성
gsize = 6
G1 = Graph(gsize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print(G1.graph)

#edge list
tempary = []
for i in range(gsize):
    for k in range(gsize):
        if G1.graph[i][k] != 0 :
            tempary.append([G1.graph[i][k],i,k])

tempary = sorted(tempary,key=itemgetter(0))
edgelist = []
for i in range(0,len(tempary),2) :
    edgelist.append(tempary[i])
print(edgelist)

#parent list
parent = [0]*gsize
for i in range(gsize):
    parent[i] = i


res = []
for edge in edgelist:
    cost, start, end = edge
    if find(parent, start) != find(parent,end):
        union(parent,start,end)
        info = [cost, namearr[start], namearr[end]]
        res.append(info)
    if len(res) == gsize -1:
        break

print(res)