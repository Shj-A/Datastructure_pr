class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = None
stack = []
visited = []
top = -1

#그래프 간선 생성
G1 = Graph(8)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][7] = 1
G1.graph[1][0] = 1
G1.graph[1][6] = 1
G1.graph[2][0] = 1
G1.graph[2][3] = 1
G1.graph[2][4] = 1
G1.graph[3][2] = 1
G1.graph[3][4] = 1
G1.graph[4][2] = 1
G1.graph[4][3] = 1
G1.graph[5][6] = 1
G1.graph[6][1] = 1
G1.graph[6][5] = 1
G1.graph[6][7] = 1
G1.graph[7][0] = 1
G1.graph[7][6] = 1

print(G1.graph)

current = 0
stack.append(current)
visited.append(current)
top += 1

while (top > -1) :
    next = None
    print('current =',current)
    for vertex in range(8):
        if G1.graph[current][vertex] == 1:
            if vertex in visited:
                pass
            else:
                next = vertex
                break
    print('next =',next)
    if next != None:
        current = next
        stack.append(current)
        top += 1
        print(top)
        visited.append(current)
        print('visited =',visited)
        print('stack =',stack,'\n')
    else:
        stack.pop(top)
        top -= 1
        if top <= -1:
            break
        current = stack[top]
        print(top)
        print('current =', current)
        print('stack =',stack,'\n')

for i in visited:
    print(i+1, end=' ')
