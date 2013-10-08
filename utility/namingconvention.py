"""
Created on 02.09.2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: Holds all the namingconventions for the autorigger
"""

import os
import json


class NamingConvention():
    """Imports naming conventions from the respective .json file and puts them
    into class variables.
    """
    def __init__(self):
        constants = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 'data', 'strings', 'namingconvention.json')
        constants = json.load(open(constants))
        for constant in constants:
            setattr(NamingConvention, constant.upper(), constant)
        # end for constant in constants
    # end def __init__
# end class NamingConvention
