from typing import Optional

from binary_tree import Node, make_tree


def levelorder(root: Optional[Node]):
    if root is None:
        return

    queue = [root]
    while any(queue):
        n = queue.pop(0)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
        yield n.val


if __name__ == '__main__':
    root = make_tree()
    assert 'a,b,c,d,e,f,g,h,i' == ','.join(levelorder(root))
