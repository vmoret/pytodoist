import collections
import json


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

    def __repr__(self):
        return repr(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


class List(collections.abc.Sequence):
    __slots__ = ('data',)

    def __init__(self, *args):
        argscount = len(args)
        if argscount == 0:
            self.data = []
        elif argscount == 1:
            self.data = list(args[0])
        else:
            self.data = args

    def __repr__(self):
        return repr(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)


class JSONEncoder(json.JSONEncoder):

        def default(self, obj):
            if isinstance(obj, Map):
                return obj.data
            return obj

