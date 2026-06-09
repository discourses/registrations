"""Module divisions"""

import pandas as pd


class Sector:
    """

    Divisions
    """

    def __init__(self):
        pass

    def __call__(self, excerpt: pd.DataFrame):
        """

        :param excerpt:
        :return:
        """

        points: pd.Series = excerpt[['milliseconds', 'division']].groupby(
            by=['milliseconds', 'division']).value_counts(sort=False)

        frame: pd.DataFrame = points.reset_index(drop=False)
        frame: pd.DataFrame = frame.copy().rename(columns={'count': 'sector'})

        return frame
