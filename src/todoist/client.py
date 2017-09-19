from .proxy import TodoistAPI
from .models import *


class Todoist(Tasks):
    __slots__ = ('data', '__projects', '__labels')

    def __init__(self, token):
        api = TodoistAPI(token)
        super().__init__()

    @property
    def projects(self):
        try:
            return self.__projects
        except AttributeError:
            self.__projects = Projects()
            return self.__projects

    @property
    def labels(self):
        try:
            return self.__labels
        except AttributeError:
            self.__labels = Labels()
            return self.__labels

