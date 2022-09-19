class Tree_node():
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None

def preorder(node):
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)


def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')

# tree 생성
for i in range(1,7):
    globals()["node{}".format(i)] = Tree_node()

node1.data = 'whisky'
node1.left = node2
node1.right = node3
node2.data = 'single'
node3.data = 'blended'
node2.left = node4
node2.right = node5
node3.left = node6
node4.data = 'balvenie'
node5.data = 'glenfidic'
node6.data = 'walker'

preorder(node1)
print('\n')
inorder(node1)
print('\n')
postorder(node1)