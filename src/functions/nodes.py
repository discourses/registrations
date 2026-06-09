"""Module nodes.py"""

import json

import pandas as pd


class Nodes:
    """

    Nodes
    """

    def __init__(self):
        pass

    @staticmethod
    def __get_nodes(data: pd.DataFrame, orient: str) -> dict | list[dict]:
        """

        :param data:
        :param orient:
        :return:
        """

        string: str = data.to_json(orient=orient)
        nodes: dict | list[dict] = json.loads(string)

        return nodes

    def __call__(self, data: pd.DataFrame, orient: str) -> dict | list[dict]:
        """

        :param data:
        :param orient:
        :return:
        """

        return self.__get_nodes(data=data, orient=orient)
