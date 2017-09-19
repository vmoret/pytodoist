import collections


class Map(collections.abc.Mapping):
    __slots__ = ('data',)

    def __init__(self, *args, **kwargs):
        argscount = len(args)
        if argscount == 1:
            arg = args[0]
            self.data = {} if arg is None else dict(arg)
        elif argscount == 0:
            self.data = kwargs
        else:
            self.data = {}
            raise TypeError(
                'Map(): Expected at most 1 argument, got {:}'.format(argscount)
            )

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)
