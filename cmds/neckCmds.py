'''
Created on 01.09.2013

@author: Emre Tekinalp
'''

from maya import cmds
from functions import jointChain


class BipedNeckPuppet(object):
    """this is the biped neck puppet class, which will be used to create a real biped neck"""
    def __init__(self, side = None, name = [None, None, None], position = [[0, 20, 0], [0, 21, 0], [0, 22, 0]]):
        #vars
        
        #methods
        self.__create(side = side, name = name, position = position)


    def reload_modules(self):
        reload(jointChain)
    
    
    def create_joint_setup(self, side = None, name = [None, None, None], position = [[0, 20, 0], [0, 21, 0], [0, 22, 0]]):
        bindJoints = jointChain.Chain(  side = side, name = name, position = position, mirror = False, radius = 0.25)
        fkJoints   = jointChain.FkChain(side = side, name = name, position = position, mirror = False, radius = 0.5)
        ikJoints   = jointChain.IkChain(side = side, name = name, position = position, mirror = False, ikSolver = 'ikRPsolver', radius = 0.75)
        
    
    def create_control_setup(self):
        pass
    
    
    def create_hook_setup(self):
        pass
    
    
    def cleanup(self):
        pass
    
        
    def __create(self, side = None, name = [None, None, None], position = [[0, 20, 0], [0, 21, 0], [0, 22, 0]]):
        self.reload_modules()
        self.create_joint_setup(side = side, name = name, position = position)
        self.create_control_setup()
        self.create_hook_setup()
        self.cleanup()
        