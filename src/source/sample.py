"""Module sample.py"""

import datetime

import pandas as pd
import numpy as np


class Sample:
    """

    Sampling by time periods.
    """

    def __init__(self, data: pd.DataFrame, cycle: str):
        """

        :param data: A data set of companies incorporated in the United Kingdom
        :param cycle:
        """

        self.__data: pd.DataFrame = data
        self.__cycle: str = cycle

        # Cycles & Granularity
        self.__granularity: dict = {'monthly': '%Y-%m-01', 'annual': '%Y-01-01'}

        # A date or time stamp
        self.__datestamp = datetime.datetime.now().date()

    def __milliseconds(self, dates: pd.Series) -> pd.Series:
        """
        Or  &Rarr; <br>
        milliseconds: np.ndarray = (__datetime.astype(np.int64) / 1e6).astype(np.int64)<br<<br>


        :param dates: Each instance/element encodes a firm incorporation date
        :return:
        """

        datestr = dates.dt.strftime(self.__granularity.get(self.__cycle))
        __datetime: pd.Series = pd.to_datetime(datestr, format='%Y-%m-%d')

        # the unit of the raw numeric value is nanoseconds, dividing by 10^6 converts it to milliseconds
        milliseconds = __datetime.where(
            __datetime.isnull(),
            __datetime.astype(np.int64) / 1e6
        )

        return milliseconds

    def __set_up(self) -> pd.DataFrame:
        """

        :return:
        """

        match self.__cycle:
            case 'monthly':
                string: str = self.__granularity.get(self.__cycle)
                limit = datetime.datetime.strptime(self.__datestamp.strftime(string), '%Y-%m-%d')
                return self.__data.loc[self.__data['date_of_creation'] < limit, :]
            case 'annual':
                return self.__data.loc[self.__data['date_of_creation'].dt.year < self.__datestamp.year, :]
            case _:
                raise ValueError(f'{self.__cycle} is an unknown granularity string')

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        data = self.__set_up()
        data = data.reset_index(drop=True)

        # adding epoch (milliseconds)
        return data.assign(
            milliseconds=self.__milliseconds(dates=data['date_of_creation']),
            cessation=self.__milliseconds(dates=data['date_of_cessation']))
