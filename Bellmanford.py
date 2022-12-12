INF = int(1e9)
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5
gsize = 6
#최단거리 테이블
distance = [INF]*(gsize)
edges = []

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[INF for _ in range(size)] for _ in range(size)]


def Bellmanford(graph, start):
    row_size = len(graph)
    col_size = len(graph[start])
    distance[start] = 0

    #전체 간선 리스트 생성
    for i in range(row_size):
        for j in range(col_size):
            if graph[i][j] != INF:
                edges.append((i,j,graph[i][j]))

    for loop in range(row_size):
        for start_n, end_n, cost in edges:
            if distance[start_n] != INF and distance[end_n] > distance[start_n] + cost:
                distance[end_n] = distance[start_n] + cost
                print(distance,":","Loop:",loop)
                if loop == row_size - 1:
                    print("Negative cycle in Graph")
                    return False

    return distance


G1 = Graph(gsize)
G1.graph[춘천][서울] = 2; G1.graph[춘천][속초] = 1; G1.graph[춘천][광주] = 5
G1.graph[서울][속초] = 3; G1.graph[서울][부산] = 3;
G1.graph[속초][대전] = 1;
G1.graph[대전][광주] = 2; G1.graph[대전][부산] = 2
G1.graph[광주][춘천] = 5
G1.graph[부산][광주] = 2

G2 = Graph(gsize)
G2.graph[춘천][서울] = 2; G2.graph[춘천][속초] = 1; G2.graph[춘천][광주] = 5
G2.graph[서울][속초] = 3; G2.graph[서울][부산] = 3;
G2.graph[속초][대전] = 1;
G2.graph[대전][광주] = 2; G2.graph[대전][부산] = 2
G2.graph[광주][춘천] = -3
G2.graph[부산][광주] = 2

ex2 = [[0, 2, 5, 1, INF, INF],
       [2, 0, 3, 2, INF, INF],
       [5, 3, 0, 3, 1, 5],
       [1, 2, 3, 0, 1, INF],
       [INF, INF, 1, 1, 0, 2],
       [INF, INF, 5, INF, 2, 0]]

#print(Bellmanford(G1.graph, 0))
#print(Bellmanford(ex2, 0))
print(Bellmanford(G2.graph, 5))