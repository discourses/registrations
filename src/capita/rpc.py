"""Module rpc.py"""

import pandas as pd

import src.patterns.frequencies
import src.capita.population


class RPC:
    """

    <b>Registrations/Capita</b><br>
    Calculates the number of businesses registrations per inhabitant, per annum.<br>
    """

    def __init__(self, data: pd.DataFrame, population: pd.DataFrame):
        """

        :param data:
        :param population:
        """

        self.__frequencies = src.patterns.frequencies.Frequencies(data=data.copy()).exc()
        self.__population = population

    def exc(self):
        """

        :return:
        """

        frequencies = self.__frequencies.copy()

        # The # of business registrations per inhabitant by year
        rpc = frequencies[['milliseconds', 'all']].merge(
            self.__population[['milliseconds', 'mid_year_estimate']], how='left', on='milliseconds')
        rpc = rpc.assign(creations_per_capita=rpc['all']/rpc['mid_year_estimate'])
        rpc = rpc.sort_values(by='milliseconds', ascending=True)

        return rpc
