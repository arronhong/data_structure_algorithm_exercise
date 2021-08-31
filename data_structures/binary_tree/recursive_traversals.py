from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def preorder(n: Optional[Node]):
    if n is None:
        return

    yield n.data
    yield from preorder(n.left)
    yield from preorder(n.right)


def inorder(n: Optional[Node]):
    if n is None:
        return

    yield from inorder(n.left)
    yield n.data
    yield from inorder(n.right)


def postorder(n: Optional[Node]):
    if n is None:
        return

    yield from postorder(n.left)
    yield from postorder(n.right)
    yield n.data


if __name__ == '__main__':
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

    root = make_tree()
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(preorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(inorder(root))
    assert 'd,g,h,e,b,i,f,c,a' == ','.join(postorder(root))
