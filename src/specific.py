"""Module specific.py"""

import logging
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

        if isinstance(value, str):
            _value = value
        else:
            self.__cache.exc()
            raise logging.error(msg=('The optional parameter --cycle expects a string; '
                                     'annual: will set each creation date to its annual equivalent, '
                                     'monthly: will set each creation date to its month equivalent '))

        if _value in {'annual', 'monthly'}:
            return _value

        self.__cache.exc()
        sys.exit(('The optional parameter --cycle expects a string; '
                  'annual: will set each creation date to its annual equivalent, '
                  'monthly: will set each creation date to its month equivalent '))
