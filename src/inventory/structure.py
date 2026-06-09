"""Module structure.py"""

import pandas as pd

import src.functions.nodes


class Structure:
    """

    Structure
    """

    def __init__(self, metrics: pd.DataFrame):
        """

        :param metrics:
        """

        self.__metrics = metrics

        # For creating dict nodes
        self.__nodes = src.functions.nodes.Nodes()

    def __get_nodes(self, blob: pd.DataFrame, partition: pd.Series):
        """

        :param blob:
        :param partition:
        :return:
        """

        data = blob.copy().sort_values(by='milliseconds', ascending=True)

        nodes = self.__nodes(data=data.drop(columns=['section', 'description']), orient='split')
        nodes.update({'section': partition.section, 'description': partition.description})

        return nodes

    def __call__(self, partition: pd.Series):
        """

        :param partition:
        :return:
        """

        blob = self.__metrics.loc[self.__metrics['section'] == partition.section, :]

        return self.__get_nodes(blob=blob, partition=partition)
