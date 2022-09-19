class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


SIZE = 10
queue = [None for _ in range(SIZE)]
visited = []
front, rear = 0, 0

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


def Enqueue(data):
    global SIZE, queue,front,rear

    if ((rear+1) % SIZE) == (front % SIZE):
        print("Anymore space in queue")
        return None
    else:
        rear = (rear + 1) % SIZE
        queue[rear] = data
        return


def Dequeue():
    global SIZE, queue, front, rear

    if front == rear:
        print("Any data in queue")
        return None
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

print(G1.graph)

current = 0
Enqueue(current)
visited.append(current)

while front != rear:
    current = Dequeue()
    print('current =',current)
    for vertex in range(8):
        if G1.graph[current][vertex]==1:
            if vertex in visited:
                pass
            else:
                Enqueue(vertex)
                visited.append(vertex)
                print('queue =', queue)
                print('visited =', visited)
    print('\n')

print(visited)

