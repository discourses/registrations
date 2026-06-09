"""Module interface"""

import glob
import os
import pathlib

import pandas as pd

import config
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

        self.__configurations = config.Config()

        # descriptions
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

        return src.functions.objects.Objects().write(nodes=nodes, path=attributes.get('path'))

    def exc(self) -> str:
        """

        :return:
        """

        attributes = {'source': self.__configurations.distributions_,
                      'path': os.path.join(self.__configurations.distributions_, 'menu.json')}

        return self.__menu(attributes=attributes)
