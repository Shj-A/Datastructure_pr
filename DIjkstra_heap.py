import heapq
INF = int(1e9)
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5
gsize = 6
visited = [False]*(gsize)
#최단거리 테이블
distance = [INF]*(gsize)

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[INF for _ in range(size)] for _ in range(size)]

def Dijkstra_heap(graph, start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        print(q)
        #가장 거리가 짧은 아이템 추출
        dist, current = heapq.heappop(q)

        #새로 들어온 간선이 이전 결과보다 크다면 처리할 필요가 없으므로 다음 아이템으로 넘어감
        if distance[current] < dist:
            continue

        #현재 방문한 노드의 간선들을 이용하여 최소 거리 테이블 업데이트
        for i in range(gsize):
            if distance[i] > distance[current] + graph[current][i]:
                distance[i] = distance[current] + graph[current][i]
                heapq.heappush(q,(distance[i],i))

    return distance

#그래프 구성
G1 = Graph(gsize)
G1.graph[춘천][서울] = 2; G1.graph[춘천][속초] = 1; G1.graph[춘천][광주] = 5
G1.graph[서울][속초] = 3; G1.graph[서울][부산] = 3;
G1.graph[속초][대전] = 1;
G1.graph[대전][광주] = 2; G1.graph[대전][부산] = 2
G1.graph[광주][춘천] = 5
G1.graph[부산][광주] = 2

ex2 = [[0, 2, 5, 1, INF, INF],
       [2, 0, 3, 2, INF, INF],
       [5, 3, 0, 3, 1, 5],
       [1, 2, 3, 0, 1, INF],
       [INF, INF, 1, 1, 0, 2],
       [INF, INF, 5, INF, 2, 0]]

G2 = Graph(gsize)
G2.graph[춘천][서울] = 2; G2.graph[춘천][속초] = 1; G2.graph[춘천][광주] = 5
G2.graph[서울][속초] = 3; G2.graph[서울][부산] = 3;
G2.graph[속초][대전] = 1;
G2.graph[대전][광주] = 2; G2.graph[대전][부산] = 2
G2.graph[광주][춘천] = -3
G2.graph[부산][광주] = 2

#print(Dijkstra_heap(G1.graph, 0))
print(Dijkstra_heap(ex2, 0))
print(Dijkstra_heap(G2.graph, 5))