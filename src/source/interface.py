"""Module interface.py"""

import numpy as np
import pandas as pd

import src.source.data
import src.source.sample


class Interface:
    """

    Interface
    """

    def __init__(self, clients: dict):

        self.__url = f's3://{clients.get('internal')}/companies/data/all/*.csv'

    def exc(self, cycle: str):
        """

        :param cycle:
        :return:
        """

        # the data
        data: pd.DataFrame = src.source.data.Data(url=self.__url).exc()

        # setting granularity per instance
        data = src.source.sample.Sample(data=data.copy(), cycle=cycle).exc()

        return data
