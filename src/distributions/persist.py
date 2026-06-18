"""Module persist"""

import os

import config
import src.functions.objects


class Persist:
    """

    Persist
    """

    def __init__(self):
        """

        Constructor
        """

        self.__configurations = config.Config()
        self.__objects = src.functions.objects.Objects()


    def __call__(self, partitions: dict | list[dict], section: str):
        """

        :param partitions:
        :param section:
        :return:
        """

        return self.__objects.write(
            nodes=partitions, path=os.path.join(self.__configurations.distributions_, f'{section}.json'))
