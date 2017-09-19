from urllib.parse import urljoin
from functools import partial, wraps
import uuid
import requests

from .immutable import Map, JSONEncoder

__all__ = ('get', 'post', 'put', 'delete')

_build_url = partial(urljoin, 'https://beta.todoist.com/API/v8/')


def tojson(func):
    @wraps(func)
    def inner(*args, **kwargs):
        resp = func(*args, **kwargs)
        code = resp.status_code
        if code == 200:
            return resp.json()
        elif code < 400:
            return None
        raise Exception('{func}(): Returned error {code}: {error}'.format(
            func=func.__name__, code=code, error=resp.text));
    return inner


@tojson
def get(url, token=None, params=None, **kwargs):
    return requests.get(_build_url(url), params=Params(token, params),
                        **kwargs)


@tojson
def post(url, data, token=None, params=None, headers=None, **kwargs):
    return requests.post(_build_url(url), JSONEncoder().encode(data),
                         params=Params(token, params),
                         headers=Headers(headers), **kwargs)


@tojson
def put(url, data, token=None, params=None, headers=None, **kwargs):
    return requests.put(_build_url(url), JSONEncoder().encode(data),
                        params=Params(token, params),
                        headers=Headers(headers), **kwargs)


@tojson
def delete(url, token=None, params=None, **kwargs):
    return requests.delete(_build_url(url), params=Params(token, params),
                           **kwargs)


class Params(Map):
    def __init__(self, token, params):
        if not isinstance(token, str):
            raise TypeError('Params(): Expected `token` to be a string')
        if len(token) < 30: # random number, probably always 40 chars...
            raise ValueError('Params(): Expected `token` to be 40 chars long')
        super().__init__(Map(token=token, **Map(params)))


class Headers(Map):
    def __init__(self, headers=None):
        default = {'Content-Type': 'application/json',
                   'X-Request-Id': str(uuid.uuid4())}
        super().__init__(Map(**default, **Map(headers)))

