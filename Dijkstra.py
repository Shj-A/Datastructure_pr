INF = int(1e9)
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5
gsize = 6
visited = [False]*(gsize)
# 최단거리 테이블
distance = [INF]*(gsize)

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[INF for _ in range(size)] for _ in range(size)]

def Dijkstra(graph, start):
    #출발노드의 거리 테이블 초기화
    distance[start] = 0
    current = start
    print(visited)
    while False in visited:
        if visited[current] != True:
            visited[current] = True
            for idx in range(gsize):
                if distance[idx] > distance[current] + graph[current][idx]:
                    distance[idx] = distance[current] + graph[current][idx]
            print(distance)
            print(visited)
            min_value = INF
            min_idx = 0
            for i in range(gsize):
                if distance[i] < min_value and not visited[i]:
                    min_value = distance[i]
                    min_idx = i

            current = min_idx

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

#print(Dijkstra(G1.graph, 0))
print(Dijkstra(ex2, 0))