from typing import Optional

from binary_tree import Node, make_tree


def recursive_preorder(root: Optional[Node]):
    if root is None:
        return

    yield root.val
    yield from recursive_preorder(root.left)
    yield from recursive_preorder(root.right)


def iterative_preorder(root: Optional[Node]):
    if root is None:
        return

    stack = [root]
    cur = None
    while any(stack):
        cur = stack.pop()
        yield cur.val
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)


def only_right_to_stack_preorder(root: Optional[Node]):
    if root is None:
        return

    cur = root
    stack = []
    while cur or any(stack):
        if cur is not None:
            yield cur.val
            if cur.right is not None:
                stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()


if __name__ == '__main__':
    root = make_tree()
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(recursive_preorder(root))
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(iterative_preorder(root))
    assert 'a,b,d,e,g,h,c,f,i' == ','.join(only_right_to_stack_preorder(root))
