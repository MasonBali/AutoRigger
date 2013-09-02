'''
Created on 01.09.2013

@author: Emre Tekinalp
'''

from maya import cmds
from functions import jointChain


class BipedHeadPuppet(object):
    """this is the biped head puppet class, which will be used to create a real biped head"""
    def __init__(self, side = None, name = [None, None, None], position = [[0, 22, 0], [0, 24, 0], [0, 27, 1]]):
        #vars
        
        #methods
        self.__create(side = side, name = name, position = position)


    def reload_modules(self):
        reload(jointChain)
    
    
    def create_joint_setup(self, side = None, name = [None, None, None], position = [[0, 22, 0], [0, 24, 0], [0, 27, 1]]):
        bindJoints = jointChain.Chain(  side = side, name = name, position = position, mirror = False, radius = 0.25)
        fkJoints   = jointChain.FkChain(side = side, name = name, position = position, mirror = False, radius = 0.5)
        
    
    def create_control_setup(self):
        pass
    
    
    def create_hook_setup(self):
        pass
    
    
    def cleanup(self):
        pass
    
        
    def __create(self, side = None, name = [None, None, None], position = [[0, 22, 0], [0, 24, 0], [0, 27, 1]]):
        self.reload_modules()
        self.create_joint_setup(side = side, name = name, position = position)
        self.create_control_setup()
        self.create_hook_setup()
        self.cleanup()
        