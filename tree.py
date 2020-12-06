class Tree:
    class Position:
        def element(self):
            raise NotADirectoryError('')
        def __eq__(self, other):
            raise NotADirectoryError('')
        def __ne__(self, other):
            return not (self == other)

    def root(self, other):
        raise NotImplementedError()

    def parent(self, p):
        raise NotImplementedError('')

    def num_children(self, p):
        raise NotImplementedError('')

    def children(self, p):
        raise NotImplementedError('')

    def __len__(self):
        raise NotImplementedError('')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p)==0
    def is_empty(self):
        return len(self) ==0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children())

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)