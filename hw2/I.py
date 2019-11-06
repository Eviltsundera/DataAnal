import copy

class FragileDict:
    def __init__(self, dictionary=None):
        if dictionary:
            self._data = copy.deepcopy(dictionary)
        else:
            self._data = dict()
        self._lock = False

    def __setitem__(self, key, value):
        if self._lock:
            self._data[key] = value
        else:
            raise RuntimeError("Protected state")

    def __getitem__(self, item):
        if item not in self._data:
            raise KeyError(item)
        else:
            if self._lock:
                return self._data[item]
            else:
                return copy.deepcopy(self._data[item])

    def __contains__(self, item):
        return item in self._data

    def __enter__(self):
        self._buf = copy.deepcopy(self._data)
        self._lock = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False
        if exc_type is not None:
            self._data, self._buf = self._buf, self._data
            print('Exception has been suppressed.')
        else:
            self._data = copy.deepcopy(self._data)
        del self._buf
        return True