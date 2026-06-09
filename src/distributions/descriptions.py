"""Module descriptions.py"""

import pandas as pd

import src.references.interface as sri


class Descriptions:
    """

    Descriptions
    """

    def __init__(self, references: sri.Interface):
        """

        :param references:
        """

        self.__data: pd.DataFrame = references.desc()

    def exc(self) -> dict:
        """

        :return:
        """


        fields = ['description', 'division']
        descriptions = self.__data.loc[self.__data['level_heading'].str.lower() == 'division', fields]
        descriptions.drop_duplicates(inplace=True)
        descriptions.set_index(keys='division', inplace=True)

        return descriptions.to_dict()['description']
