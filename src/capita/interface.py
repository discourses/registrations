"""Module interface.py"""

import os

import pandas as pd

import config
import src.capita.cpc
import src.capita.rpc
import src.capita.population
import src.functions.nodes
import src.functions.objects


class Interface:
    """

    Interface
    """

    def __init__(self, data: pd.DataFrame, clients: dict):
        """

        :param data:
        :param clients: A dict of service/s parameters
        """

        self.__data = data
        self.__clients = clients

        self.__configurations = config.Config()
        self.__nodes = src.functions.nodes.Nodes()
        self.__objects = src.functions.objects.Objects()

    def __persist(self, data: pd.DataFrame, string: str, orient: str = 'split'):
        """

        :param data:
        :param string:
        :param orient:
        :return:
        """

        if data.empty:
            return f'skipping: {string}.json'

        # persist
        nodes = self.__nodes(data=data, orient=orient)

        return self.__objects.write(
            nodes=nodes, path=os.path.join(self.__configurations.capita_, f'{string}.json'))

    def exc(self):
        """

        :return:
        """

        population = src.capita.population.Population(clients=self.__clients).exc()

        rpc = src.capita.rpc.RPC(data=self.__data, population=population).exc()
        self.__persist(data=rpc, string='rpc')

        cpc = src.capita.cpc.CPC(data=self.__data, population=population).exc()
        self.__persist(data=cpc, string='cpc')
