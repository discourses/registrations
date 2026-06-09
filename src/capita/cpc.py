"""Module cpc.py"""

import pandas as pd


class CPC:
    """

    <b>Cessations/Capita</b><br>
    Calculates the number of dissolved businesses per inhabitant, per annum.<br>
    """

    def __init__(self, data: pd.DataFrame, population: pd.DataFrame):
        """

        :param data:
        :param population:
        """

        self.__data = data

        # Population
        self.__population = population

    def __frequency(self):

        data = self.__data[['cessation']].groupby(by=['cessation']).value_counts(sort=False)
        data = data.copy().reset_index(drop=False)
        data = data.copy().rename(columns={'count': 'frequency'})

        return data

    def exc(self):
        """

        :return:
        """

        frequencies = self.__frequency()

        # the cessations per capita by year
        cpc = frequencies[['cessation', 'frequency']].merge(
            self.__population[['milliseconds', 'mid_year_estimate']],
            how='left', left_on='cessation', right_on='milliseconds')
        cpc.assign(cessations_per_capita=cpc['frequency']/cpc['mid_year_estimate'])
        cpc = cpc.sort_values(by='cessation', ascending=True)

        return cpc
