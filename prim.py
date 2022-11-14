import heapq

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

namearr = ["춘천","서울",'속초','대전','광주','부산']
춘천,서울,속초,대전,광주,부산 = 0,1,2,3,4,5

def prim(graph, point):
    start_node = point
    visited = []
    edge_list = []
    q = []
    weight_sum = 0
    #최초 방문 설정
    for item in enumerate(graph[start_node]):
        des = item[0]
        weight = item[1]
        if weight != 0: #가중치가 있다면 우선순위 큐에 삽입
            heapq.heappush(q,(weight,start_node,des))
    visited.append(start_node)
    print(q)
    print(visited)

    while q:# 큐에 아이템이 남아있는 동안 반복
        print(q)
        min_item = heapq.heappop(q) # 가장 가중치가 작은 아이템 pop
        des = min_item[2] #목적 노드 저장
        weight = min_item[0] #가중치 저장
        if des in visited:
            print(min_item,"pass")#목적 노드가 이미 방문된 노드라면 pass(사이클 방지)
            pass
        else:
            visited.append(des)
            edge_list.append(min_item)
            print(visited)
            weight_sum += weight

            for item in enumerate(graph[des]):
                new_des = item[0]
                new_weight = item[1]
                if new_des not in visited:
                    if new_weight != 0:
                        heapq.heappush(q, (new_weight, des, new_des))
                        print(q)
                else:
                    pass

    print(visited)
    return weight_sum, edge_list



#그래프 구성
gsize = 6
G1 = Graph(gsize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 6
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 6; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print(prim(G1.graph,0))