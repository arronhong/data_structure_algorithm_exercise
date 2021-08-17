class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def multiplicative_hashing(k: int, m: int) -> int:
    # hash(k) = (ak mod 2^w) // 2^(w-m)
    a = 1046527 # odd and prime
    w = 32 # machine word width
    if m >= w:
        raise ValueError(f'm should less then {w}')
    return ((a * k) & ((1 << w) - 1)) >> (w - m)


def is_power_of_two(n: int) -> bool:
    return n != 0 and (n-1) & n == 0


def log2(n: int) -> int:
    if not is_power_of_two(n):
        raise ValueError('n should be power of 2')

    ans = -1
    while n:
        n = n >> 1
        ans += 1
    return ans


class HashSet:
    def __init__(self):
        self.size = 0
        self._buckets = [None] * 2
        self.hash_func = multiplicative_hashing

    @property
    def bucket_size(self):
        return len(self._buckets)

    def hash(self, k):
        return self.hash_func(k, log2(len(self._buckets)))

    def _double_buckets(self):
        old_buckets = self._buckets
        self._buckets = [None] * (len(self._buckets) * 2)
        self.size = 0
        for n in old_buckets:
            while n:
                self.add(n.val)
                n = n.next

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        if self.size >= len(self._buckets):
            self._double_buckets()

        hash_val = self.hash(key)
        n = Node(key)
        n.next = self._buckets[hash_val]
        self._buckets[hash_val] = n
        self.size += 1

    def _half_buckets(self):
        old_buckets = self._buckets
        self._buckets = [None] * (len(self._buckets)//2)
        self.size = 0
        for n in old_buckets:
            while n:
                self.add(n.val)
                n = n.next

    def remove(self, key: int) -> None:
        hash_val = self.hash(key)
        cur = self._buckets[hash_val]
        post = None
        while cur:
            if cur.val != key:
                post = cur
                cur = cur.next
                continue

            if post is None:
                self._buckets[hash_val] = cur.next
            else:
                post.next = cur.next

            self.size -= 1
            break

        # min bucket size is 2
        if self.size < len(self._buckets) // 4:
            self._half_buckets()

    def contains(self, key: int) -> bool:
        hash_val = self.hash(key)
        cur = self._buckets[hash_val]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def __str__(self):
        def gen():
            for n in self._buckets:
                while n:
                    yield n.val
                    n = n.next
        return ','.join(map(str, sorted(gen())))


if __name__ == "__main__":
    assert False == is_power_of_two(0)
    assert True == is_power_of_two(1)
    assert False == is_power_of_two(31)
    assert True == is_power_of_two(32)

    assert 0 == log2(1)
    assert 1 == log2(2)
    assert 3 == log2(8)

    s = HashSet()
    s.add(9)
    s.remove(19)
    assert '9' == str(s)
    s.add(14)
    s.remove(19)
    s.remove(9)
    assert 2 == s.bucket_size
    assert 1 == s.size
    s.add(0)
    s.add(3)
    s.add(3)
    assert 4 == s.bucket_size
    assert 3 == s.size
    assert '0,3,14' == str(s)
    s.add(4)
    s.add(5)
    s.add(5)
    assert 8 == s.bucket_size
    assert 5 == s.size
    assert '0,3,4,5,14' == str(s)
    s.remove(0)
    s.remove(3)
    s.remove(3)
    s.remove(4)
    s.remove(5)
    assert 4 == s.bucket_size
    assert 1 == s.size
    s.remove(14)
    assert 2 == s.bucket_size
    assert 0 == s.size
