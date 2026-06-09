"""Module config.py"""

import os


class Config:
    """

    Config
    """

    def __init__(self):
        """
        self.data: str = os.path.join(os.getcwd(), 'data')
        self.library: str = os.path.join(os.getcwd(), 'library')

        Constructor
        """

        '''
        warehouse
        '''
        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.capita_: str = os.path.join(self.warehouse, 'capita')
        self.distributions_: str = os.path.join(self.warehouse, 'distributions')
        self.inventory_: str = os.path.join(self.warehouse, 'inventory')
        self.patterns_:str = os.path.join(self.warehouse, 'patterns')

        '''
        a year (seconds)
        '''
        self.year: float = 365.25 * 24 * 60 * 60

        '''
        The names and tags of the discourses project
        '''
        self.project_tag = 'discourses'
        self.project_key_name = 'TDP'
