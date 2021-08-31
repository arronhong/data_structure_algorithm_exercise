from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root: Optional[Node]):
    stack = [root]
    while any(stack):
        cur = stack.pop()
        yield cur.val
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)


def space_optimized_preorder(root: Optional[Node]):
    # stack
    right_children = []
    cur = root
    while cur or any(right_children):
        if not cur:
            cur = right_children.pop()

        yield cur.val
        if cur.right is not None:
            right_children.append(cur.right)
        cur = cur.left


def inorder(root: Optional[Node]):
    parents = []
    cur = root
    while cur:
        while cur.left is not None:
            parents.append(cur)
            cur = cur.left

        yield cur.val
        # go to next
        if cur.right is not None:
            cur = cur.right
        else:
            # find a parent who has right child
            # visit parent and to go right child
            while any(parents):
                cur = parents.pop()
                yield cur.val
                if cur.right is not None:
                    cur = cur.right
                    break
                else:
                    return


def levelorder(n: Optional[Node]):
    if n is None:
        return

    fifo = [n]
    while len(fifo):
        n = fifo.pop(0)
        if n.left is not None:
            fifo.append(n.left)
        if n.right is not None:
            fifo.append(n.right)
        yield n.val


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


if __name__ == '__main__':
    root = make_tree()
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(preorder(root))
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(space_optimized_preorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(inorder(root))
    assert 'a,b,c,d,e,f,g,h,i' == ','.join(levelorder(root))
