"""
Hier ein header mit copyright, autor usw. den header muss ich noch raussuchen
"""

# First all python imports, then all maya imports
# Two blank lines after the import statements
import os
from maya import cmds, mel


class Attribute():
    """This is the class description"""
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
        @return: Some description about the return value.
        @todo: Some real content has yet to be implemented.
        """
        # This is an inline comment.
        
        # This is how String concatenations are handled:
        # Note also that Strings are always surrounded by '. " are used only for 
        # comments
        print 'This is variable a: %s, this is variable b: %s'%(input_a, input_b)
        
        # For loops, while loops, trys, defs, classes and the like are ended with
        # a comment. This is for readability only.
        for i in range(999):
            print i
        # end for i in range(999)
        
        self.public_variable = 0
        self._private_variable = 1
        
        return True
    # end def method_name()
#end class Attribute()