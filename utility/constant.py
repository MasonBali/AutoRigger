"""
Created on 02.09.2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: Holds all the constants for the autorigger
"""

import os
import json


class Constant():
    """#####################################################################"""
    def __init__(self):
        self.namingconvention()
    # end def __init__()

    def namingconvention(self):
        """Imports naming conventions from the respective .json file and puts
        them into class variables.
        """
        constants = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 'data', 'strings', 'namingconvention.json')
        constants = json.load(open(constants))
        for constant in constants:
            setattr(Constant, constant.upper(), constant)
        # end for constant in constants
    # end def namingconvention()
# end class Constant()
