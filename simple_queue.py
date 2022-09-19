SIZE = 5

queue = [None for _ in range(SIZE)]
front, rear = -1, -1

def Enqueue(item):
    global SIZE, queue, front, rear

    if (front ==-1) and (rear ==(SIZE-1)):
        print("Anymore space in Queue")
        return None
    else:
        rear += 1
        queue[rear] = item
        return

def Dequeue():
    global SIZE, queue, front, rear

    if (front == -1) and (rear == -1):
        print("Any Data in Queue")
        return None
    else:
        front += 1
        item = queue[front]
        for idx in range(front+1,rear+1):#하나의 출력마다 나머지 모든 값을 움직이는 동작이 수행되므로 크기가 커질수록 비효율적이다
            queue[idx-1] = queue[idx]
        queue[rear] = None
        rear -= 1
        front = -1
        return item


for i in range(4):
    data = str(i) + "!"
    Enqueue(data)
    print(queue)
print('\n')
for i in range(2):
    print(Dequeue())
    print(queue)