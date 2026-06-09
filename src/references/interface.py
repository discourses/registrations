"""Module interface.py"""

import pandas as pd

import src.references.data


class Interface:
    """

    Interface
    """

    def __init__(self, clients: dict):
        """

        Constructor
        """

        self.__references = src.references.data.Data()

        # A simple storage service endpoint
        self.__endpoint = f's3://{clients.get('configurations')}/constants/library/'

    def desc(self) -> pd.DataFrame:
        """

        :return:
        """

        uri =  self.__endpoint + '2007.csv'
        dtype = {'description': str, 'section': str, 'division': str, 'group': str, 'level_heading': str}

        # get data
        __desc = self.__references.exc(uri=uri, dtype = dtype)

        return __desc

    def codes(self) -> pd.DataFrame:
        """

        :return:
        """

        uri = self.__endpoint +  'codes.csv'

        # get data
        __codes = self.__references.exc(uri=uri, dtype={'code': str, 'section': str, 'division': str, 'group': str})

        return __codes

    def level(self, level: str) -> pd.DataFrame:
        """

        :param level: At present, `section` or `division` or `group`
        :return:
        """

        desc = self.desc()
        frame = desc.loc[desc['level_heading'].str.lower() == level.lower(), ['description', level]]

        return frame
