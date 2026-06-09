"""Module interface.py"""

import os

import pandas as pd

import src.patterns.frequencies
import src.patterns.percentages
import src.patterns.persist


class Interface:
    """

    Interface
    """

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__data = data

        # Instances
        self.__persist = src.patterns.persist.Persist()

    def exc(self):
        """

        :return:
        """

        # frequencies
        frequencies = src.patterns.frequencies.Frequencies(data=self.__data).exc()
        self.__persist(data=frequencies, string='frequencies')

        # percentages
        percentages = src.patterns.percentages.Percentages(data=self.__data).exc()
        self.__persist(data=percentages, string='percentages')
