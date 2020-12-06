class ArrayStack:

    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        return len(self._data) ==0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()
    