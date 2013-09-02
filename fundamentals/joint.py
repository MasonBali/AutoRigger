'''
Created on 28.08.2013

@author: Emre Tekinalp
'''

from maya import cmds


class Joint(object):
    """this is the base joint class, which will be used to create everything dealing with joints"""
    def __init__(self, side = None, name = None, suffix = None, position = [0,0,0], parent = True, radius = 1):
        #vars
        self.name       = []
        self.position   = []
    
        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, parent = parent, radius = radius)
    
    
    def check_joint_name(self, side = None, name = None, suffix = None):
        if side == None:
            if name == None:
                if suffix == None:
                    self.name = 'joint'
                else:
                    self.name = 'joint_' + suffix 
            else:
                if suffix == None:
                    self.name = name
                else:
                    self.name = name + '_' + suffix
        else:
            if name == None:
                if suffix == None:
                    self.name = side + '_joint'
                else:
                    self.name = side + '_joint_' + suffix 
            else:
                if suffix == None:
                    self.name = side + '_' + name + '_JNT'
                else:
                    self.name = side + '_' + name + '_' + suffix 
                
        if name == None:
            if side == None:
                if suffix == None:
                    self.name = 'joint'
                else:
                    self.name = 'joint_' + suffix 
            else:
                if suffix == None:
                    self.name = side + '_joint'
                else:
                    self.name = side + '_joint_' + suffix
        else:
            if side == None:
                if suffix == None:
                    self.name = name
                else:
                    self.name = name + '_' + suffix 
            else:
                if suffix == None:
                    self.name = side + '_' + name + '_JNT'
                else:
                    self.name = side + '_' + name + '_' + suffix 
                    
                    
    def create_joint(self, position = [0,0,0], parent = True, radius = 1):
        if parent == True:
            jnt = cmds.joint(name = self.name, position = position, radius = radius)
            if "|" in jnt:
                self.name = jnt.split("|")[-1]
            else:
                self.name = jnt
        else:
            jnt = cmds.joint(name = self.name, position = position, radius = radius)
            self.name = jnt
            cmds.select(clear = 1)
        
        return self.name


    def __create(self, side = None, name = None, suffix = None, position = [0,0,0], parent = True, radius = 1):
        self.check_joint_name(side = side, name = name, suffix = suffix)
        self.create_joint(position = position, parent = parent, radius = radius)