from .api import *
from .recipes import SingletonMeta


class TodoistAPI(object, metaclass=SingletonMeta):

    def __init__(self, token=None):
        self.token = token

    def get(self, url, **kwargs):
        return get(url, token=self.token, **kwargs)

    def post(self, url, data, **kwargs):
        return post(url, data, token=self.token, **kwargs)

    def put(self, url, data, **kwargs):
        return put(url, data, token=self.token, **kwargs)

    def delete(self, url, **kwargs):
        return delete(url, token=self.token, **kwargs)

