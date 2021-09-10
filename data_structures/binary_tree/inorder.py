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


def predecessor(node):
    cur = node.left
    while cur.right and cur.right is not node:
        cur = cur.right

    return cur


def morris_inorder(root: Optional[Node]):
    if root is None:
        return

    cur = root
    while cur:
        if cur.left is not None:
            pre = predecessor(cur)
            if pre.right is not cur:
                pre.right = cur
                cur = cur.left
            else:
                # it means left subtree of current node is visisted, so destroy
                # threaded link and visit current node and go to right
                pre.right = None
                yield cur.val
                cur = cur.right
        else:
            # node without left subtree, visit the node and go to right subtree
            yield cur.val
            cur = cur.right


if __name__ == '__main__':
    root = make_tree()
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(recursive_inorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(iterative_inorder(root))
    assert 'd,b,g,e,h,a,f,i,c' == ','.join(morris_inorder(root))
