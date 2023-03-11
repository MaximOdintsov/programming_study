class Public:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Protected:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


class Private:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y


public = Public(20, 30)
protected = Protected(10, 5)
private = Private(1, 2)

print(f'Public: {public.x}, {public.y}')
print(f'Protected: {protected._x}, {protected._y}')
print(f'Private: {private.__x}, {private.__y}')