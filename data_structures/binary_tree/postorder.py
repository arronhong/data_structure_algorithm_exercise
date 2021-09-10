from typing import Optional

from binary_tree import Node, make_tree


def recursive_postorder(root: Optional[Node]):
    if root is None:
        return

    yield from recursive_postorder(root.left)
    yield from recursive_postorder(root.right)
    yield root.val


def postorder_one_stack(root: Optional[Node]):
    if root is None:
        return

    stack = []
    cur = root
    last_visit = None
    while cur or any(stack):
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        else:
            peek = stack[-1]
            # right child is always visited before root
            if peek.right is None or peek.right == last_visit:
                yield peek.val
                stack.pop()
                last_visit = peek
            else:
                # it means right child is not visited yet
                cur = peek.right


def postorder_two_stacks(root: Optional[Node]):
    """
    postorder is LRN and reverse preorder is NRL. so find reverse preorder and
    push item into stack, then we iteratively pop the stack.
    """
    if root is None:
        return

    cur = root
    st1 = [cur]
    # stack 2 is reverse preorder
    st2 = []
    while any(st1):
        cur = st1.pop()
        st2.append(cur)
        if cur.left is not None:
            st1.append(cur.left)
        if cur.right is not None:
            st1.append(cur.right)

    while any(st2):
        yield st2.pop().val


if __name__ == '__main__':
    root = make_tree()
    assert 'd,g,h,e,b,i,f,c,a' == ','.join(recursive_postorder(root))
    assert 'd,g,h,e,b,i,f,c,a' == ','.join(postorder_one_stack(root))
    assert 'd,g,h,e,b,i,f,c,a' == ','.join(postorder_two_stacks(root))
