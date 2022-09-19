class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_node(start):
    current = start
    if current == None:
        return
    print(current.data, end='')
    while current.link != start:
        current = current.link
        print(current.data, end='')
    print()


def insert_node(point, new_data):
    global head, current, pre, memory
    current = head

    if head.data == point:
        node = Node()
        node.data = new_data
        node.link = head
        last = head #현재 리스트의 마지막 부분 탐색을 위한 부분
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    while current.link != head:
        pre = current
        current = current.link  # current 한 칸 이동
        if current.data == point:
            node = Node()
            node.data = new_data
            node.link = current
            pre.link = node
            return

    # 마지막에 삽입
    node = Node()
    node.data = new_data
    current.link = node
    node.link = head

def delete_node(del_data):
    global head, current, pre, memory
    current = head
    #head 삭제
    if del_data == head.data:
        head = current.link
        last = current
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    #나머지 부분 삭제 시
    while current.link != head:
        pre = current
        current = current.link
        if current.data == del_data:
            pre.link = current.link
            del(current)
            return

def search_node(find_data):
    global head, current, pre, memory
    current = head
    while current.link != head:
        if current.data == find_data:
            return current.data
        current = current.link

    # 마지막 노드 확인
    if current.data == find_data:
        return current.data
    else:
        return "찾는 데이터가 없습니다"

memory = []
head, current, pre = None, None, None
arr = ['1a', '2b', '3c', '4d', '5e']

if __name__ == '__main__':

    node = Node()
    node.data = arr[0]
    head = node
    node.link = head
    memory.append(node)

    for item in arr[1:]:
        pre = node
        node = Node()
        node.data = item
        pre.link = node
        node.link = head
        memory.append(node)

    print_node(head)

    # insert_node('7', '0-')
    # print_node(head)

    # delete_node('4d')
    # print_node(head)

    print(search_node('5e'))