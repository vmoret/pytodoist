"""Provides common recipes"""


class SingletonMeta(type):
    """This is a singleton metaclass."""

    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls.__instance

