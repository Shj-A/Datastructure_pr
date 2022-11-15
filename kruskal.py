from operator import itemgetter

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

namearr = ["춘천","서울",'속초','대전','광주','부산']
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5

def find(parent, x): #x노드와 부모노드 배열을 입력받아 root노드를 찾는 함수
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b): #두 노드의 root 노드를 찾아 작은 인덱스의 root 노드로 변경하는 함수
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

# tempary의 각 아이템의 0번째 요소(가중치)를 기준으로 정렬
tempary = sorted(tempary,key=itemgetter(0))
edgelist = []
for i in range(0,len(tempary),2): #중복되는 간선 제거
    edgelist.append(tempary[i])
print(edgelist)

#각 노드의 parent를 자기 자신으로 초기화
parent = [0]*gsize
for i in range(gsize):
    parent[i] = i


res = []
for edge in edgelist:
    cost, start, end = edge
    # 간선으로 연결된 start노드와 end노드가 같은 집합이 아니면 해당 간선을 선택하고 두 노드의 root노드 갱신
    if find(parent, start) != find(parent,end):
        union(parent,start,end)
        info = (cost, namearr[start], namearr[end])
        res.append(info)
    if len(res) == gsize -1:
        break

print(res)