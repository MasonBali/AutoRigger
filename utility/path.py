"""
Created on 21.09.2013
@author: Paul
"""
import os


class Path():
    def __init__(self):
        pass
    # end def __init__
    
    def get_root_path(self):
        return os.path.dirname(os.path.dirname(__file__))
    # end def get_root_path
# end class Path
