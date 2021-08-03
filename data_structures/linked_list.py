from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def empty(self) -> bool:
        return self.head is None

    def join_value(self):
        d = []
        cur = self.head
        while cur is not None:
            d.append(str(cur.data))
            cur = cur.next
        return ','.join(d)

    def push_front(self, data):
        """adds an item to the front of the list"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def push_back(self, data):
        """adds an item at the end"""
        node = Node(data)
        if self.empty():
            self.head = node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node

    def pop_front(self):
        """remove front item and return its value"""
        if self.empty():
            return

        popped = self.head
        self.head = self.head.next
        popped.next = None
        return popped.data

    def pop_back(self):
        """removes end item and returns its value"""
        if self.empty():
            return
        if self.head.next is None:
            cur = self.head
            self.head = None
            return cur.data

        cur = self.head
        post = None
        while cur.next is not None:
            post = cur
            cur = cur.next

        post.next = None
        return cur.data

    def front(self):
        """get value of front item"""
        if self.empty():
            return
        return self.head.data

    def back(self):
        """get value of end item"""
        if self.empty():
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        return cur.data

    def insert(self, index: int, data):
        """insert value at index, so current item at that index is pointed to
        by new item at index"""
        if index < 0:
            raise ValueError('index should not be negative')
        if self.empty() and index > 0:
            raise IndexError('list is empty')
        if index == 0:
            self.push_front(data)
            return

        cur = self.head
        while index > 1:
            cur = cur.next
            if cur is None:
                raise IndexError('not enough nodes')

            index -= 1

        node = Node(data)
        node.next = cur.next
        cur.next = node

    def delete(self, index: int):
        """removes node at given index"""
        if index < 0:
            raise ValueError('index should not be negative')
        if self.empty():
            raise IndexError('list is empty')
        if index == 0:
            self.pop_front()
            return

        cur = self.head
        post = None
        while index > 0:
            if cur.next is None:
                raise IndexError('not enough nodes')
            post = cur
            cur = cur.next
            index -= 1

        post.next = cur.next
        cur.next = None

    def remove(self, data):
        """removes the first item in the list with this value"""
        if self.empty():
            raise ValueError('list is empty')

        cur = self.head
        post = None
        while cur.data != data:
            if cur.next is None:
                raise ValueError('value not exist in list')

            post = cur
            cur = cur.next

        # data is on first node
        if post is None:
            self.pop_front()
            return

        post.next = cur.next
        cur.next = None

    def reverse(self):
        if self.empty():
            return

        cur = self.head
        post = None
        while cur.next is not None:
            front = cur.next
            cur.next = post
            post = cur
            cur = front
        cur.next = post
        self.head = cur


if __name__ == '__main__':
    ll = LinkedList()
    assert True == ll.empty()
    assert None is ll.pop_front()
    assert None is ll.pop_back()
    try:
        ll.insert(1, 1)
        raise AssertionError('insert empty list with index should be raise')
    except IndexError:
        pass
    try:
        ll.delete(1)
        raise AssertionError('delete empty list with index should be raise')
    except IndexError:
        pass

    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    assert '1,2,3' == ll.join_value()

    ll.push_front(1)
    ll.push_front(2)
    ll.push_front(3)
    assert '3,2,1,1,2,3' == ll.join_value()

    assert 3 == ll.pop_front()
    assert 2 == ll.pop_front()
    assert 1 == ll.pop_front()
    assert '1,2,3' == ll.join_value()

    assert 3 == ll.pop_back()
    assert 2 == ll.pop_back()
    assert 1 == ll.pop_back()
    assert None is ll.pop_back()
    assert None is ll.pop_front()

    ll.insert(0, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    ll.insert(1, 4)
    assert '1,4,2,3' == ll.join_value()
    try:
        ll.insert(100, 100)
        raise AssertionError('insert out of bound should be raise')
    except IndexError:
        pass

    ll.delete(0)
    ll.delete(1)
    ll.delete(1)
    assert '4' == ll.join_value()
    try:
        ll.delete(100)
        raise AssertionError('delete out of bound should be raise')
    except IndexError:
        pass


    ll.push_front(3)
    ll.push_front(4)
    ll.push_front(2)
    ll.push_front(1)
    assert '1,2,4,3,4' == ll.join_value()
    ll.remove(4)
    assert '1,2,3,4' == ll.join_value()
    ll.remove(4)
    assert '1,2,3' == ll.join_value()
    ll.remove(1)
    assert '2,3' == ll.join_value()

    ll.push_back(4)
    ll.push_back(5)
    assert '2,3,4,5' == ll.join_value()
    ll.reverse()
    assert '5,4,3,2' == ll.join_value()
    ll.pop_back()
    ll.pop_back()
    ll.pop_back()
    ll.reverse()
    assert '5' == ll.join_value()
