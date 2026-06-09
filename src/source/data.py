"""Module data.py"""

import dask.dataframe
import pandas as pd


class Data:
    """

    Reads-in the raw data
    """

    def __init__(self, url: str):
        """

        Constructor
        """

        self.__url = url
        self.__dtype = {'company_number': str, 'company_status': str,
                        'date_of_creation': str, 'date_of_cessation': str,
                        'code': str, 'postal_code': str}

    def __get_data(self) -> pd.DataFrame:
        """

        :return:
        """

        try:
            block: dask.dataframe = dask.dataframe.read_csv(
                self.__url, header=0, usecols=list(self.__dtype.keys()), dtype=self.__dtype)
        except OSError as err:
            raise err from err

        return block.compute()

    def exc(self):
        """

        :return:
        """

        data = self.__get_data()

        data = data.assign(
            date_of_creation=pd.to_datetime(data['date_of_creation'], format='%Y-%m-%d'),
            date_of_cessation=pd.to_datetime(data['date_of_cessation'], format='%Y-%m-%d'))

        data.reset_index(drop=True, inplace=True)
        data.sort_values(by='date_of_creation', ascending=True, inplace=True)
        data.drop_duplicates(subset='company_number', keep='first', inplace=True)

        return data
