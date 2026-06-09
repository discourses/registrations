"""Module setup.py"""

import sys

import src.elements.service as sr
import src.functions.cache
import src.functions.directories
import src.s3.bucket


class Cloud:
    """
    Description
    -----------

    Sets up local & cloud environments
    """

    def __init__(self, service: sr.Service, clients: dict):
        """

        :param service: A suite of services for interacting with Amazon Web Services.<br>
        :param clients: A dict of service/s parameters<br>
        """

        self.__service: sr.Service = service
        self.__clients = clients

        # Bucket
        self.__bucket_name = self.__clients.get('external')

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        # An instance for interacting with Amazon S3 buckets.
        bucket = src.s3.bucket.Bucket(service=self.__service,
                                      location_constraint=self.__clients.get('region_name'),
                                      bucket_name=self.__bucket_name)

        # Strategy Switch: If the bucket exist, do not clear the target prefix, overwrite files instead.
        if bucket.exists():
            return True

        return bucket.create()

    def exc(self) -> bool:
        """

        :return:
        """

        if self.__s3():
            return True

        src.functions.cache.Cache().exc()
        sys.exit('Unable to set up an Amazon S3 (Simple Storage Service) section.')
