from typing import Optional

from binary_tree import Node, make_tree


def recursive_inorder(root: Optional[Node]):
    if root is None:
        return

    yield from recursive_inorder(root.left)
    yield root.val
    yield from recursive_inorder(root.right)


def iterative_inorder(root: Optional[Node]):
    if root is None:
        return

    stack = []
    cur = root
    while cur or any(stack):
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            yield cur.val
            cur = cur.right


if __name__ == '__main__':
    root = make_tree()
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(recursive_inorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(iterative_inorder(root))
