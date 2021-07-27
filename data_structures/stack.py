class ListStack:
    def __init__(self):
        self._stack = []

    def push(self, obj):
        self._stack.append(obj)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            print('stack is empty')
            return None

    def top(self):
        try:
            return self._stack[-1]
        except IndexError:
            print('stack is empty')
            return None
