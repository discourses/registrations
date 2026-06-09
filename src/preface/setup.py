"""Module src/preface/setup.py"""

import sys

import config
import src.functions.cache
import src.functions.directories


class Setup:
    """

    Setup
    """

    def __init__(self):
        """

        Constructor
        """

        self.__configurations = config.Config()
        self.__directories = src.functions.directories.Directories()

    def __local(self) -> bool:
        """

        :return:
        """

        self.__directories.cleanup(path=self.__configurations.warehouse)

        states = []
        for path in [self.__configurations.capita_, self.__configurations.distributions_,
                     self.__configurations.inventory_,  self.__configurations.patterns_]:
            states.append(self.__directories.create(path=path))

        return all(states)

    def exc(self):
        """

        :return:
        """

        # previous outputs
        if not self.__local():
            src.functions.cache.Cache().exc()
            sys.exit('Local directories set up stage failure.')
