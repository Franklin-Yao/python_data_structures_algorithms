class PostionalList(_DoublyLinkedBase):
    class Postion:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element