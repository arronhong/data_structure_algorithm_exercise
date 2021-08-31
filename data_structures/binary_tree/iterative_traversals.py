from typing import Optional, List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root: Optional[Node]):
    stack: List[Node] = [root]
    while any(stack):
        cur = stack.pop()
        yield cur.val
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)


def space_optimized_preorder(root: Optional[Node]):
    # stack
    rights: List[Node] = []
    cur = root
    while cur or any(rights):
        if not cur:
            cur = rights.pop()

        yield cur.val
        if cur.right is not None:
            rights.append(cur.right)
        cur = cur.left


def inorder(root: Optional[Node]):
    # 1. Push the current node to Stack and set current = current->left until current is NULL
    # 2. If current is NULL and stack is not empty then
    #   a) Pop the top item from stack.
    #   b) Print the popped item, set current = popped_item->right
    #   c) Go to first step
    # 3. If current is NULL and stack is empty then we are done.
    parents: List[Node] = []
    cur = root
    while cur or any(parents):
        if cur:
            parents.append(cur)
            cur = cur.left
        else:
            cur = parents.pop()
            yield cur.val
            cur = cur.right


def levelorder(n: Optional[Node]):
    if n is None:
        return

    fifo: List[Node] = [n]
    while any(fifo):
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
