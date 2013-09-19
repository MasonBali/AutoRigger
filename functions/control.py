'''
Created on 16.09.2013

@author: Emre Tekinalp
'''

from maya import cmds
from fundamentals import attribute, node, parent


class Control(object):
    """
    This class creates the control shapes, which will be used for the rig
    """

    def __init__(self, side = None, name = None, size = 1, shape = 0, 
                  color = None, position = [0.0,0.0,0.0], rotation = [0.0,0.0,0.0], 
                  orientation = None, flip = False, rotateOrder = None, 
                  parent = None):
        ########################################################################
        #vars

        #methods
        self.__create(side = side, name = name, size = size, shape = shape, 
                      color = color, position = position, rotation = rotation, 
                      orientation = orientation, flip = flip, 
                      rotateOrder = rotateOrder, parent = parent)
    #end def __init__()

    def _reload_modules(self):
        ########################################################################
        reload(attribute)
        reload(node)
        reload(parent)

    def _control_shapes(self, side = None, name = None, size = 1, shape = 0, 
                         color = None, position = [0.0,0.0,0.0], 
                         rotation = [0.0,0.0,0.0], orientation = None, 
                         flip = False, rotateOrder = None, parent = None):
        pass

    def __create(self, side = None, name = None, size = 1, shape = 0, 
                  color = None, position = [0.0,0.0,0.0], rotation = [0.0,0.0,0.0], 
                  orientation = None, flip = False, rotateOrder = None, 
                  parent = None):
        ########################################################################
        self._reload_modules()
        self._control_shapes(side = side, name = name, size = size, shape = shape, 
                      color = color, position = position, rotation = rotation, 
                      orientation = orientation, flip = flip, 
                      rotateOrder = rotateOrder, parent = parent)
    #end def __create()

Control()
#end class Control()