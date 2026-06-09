"""Module state.py"""

import pandas as pd


class State:
    """

    Members
    """

    def __init__(self):
        pass

    @staticmethod
    def __get_data(excerpt: pd.DataFrame, company_status: str) -> pd.DataFrame:
        """

        :param excerpt:
        :param company_status:
        :return:
        """

        return excerpt.copy().loc[excerpt['company_status'] == company_status, :]

    def __call__(self, excerpt: pd.DataFrame, company_status: str) -> pd.DataFrame:
        """

        :param excerpt: <br>A data set vis-à-vis an industry sector.  The fields are
                        <ul><li>company_number, company_status, code, milliseconds, section, division</li></ul>
                        Wherein the values of `section` & `division` are <b>standard industrial classification</b>
                        classes values.<br><br>
        :param company_status: Refer to the `company_status` section of the Companies House
                               <a href="https://github.com/companieshouse/api-enumerations">constants.yml</a>
        :return:
        """

        data = self.__get_data(excerpt=excerpt, company_status=company_status)
        if data.empty:
            return pd.DataFrame()

        # for a status in question, group the data by division
        points: pd.DataFrame = data[['milliseconds', 'division', 'company_status']].groupby(
            by=['milliseconds', 'division', 'company_status']).value_counts(sort=False).reset_index(drop=False)

        # states
        frame: pd.DataFrame = points.pivot(index=['milliseconds', 'division'], columns='company_status', values='count')
        instances: pd.DataFrame = frame.copy().reset_index(drop=False)

        return  instances[['milliseconds', 'division', company_status]]
