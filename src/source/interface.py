"""Module interface.py"""

import logging

import numpy as np
import pandas as pd

import src.source.data
import src.source.sample


class Interface:
    """

    Interface
    """

    def __init__(self, clients: dict):

        self.__url = f's3://{clients.get('internal')}/companies/data/all/196*-01-01.csv'

    def exc(self, cycle: str):
        """

        :param cycle:
        :return:
        """

        # the data
        data: pd.DataFrame = src.source.data.Data(url=self.__url).exc()
        data.info()
        logging.info(data)

        # x = pd.NaT if data['date_of_cessation'].isnull() else data['date_of_cessation'].astype(np.int64) / 1e6
        logging.info(data['date_of_cessation'].where(
            data['date_of_cessation'].isnull(),
            data['date_of_cessation'].astype(np.int64) / 1e6)
        )

        # setting granularity per instance
        data = src.source.sample.Sample(data=data.copy(), cycle=cycle).exc()

        return data
