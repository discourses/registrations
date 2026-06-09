"""Module data.py"""

import pandas as pd

import src.functions.streams
import src.elements.text_attributes as txa


class Data:
    """

    Data
    """

    def __init__(self):

        self.__streams = src.functions.streams.Streams()

    def __data(self, uri: str, dtype: dict) -> pd.DataFrame:
        """

        :param uri:
        :param dtype:
        :return:
        """

        text = txa.TextAttributes(uri=uri, header=0, dtype=dtype)
        data = self.__streams.read(text=text)

        return data

    def exc(self, uri: str, dtype: dict) -> pd.DataFrame:
        """

        :param uri:
        :param dtype:
        :return:
        """

        return self.__data(uri=uri, dtype=dtype)
