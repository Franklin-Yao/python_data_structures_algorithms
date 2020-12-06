from ch02.array_stack import ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise"""
    lefty = '{[('
    righty = '}])'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if c!=S.pop():
                return False
    return S.is_empty()

print(is_matched('[(5+x)-(y+z)]'))
print(is_matched('[(5+x)-(y+z]]'))
