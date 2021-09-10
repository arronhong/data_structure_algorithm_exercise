from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def make_tree():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = g
    e.right = h
    c.left = f
    f.right = i
    return a