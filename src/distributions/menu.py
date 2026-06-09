"""Module interface"""

import glob
import os
import pathlib

import pandas as pd

import src.functions.objects
import src.references.interface as sri


class Menu:
    """

    Interface
    """

    def __init__(self, references: sri.Interface):
        """

        :param references:
        """

        self.__objects = src.functions.objects.Objects()

        desc = references.desc()
        self.__sections: pd.DataFrame = desc.loc[
            desc['level_heading'].str.lower() == 'section', ['description', 'section']].drop_duplicates()

    def __menu(self, attributes: dict) -> str:
        """

        :param attributes:
        :return:
        """

        listings = glob.glob(os.path.join(attributes.get('source'), '*.json'))
        sections = [pathlib.Path(listing).stem for listing in listings]

        # menu data
        frame = pd.DataFrame(data={'section': sections})
        menu = frame.merge(self.__sections, how='left', on='section')
        menu = menu.rename(columns={'section': 'desc', 'description': 'name'})

        # nodes
        nodes = menu.to_dict(orient='records')

        return self.__objects.write(nodes=nodes, path=attributes.get('path'))

    def exc(self, attributes: dict) -> str:
        """

        :return:
        """

        return self.__menu(attributes=attributes)
