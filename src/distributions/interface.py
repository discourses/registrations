"""Module interface.py"""

import logging

import dask
import pandas as pd

import src.distributions.descriptions
import src.distributions.menu
import src.distributions.patterns
import src.distributions.persist
import src.distributions.sector
import src.distributions.state
import src.functions.objects
import src.patterns.frequencies
import src.references.interface as sri


class Interface:
    """

    Latest, per year of creation, and per sector, (a) created, (b) active, (c) dissolved.
    """

    def __init__(self, data: pd.DataFrame, references: sri.Interface):
        """

        :param data:
        :param references:
        """

        self.__frequencies = src.patterns.frequencies.Frequencies(data=data).exc()
        self.__descriptions = src.distributions.descriptions.Descriptions(references=references).exc()
        self.__patterns = dask.delayed(src.distributions.patterns.Patterns(
            frequencies=self.__frequencies, descriptions=self.__descriptions))

        # merging with codes reference sheet; code | section | division
        self.__frame: pd.DataFrame = data[['company_number', 'company_status', 'code', 'milliseconds']].merge(
            references.codes(), how='left', on='code')

        # menu
        self.__menu = src.distributions.menu.Menu(references=references)

    @dask.delayed
    def __get_excerpt(self, section: str):
        """

        :param section:
        :return:
        """

        return self.__frame.copy().loc[self.__frame['section'] == section, :]

    def exc(self):
        """

        :return:
        """

        __sector = dask.delayed(src.distributions.sector.Sector())
        __state = dask.delayed(src.distributions.state.State())
        __persist = dask.delayed(src.distributions.persist.Persist())

        # compute
        sections: pd.Series = self.__frame['section'].unique().fillna(value='Z')
        computations = []
        for section in sections.to_numpy():
            excerpt = self.__get_excerpt(section=section)
            sector = __sector(excerpt=excerpt)
            active = __state(excerpt=excerpt, company_status='active')
            dissolved = __state(excerpt=excerpt, company_status='dissolved')
            patterns = self.__patterns(sector=sector, active=active, dissolved=dissolved)
            message = __persist(patterns=patterns, section=section)
            computations.append(message)
        messages = dask.compute(computations, scheduler='processes')[0]
        logging.info(messages)

        # menu
        self.__menu.exc()
