"""Module metrics.py"""

import pandas as pd

import src.references.interface as sri


class Metrics:
    """

    Metrics
    """

    def __init__(self, data: pd.DataFrame, references: sri.Interface):
        """

        :param data:
        :param references:
        """

        # description
        self.__desc: pd.DataFrame = references.level(level='section')

        # appending the section, division, and group identification codes
        self.__blob: pd.DataFrame = data.merge(references.codes(), how='left', on='code')

    def __aggregates(self) -> pd.DataFrame:
        """

        :return:
        """

        data = self.__blob[['milliseconds']].groupby(
            by=['milliseconds']).value_counts(sort=False).to_frame()

        __data = data.reset_index(drop=False).rename(columns={'count': 'denominator'})

        return __data

    def __disaggregates(self) -> pd.DataFrame:
        """

        :return:
        """

        data = self.__blob[['milliseconds', 'section']].groupby(
            by=['milliseconds', 'section']).value_counts(sort=False)

        __data: pd.DataFrame = data.copy().reset_index(drop=False).rename(columns={'count': 'frequency'})

        return __data

    def exc(self):
        """

        :return:
        """

        disaggregates = self.__disaggregates()
        aggregates = self.__aggregates()

        # frequency, percentage, date & section
        frame = disaggregates.merge(aggregates, how='left', on=['milliseconds']).merge(
            self.__desc, how='left', on='section')
        frame['percentage'] = 100 * frame['frequency'] / frame['denominator']

        return frame
