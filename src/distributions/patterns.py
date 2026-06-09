"""Module patterns.py"""

import pandas as pd

import src.distributions.graphing


class Patterns:
    """

    Patterns
    """

    def __init__(self, frequencies: pd.DataFrame, descriptions: dict):
        """

        :param frequencies:
        :param descriptions: industrial classifications descriptions
        """

        # instances
        self.__graphing = src.distributions.graphing.Graphing(frequencies=frequencies, descriptions=descriptions)

    def __call__(self, sector: pd.DataFrame, active: pd.DataFrame, dissolved: pd.DataFrame) -> dict:
        """

        :param sector:
        :param active:
        :param dissolved:
        :return:
        """

        # graphing dictionary
        nodes = {}
        for data, stack in zip([sector, active, dissolved], ['sector', 'active', 'dissolved']):
            if data.empty:
                continue
            nodes[stack] = self.__graphing(data=data, stack=stack)

        return nodes
