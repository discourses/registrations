"""Module interface.py"""

import logging
import os
import pathlib

import pandas as pd

import config
import src.elements.service as sr
import src.functions.objects
import src.s3.ingress
import src.transfer.cloud
import src.transfer.dictionary


class Interface:
    """
    Class Interface
    """

    def __init__(self, service: sr.Service, clients: dict):
        """

        :param service: A suite of services for interacting with Amazon Web Services. <br>
        :param clients: A dict of service/s parameters<br>
        """

        self.__service: sr.Service = service
        self.__clients = clients

        # Configurations
        self.__configurations = config.Config()

        # Metadata dictionary
        self.__metadata: dict = src.functions.objects.Objects().read(
            uri=os.path.join(pathlib.Path(__file__).parent, 'metadata.json'))

    def __get_metadata(self, frame: pd.DataFrame) -> pd.DataFrame:
        """

        :param frame:
        :return:
        """

        frame = frame.assign(metadata = frame['section'].map(lambda x: self.__metadata[x]))
        logging.info(frame)

        return frame

    def exc(self) -> list[str] | None:
        """

        :return:
        """

        # The strings for transferring data to Amazon S3 (Simple Storage Service)
        strings: pd.DataFrame = src.transfer.dictionary.Dictionary().exc(
            path=self.__configurations.warehouse, extension='*', prefix=self.__configurations.prefix)
        if strings.empty:
            return ['Nothing to transfer.']

        # + metadata
        strings = self.__get_metadata(frame=strings.copy())

        # storage area
        src.transfer.cloud.Cloud(service=self.__service, clients=self.__clients).exc()

        # transfer
        messages = src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__clients.get('external')).exc(
            strings=strings, tags={'project': self.__configurations.project_tag})

        return messages
