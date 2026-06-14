"""Module population.py"""

import numpy as np
import pandas as pd

import src.elements.text_attributes as txa
import src.functions.streams


class Population:
    """

    Population
    """

    def __init__(self, clients: dict):
        """

        :param clients: A dict of service/s parameters
        """

        self.__uri = f's3://{clients.get('configurations')}/inhabitants/library/series-population.csv'

    def __get_population(self) -> pd.DataFrame:
        """

        :return:
        """

        dtype = {'year': int, 'mid_year_estimate': int}
        text = txa.TextAttributes(uri=self.__uri, header=0, usecols=list(dtype.keys()), dtype=dtype)
        data = src.functions.streams.Streams().read(text=text)

        # append the date form of each year
        microseconds=pd.to_datetime(data['year'].astype(str) + '-01-01', format='%Y-%m-%d').astype(np.int64)
        data = data.assign(milliseconds=(microseconds / 1e3).astype(np.int64))

        return data

    def exc(self):
        """

        :return:
        """

        return self.__get_population()
