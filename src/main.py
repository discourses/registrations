"""Module main.py"""

import argparse
import datetime
import logging
import os
import sys

import pandas as pd


# noinspection DuplicatedCode
def main():
    """
    Entry point

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))

    # the raw data
    data: pd.DataFrame = source.exc(cycle=args.cycle)
    data.info()

    # distributions
    src.distributions.interface.Interface(data=data, references=references).exc()

    # inventory
    src.inventory.interface.Interface(data=data, references=references).exc()

    # patterns
    src.patterns.interface.Interface(data=data).exc()

    # capita
    if args.cycle == 'annual':
        src.capita.interface.Interface(data=data, clients=clients).exc()
    else:
        src.capita.interface.Interface(data=source.exc(cycle='annual'), clients=clients)

    # transfer
    src.transfer.interface.Interface(service=service, clients=clients).exc()

    # cache
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # noinspection DuplicatedCode
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO, filename='project.log', filemode='w',
                        format='%(message)s\n%(asctime)s.%(msecs)03d\n',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.capita.interface
    import src.distributions.interface
    import src.functions.cache
    import src.patterns.interface
    import src.preface.interface
    import src.inventory.interface
    import src.references.interface
    import src.source.interface
    import src.transfer.interface
    import src.specific

    specific = src.specific.Specific()
    parser = argparse.ArgumentParser()
    parser.add_argument('--cycle', type=specific.cycle, default='annual',
                        help='This optional parameter expects a string; annual | monthly')
    args: argparse.Namespace = parser.parse_args()

    # clients, service
    clients, service = src.preface.interface.Interface().exc()

    # references
    references = src.references.interface.Interface(clients=clients)

    # source
    source = src.source.interface.Interface(clients=clients)

    main()
