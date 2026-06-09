"""Module persist.py"""

import os

import pandas as pd

import config
import src.functions.nodes
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
        self.__nodes = src.functions.nodes.Nodes()
        self.__objects = src.functions.objects.Objects()

    def __call__(self, data: pd.DataFrame, string: str, orient: str = 'split') -> str:
        """

        :param data:
        :param string:
        :param orient:
        :return:
        """

        if data.empty:
            return f'skipping: {string}.json'

        # persist
        nodes = self.__nodes(data=data, orient=orient)

        return self.__objects.write(
            nodes=nodes, path=os.path.join(self.__configurations.patterns_, f'{string}.json'))
