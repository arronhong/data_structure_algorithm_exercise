from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None


def preorder(n: Optional[Node]):
    """
    while not all nodes are visited
        visit current
        go to next
            if has left
                go left
            else if has right
                go right
            else
                find a parent whose right subtree hasn't traversal
                => a parent has right and child to this parent is from left
                then go to right of this parent
    """
    while True:
        yield n.data
        if n.left is not None:
            n = n.left
        elif n.right is not None:
            n = n.right
        else:
            while not (n is n.parent.left and n.parent.right is not None):
                n = n.parent
                if n.parent is None:
                    # now n is root
                    return
            n = n.parent.right


def left_most(n: Node):
    while n.left is not None:
        n = n.left

    return n


def inorder(n: Optional[Node]):
    """
    go to left most
    while not all nodes are visited
        visit current
        go to next
            if has right
                go to right then left most
            else
                if is left
                    go to parent
                else if is right
                    find a parent that child to this parent is from left
    """
    if n is None:
        return

    n = left_most(n)
    while True:
        yield n.data
        if n.right is not None:
            n = n.right
            n = left_most(n)
        else:
            while not (n is n.parent.left):
                n = n.parent
                if n.parent is None:
                    # now n is root
                    return
            n = n.parent


def left_or_right_most(n: Node):
    while True:
        if n.left is not None:
            n = n.left
        elif n.right is not None:
            n = n.right
        else:
            return n

def postorder(n: Optional[Node]):
    """
    go to left or right most
    while not all nodes are visited
        visit current
        go to next
            if is left
                if parent has right
                    go to right of parent and left or right most
                else
                    go to parent
            else if is right
                go to parent
    """
    n = left_or_right_most(n)
    while True:
        yield n.data
        if n.parent is None:
            return
        if n is n.parent.left:
            if n.parent.right is not None:
                n = n.parent.right
                n = left_or_right_most(n)
            else:
                n = n.parent
        else:
            n = n.parent


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
        b.parent = a
        a.right = c
        c.parent = a
        b.left = d
        d.parent = b
        b.right = e
        e.parent = b
        e.left = g
        g.parent = e
        e.right = h
        h.parent =e
        c.left = f
        f.parent = c
        f.right = i
        i.parent = f
        return a
    root = make_tree()
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(preorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(inorder(root))
    assert 'd,g,h,e,b,i,f,c,a' == ','.join(postorder(root))
