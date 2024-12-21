import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}

def insert(root, path):
    node = root
    for p in path:
        if p not in node.children:
            node.children[p] = Node()
        node = node.children[p]

def print_tree(node, depth):
    for key in sorted(node.children):
        print("--" * depth + key)
        print_tree(node.children[key], depth + 1)

n = int(input())
root = Node()

for _ in range(n):
    path = input().split()[1:]
    insert(root, path)

print_tree(root, 0)
