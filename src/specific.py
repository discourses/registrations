"""Module specific.py"""

import sys

import src.functions.cache


class Specific:
    """
    Specific
    """

    def __init__(self):
        """
        Constructor
        """

        self.__cache = src.functions.cache.Cache()

    def cycle(self, value: str = 'annual') -> str:
        """

        :param value:
        :return:
        """

        if not isinstance(value, str):
            self.__cache.exc()
            raise ValueError(('The optional parameter --cycle expects a string; '
                              'annual: will set each creation date to its annual equivalent, '
                              'monthly: will set each creation date to its month equivalent '))

        if value in {'annual', 'monthly'}:
            return value

        self.__cache.exc()
        sys.exit(('The optional parameter --cycle expects a string; '
                  'annual: will set each creation date to its annual equivalent, '
                  'monthly: will set each creation date to its month equivalent '))
