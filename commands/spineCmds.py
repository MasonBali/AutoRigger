'''
Created on 31.08.2013

@author: Emre Tekinalp
'''

from maya import cmds
from functions import jointChain


class BipedSpinePuppet(object):
    """this is the biped spine puppet class, which will be used to create a real biped spine"""
    def __init__(self, side = None, name = [None, None, None], position = [[0, 10, 0], [0, 12, 0], [0, 14, 0], [0, 16, 0]]):
        #vars
        
        #methods
        self.__create(side = side, name = name, position = position)


    def reload_modules(self):
        reload(jointChain)
    
    
    def create_joint_setup(self, side = None, name = [None, None, None], position = [[0, 10, 0], [0, 12, 0], [0, 14, 0], [0, 16, 0]]):
        bindJoints = jointChain.Chain(  side = side, name = name, position = position, mirror = False, radius = 0.25)
        fkJoints   = jointChain.FkChain(side = side, name = name, position = position, mirror = False, radius = 0.5)
        ikJoints   = jointChain.IkChain(side = side, name = name, position = position, mirror = False, ikSolver = 'ikSplineSolver', radius = 0.75)
        
    
    def create_control_setup(self):
        pass
    
    
    def create_hook_setup(self):
        pass
    
    
    def cleanup(self):
        pass
    
        
    def __create(self, side = None, name = [None, None, None], position = [[0, 10, 0], [0, 12, 0], [0, 14, 0], [0, 16, 0]]):
        self.reload_modules()
        self.create_joint_setup(side = side, name = name, position = position)
        self.create_control_setup()
        self.create_hook_setup()
        self.cleanup()
        