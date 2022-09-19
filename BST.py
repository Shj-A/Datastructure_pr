class Tree_node():
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


memory = []
root = None
data_arr = [30, 20, 50, 16, 45, 28]

node = Tree_node()
node.data = data_arr[0]
root = node
memory.append(node)

def print_tree():
    global memory

    for data in memory:
        b = data.data
        if b is None:
            print(None)
        else:
            l = data.left
            r = data.right
            if l is None or r is None:
                if l is None and r is not None:
                    print(b, None, r.data)
                elif r is None and l is not None:
                    print(b, l.data, None)
                else:
                    print(b, 'is leaf Node')
            else:
                print(b, l.data, r.data)

def search_data(data):
    global memory, root

    current = root
    while current is not None:
        if current.data == data:
            return data
        elif current.data > data:
            current = current.left
        else:
            current = current.right

    print("찾는 데이터가 없습니다")
    return 0

def del_node(del_item):
    global memory, root
    current = root
    while current is not None:
        l = current.left
        r = current.right

        if current.data == del_item:
            return 0
        else:
            if l is None:
                pass
            if l.data == del_item:
                if l.left is None:
                    if l.right is None:
                        current.left = None
                        memory.remove(l)
                        del(l)
                        print("삭제완료")
                        return
                    else:
                        current.left = l.right
                        memory.remove(l)
                        del(l)
                        print("삭제완료")
                        return
                else: #삭제할 노드의 왼쪽노드가 있을 때
                    if l.right is None:
                        current.left = l.left
                        memory.remove(l)
                        del(l)
                        print("삭제완료")
                        return
                    else:
                        print("아직 안 배운거")
                        return 0
            elif r.data == del_item:
                if r.left is None:
                    if r.right is None:
                        current.right = None
                        memory.remove(r)
                        del(r)
                        print("삭제완료")
                        return
                    else:
                        current.right = r.right
                        memory.remove(r)
                        del(r)
                        print('삭제완료')
                        return
                else:
                    if r.right is None:
                        current.right = r.left
                        memory.remove(r)
                        del(r)
                        print("삭제완료")
                        return
                    else:
                        return 0
            else:
                if del_item < current.data:
                    if l is None:
                        print("삭제할 데이터가 없습니다")
                        return 0
                    current = l
                else:
                    if r is None:
                        print("삭제할 데이터가 없습니다")
                        return 0
                    current = r

    print("삭제할 데이터가 없습니다")
    return 0


#이진트리 구성
for item in data_arr[1:]:
    temp_node = Tree_node()
    temp_node.data = item

    current = root
    while True:
        if current.data > temp_node.data:
            if current.left == None:
                current.left = temp_node
                memory.append(temp_node)
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = temp_node
                memory.append(temp_node)
                break
            else:
                current = current.right

for item in data_arr:
    print(search_data(item))

print_tree()
del_node(45)
print_tree()
