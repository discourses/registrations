"""Module percentages.py"""

import pandas as pd

import src.patterns.frequencies


class Percentages:
    """

    Percentages
    """

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__frequencies = src.patterns.frequencies.Frequencies(data=data.copy()).exc()

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        # percentages
        percentages = self.__frequencies.copy()
        percentages = percentages.assign(
            active = 100 * percentages['active']/percentages['all'],
            dissolved = 100 * percentages['dissolved']/percentages['all'])

        return percentages
