from ..proxy import TodoistAPI
from ..immutable import Map, List


class Project(Map):

    def __eq__(self, other):
        if isinstance(other, str):
            return self['name'] == other
        return super().__eq__(other)


class Projects(List):

    def __init__(self, url='projects', **kwargs):
        super().__init__([Project(x) for x in TodoistAPI().get(url, **kwargs)])

