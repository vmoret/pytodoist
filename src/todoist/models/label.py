from ..proxy import TodoistAPI
from ..immutable import Map, List


class Label(Map):

    def __eq__(self, other):
        if isinstance(other, str):
            return self['name'] == other
        return super().__eq__(other)


class Labels(List):

    def __init__(self, url='labels', **kwargs):
        super().__init__([Label(x) for x in TodoistAPI().get(url, **kwargs)])

