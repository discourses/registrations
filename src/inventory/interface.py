"""Module interface.py"""

import os

import dask
import pandas as pd

import config
import src.functions.objects
import src.inventory.metrics
import src.inventory.structure
import src.references.interface as sri


class Interface:
    """

    Interface
    """

    def __init__(self, data: pd.DataFrame, references: sri.Interface):
        """

        :param data:
        :param references:
        """

        self.__data = data

        # the metrics
        self.__metrics = src.inventory.metrics.Metrics(data=self.__data, references=references).exc()

        # instances
        self.__configurations = config.Config()
        self.__objects = src.functions.objects.Objects()

    def exc(self):
        """

        :return:
        """

        # get structures by `section` partition
        __structure = src.inventory.structure.Structure(metrics=self.__metrics)

        # compute
        partitions: pd.DataFrame = self.__metrics[['section', 'description']].drop_duplicates()
        computations = []
        partition: pd.Series
        for partition in partitions.itertuples():
            nodes = __structure(partition=partition)
            computations.append(nodes)
        __nodes = dask.compute(computations)[0]

        self.__objects.write(
            nodes=__nodes, path=os.path.join(self.__configurations.inventory_, 'inventory.json'))
