"""Module graphing.py"""

import pandas as pd


class Graphing:
    """

    Graphing
    """

    def __init__(self, frequencies: pd.DataFrame, descriptions: dict):
        """

        :param frequencies:
        :param descriptions: industrial classifications descriptions
        """

        self.__frequencies = frequencies
        self.__descriptions = descriptions

    def __get_distributions(self, frame: pd.DataFrame, name: str) -> pd.DataFrame:
        """

        :param frame:
        :param name: the code name of a division
        :return:
            x: milliseconds, y: percentage, custom: dict of frequency
        """

        # get the number of firms created per time point of a period in question
        data = frame.merge(self.__frequencies[['milliseconds', 'all']], how='left', on='milliseconds')

        # percentage per time point -> assign to `y`
        data = data.assign(y=100 * data[name]/data['all'])
        data = data.copy().sort_values(by='milliseconds', ascending=True)

        # structuring
        __data = data.rename(columns={'milliseconds': 'x', name: 'frequency'})
        __data = __data.assign(custom=__data[['frequency']].to_dict(orient='records')).drop(columns=['all', 'frequency'])

        return __data

    def __per_division(self, excerpt: pd.DataFrame, name: str, stack: str):
        """

        :param excerpt: vis-à-vis the `division` of a `section`
        :param name: the code name of a division
        :param stack: sector | active | dissolved
        :return:
        """

        frame = excerpt.reset_index(drop=False)
        frame = frame.copy().loc[frame[name].notna(), :]

        distributions = self.__get_distributions(frame=frame, name=name)
        data = distributions.to_dict(orient='records')

        # hence
        dictionary = {'data': data}
        dictionary.update({'id': name, 'name': self.__descriptions[name], 'stack': stack})

        return dictionary

    def __call__(self, data: pd.DataFrame, stack: str) -> list[dict]:
        """

        :param data: The data of an industrial classification section; vis-à-vis entire sector,
                     inactive members of sector, or active members of sector.
        :param stack: sector | active (vis-à-vis sector) | dissolved (vis-à-vis sector)
        :return:
        """

        # pivot
        frame = data.pivot(index='milliseconds', columns='division', values=stack)

        # numeric
        dictionaries = [self.__per_division(excerpt=frame[[c]], name=c, stack=stack) for c in frame.columns]

        return dictionaries
