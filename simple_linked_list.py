class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_node(start):
    current = start
    if current == None :
        return
    print(current.data, end='')
    while current.link != None:
        current = current.link
        print(current.data, end='')
    print()

def insert_node(in_point, new_data):
    global memory, head, current, pre

    #제일 앞에 노드를 삽입할 때
    if head.data == in_point:
        node = Node()
        node.data = new_data
        node.link = head
        head = node # 새로 생성한 노드로 head를 변경
        return

    # 중간에 노드를 삽입할 때
    current = head
    while current.link != None:
        pre = current
        current = current.link #current 한 칸 이동
        if current.data == in_point:
            node = Node()
            node.data = new_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = new_data
    current.link = node


def delete_node(del_item):
    global memory, head, current, pre

    if del_item == head.data:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == del_item:
            pre.link = current.link
            del(current)
            return

    print("삭제할 데이터가 없습니다")

def search_node(search_item):
    global memory, head, current, pre

    for item in memory:
        if item.data == search_item:
            return (item.data, memory.index(item))

    node = Node()
    return (node.data, "No data")

memory = []
head, current, pre = None, None, None
arr = ['1a','2b','3c','4d','5e']

if __name__ == '__main__':

    node = Node()
    node.data = arr[0]
    head = node
    memory.append(node)

    for item in arr[1:]:
        pre = node
        node = Node()
        node.data = item
        pre.link = node
        memory.append(node)

    print_node(head)

    # insert_node("1a", "0-")
    # print_node(head)

    # insert_node("3c", "0-")
    # print_node(head)

    # insert_node("--", '0-')
    # print_node(head)

    # delete_node('3c')
    # print_node(head)

    print(search_node('0-'))