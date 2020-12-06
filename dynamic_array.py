import ctypes


class DynamicArray:
    '''A dynamic array class akin to a simplified python list'''

    def __init__(self):
        self._n = 0
        self._capaciy = 1
        self._A = self._make_array(self._capaciy)

    def __len__(self):
        return self._n
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    def append(self, obj):
        if self._n == self._capaciy:
            self._resize(2*self._capaciy)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]

    def _make_array(self, _capaciy):
        return (_capaciy * ctypes.py_object)()