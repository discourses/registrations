"""Module frequencies.py """

import pandas as pd


class Frequencies:
    """

    Frequencies
    """

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__data = data

    def __get_active(self) -> pd.DataFrame:
        """

        :return:
        """

        active: pd.DataFrame = self.__data.copy().loc[self.__data['company_status'] == 'active', :]

        __active = active[['milliseconds']].groupby(by=['milliseconds']).value_counts(sort=False)
        __active = __active.copy().reset_index(drop=False)
        __active = __active.copy().rename(columns={'count': 'active'})

        return __active

    def __get_dissolved(self) -> pd.DataFrame:
        """
        Alas, and incomprehensibly, isin(['active', 'dissolved', ...]) fails

        :return:
        """

        dissolved: pd.DataFrame = self.__data.copy().loc[self.__data['company_status'] == 'dissolved', :]
        __dissolved = dissolved[['milliseconds']].groupby(by=['milliseconds']).value_counts(sort=False)
        __dissolved = __dissolved.copy().reset_index(drop=False)
        __dissolved = __dissolved.copy().rename(columns={'count': 'dissolved'})

        return __dissolved

    def __get_all(self) -> pd.DataFrame:
        """

        :return:
        """

        data = self.__data[['milliseconds']].groupby(by=['milliseconds']).value_counts(sort=False)
        data = data.copy().reset_index(drop=False)
        data = data.copy().rename(columns={'count': 'all'})

        return data

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        points = self.__data[['milliseconds']].drop_duplicates()

        # frequencies
        frequencies = points.merge(
            self.__get_active(), how='left', on='milliseconds').merge(
            self.__get_dissolved(), how='left', on='milliseconds').merge(
            self.__get_all(), how='left', on='milliseconds')
        frequencies.sort_values(by='milliseconds', ascending=True, inplace=True)

        return frequencies
