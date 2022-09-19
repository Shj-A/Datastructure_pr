SIZE = 5

queue = [None for _ in range(SIZE)]
front, rear = 0, 0


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

def Peek():
    global SIZE, queue, front, rear

    if front == rear:
        print("Any data in queue")
        return None
    else:
        return queue[(front+1)%SIZE]

Peek()
for i in range(5):
    data = str(i) + "!"
    Enqueue(data)
    print(queue)
print('\n')
for i in range(2):
    print(Dequeue())
    print(queue)
print('\n')
for i in range(2):
    data = str(i) + "!"
    Enqueue(data)
    print(queue)


