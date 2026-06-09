"""Module interface.py"""

import typing

import boto3

import config
import src.elements.service as sr
import src.functions.clients
import src.functions.service
import src.preface.setup
import src.s3.configurations


class Interface:
    """

    Interface
    """

    def __init__(self):
        """

        Constructor
        """

        self.__configurations = config.Config()

    def exc(self) -> typing.Tuple[dict, sr.Service]:
        """

        :return:
        """

        connector = boto3.session.Session()

        # Clients
        clients: dict = src.functions.clients.Clients(connector=connector).exc(
            secret_id=self.__configurations.project_key_name)
        service: sr.Service = src.functions.service.Service(
            connector=connector, region_name=clients.get('region_name')).exc()

        # set-up
        src.preface.setup.Setup().exc()

        return clients, service
