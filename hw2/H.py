from collections import deque
class Node:
    right, left, key, parent = None, None, None, None
    def __init__(self, key = None):
        self.right = None
        self.left = None
        self.parent = None
        self.key = key


class BinarySearchTree:
    root, size = None, 0
    _queue = deque()
    endofiter = False

    def __init__(self, val=None):
        self.root = Node(val)
        self.size = 0

    def append(self, val):
        if val is None:
            pass
        if self.root.key is None:
            self.root = Node(val)
        else:
            self._append(self.root, val)

    def _append(self, root, val):
        if val > root.key:  #go to right
            if root.right is None:
                root.right = Node(val)
                root.right.parent = root
            else:
                self._append(root.right, val)
        elif val < root.key: #go to left
            if root.left is None:
                root.left = Node(val)
                root.left.parent = root
            else:
                self._append(root.left, val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.root.key is None:
            raise StopIteration()
        if self._queue:
            res = self._queue.popleft()
            if not bool(self._queue):
                self.endofiter = True
            return res.key
        else:
            if self.endofiter:
                self.endofiter = False
                raise StopIteration()
            else:
                self.fill_q()
                res = self._queue.popleft()
                if not bool(self._queue):
                    self.endofiter = True
                return res.key

    def fill_q(self):
        q = deque()
        if self.root.key is None:
            pass
        q.append(self.root)
        while q:
            cur = q.popleft()
            self._queue.append(cur)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)

    def __contains__(self, item):
        if self.root.key is None:
            return False
        return self._search(self.root, item)

    def _search(self, root, item):
        if root.key == item:
            return True
        if item > root.key:
            if root.right is None:
                return False
            return self._search(root.right, item)
        if item < root.key:
            if root.left is None:
                return False
            return self._search(root.left, item)


