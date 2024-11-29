def preorder(node):
    if node != '.':
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])

def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")

n = int(input())
tree = {}

for _ in range(n):
    data, left, right = input().split()
    tree[data] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
