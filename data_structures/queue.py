class Queue:
    def __init__(self):
        self._queue = []

    def push(self, obj):
        self._queue.append(obj)

    def pop(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            print('queue is empty')