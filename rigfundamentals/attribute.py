"""
Hier ein header mit copyright, autor usw. den header muss ich noch raussuchen
"""

import os
from maya import cmds, mel


class Attribute():
    """This is the class desription"""
    def __init__(self):
        pass
    # end def __init__()

    def method_name(self, input_a, input_b):
        """This method is here for demonstration purposes, and shows for example
        that no line should be longer than 80 characters.
        @param input_a: input with the letter a at the end
        @param input_b: input with b at the end
        @type input_a: String
        @type input_b: int
        @todo: Some real content has yet to be implemented.
        """
        print 'This is variable a: %s'%input_a
        
        # This is an inline comment
        
        for i in range(999):
            print i
        # end for i in range(999)
    # end def method_name()
#end class Attribute