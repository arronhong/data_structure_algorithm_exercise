from typing import Optional, List, Tuple


class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    @classmethod
    def from_list(cls, arr: List[int]):
        bst = cls()
        for k in arr:
            bst.insert(k)

        return bst

    def first(self) -> Optional[int]:
        cur = self.root
        if cur is None:
            return None

        while cur.left is not None:
            cur = cur.left

        return cur.key

    def last(self) -> Optional[int]:
        cur = self.root
        if cur is None:
            return None

        while cur.right is not None:
            cur = cur.right

        return cur.key

    def find(self, key) -> Optional[Node]:
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return cur
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right

        return None

    def close_to(self, key) -> Tuple[Optional[int], Optional[int]]:
        # find 1. max of lte key 2. min of gte key
        cur = self.root
        min_gt = max_lt = None
        while cur is not None:
            if key > cur.key:
                max_lt = max(max_lt or float('-inf'), cur.key)
                cur = cur.right
            elif key < cur.key:
                min_gt = min(min_gt or float('inf'), cur.key)
                cur = cur.left
            else:
                return key, key
        return max_lt, min_gt

    def remove(self, val):
        # TODO
        pass

    def insert(self, key):
        n = Node(key)
        pre = self.root
        pos = None
        while pre is not None:
            pos = pre
            if key <= pre.key:
                pre = pre.left
            else:
                pre = pre.right

        if pos is None:
            self.root = n
        elif key <= pos.key:
            pos.left = n
        else:
            pos.right = n


def inorder(n: Node):
    def _inorder(n: Node):
        if n is None:
            return
        yield from _inorder(n.left)
        yield n.key
        yield from _inorder(n.right)

    return ','.join(str(k) for k in _inorder(n))


if __name__ == '__main__':
    keys = [18,12,25,4,15,25,30,1,13,17,28,3,14,29]
    bst = BinarySearchTree.from_list(keys)
    assert ','.join(str(k) for k in sorted(keys)) == inorder(bst.root)
    assert 1 == bst.first()
    assert 30 == bst.last()
    assert None == bst.find(27)
    assert 13 == bst.find(13).key
    assert (25, 28) == bst.close_to(27)
    assert (30, None) == bst.close_to(45)
    assert (25, 25) == bst.close_to(25)
