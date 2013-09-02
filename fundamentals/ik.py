'''
Created on 28.08.2013

@author: Emre Tekinalp
'''

from maya import cmds


class IkHandle(object):
    """this is the base ik class, which will be used to create everything dealing with iks"""
    def __init__(self):
        #vars
        self.ikName = []


    def check_ik_joints(self, startJoint = None, endEffector = None):
        #check if startJoint and endEffector exists
        if cmds.objExists(startJoint):
            if cmds.objExists(endEffector):
                pass
            else:
                raise Exception('EndEffector to ' + startJoint + ' is missing!')
        else:
            raise Exception('StartJoint is missing, cannot create ikHandle!')        


    def check_ik_name(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #check if joints exist
        self.check_ik_joints(startJoint = startJoint, endEffector = endEffector)
        
        #get the side info of the startJoint and store it
        sideList = ['C_', 'L_', 'R_', 'c_', 'l_', 'r_']
        for i in sideList:
            if i in startJoint:
                side = startJoint[0]
                break
            elif i in endEffector:
                side = endEffector[0]
        
        #check names
        if side == None:
            if name == None:
                if suffix == None:
                    self.ikName = 'ikHandle'
                else:
                    self.ikName = 'ikHandle_' + suffix 
            else:
                if suffix == None:
                    self.ikName = name
                else:
                    self.ikName = name + '_' + suffix
        else:
            if name == None:
                if suffix == None:
                    self.ikName = side + '_ikHandle'
                else:
                    self.ikName = side + '_ikHandle_' + suffix 
            else:
                if suffix == None:
                    self.ikName = side + '_' + name + '_IK'
                else:
                    self.ikName = side + '_' + name + '_' + suffix 
                
        if name == None:
            if side == None:
                if suffix == None:
                    self.ikName = 'ikHandle'
                else:
                    self.ikName = 'ikHandle_' + suffix 
            else:
                if suffix == None:
                    self.ikName = side + '_ikHandle'
                else:
                    self.ikName = side + '_ikHandle_' + suffix
        else:
            if side == None:
                if suffix == None:
                    self.ikName = name
                else:
                    self.ikName = name + '_' + suffix 
            else:
                if suffix == None:
                    self.ikName = side + '_' + name + '_IK'
                else:
                    self.ikName = side + '_' + name + '_' + suffix 


    def ikSCsolver(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)
        
        #create the ikHandle
        ik = cmds.ikHandle(startJoint = startJoint, endEffector = endEffector, name = self.ikName, solver = 'ikSCsolver')
        
        #rename the effector
        eff = cmds.rename(ik[-1], ik[0] + 'EFF')
        
        #store the ikHandle and effector in a list to return
        ikHandle = [ik[0], eff]

        cmds.select(clear = 1)
        return ikHandle
    
    
    def ikRPsolver(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)
        
        #create the ikHandle
        ik = cmds.ikHandle(startJoint = startJoint, endEffector = endEffector, name = self.ikName, solver = 'ikRPsolver')
                
        #rename the effector
        eff = cmds.rename(ik[-1], ik[0] + 'EFF')
        
        #store the ikHandle and effector in a list to return
        ikHandle = [ik[0], eff]

        cmds.select(clear = 1)
        return ikHandle


    def ikSplineSolver(self, startJoint = None, endEffector = None, curve = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)
        
        #create the ikHandle
        if curve == None:
            ik = cmds.ikHandle(startJoint = startJoint, endEffector = endEffector, createCurve = True, name = self.ikName, solver = 'ikSplineSolver')
        else:
            if cmds.objExists(curve):
                ik = cmds.ikHandle(startJoint = startJoint, endEffector = endEffector, curve = curve, createCurve = False, name = self.ikName, solver = 'ikSplineSolver')
            else:
                raise Exception('There is no specified curve: ' + curve )
            
        #rename the effector
        eff = cmds.rename(ik[1], ik[0] + 'EFF')
        
        #store the ikHandle and effector in a list to return
        if curve == None:
            #rename the automated curve
            crv = cmds.rename(ik[-1], ik[0] + 'CRV')
            ikHandle = [ik[0], eff, crv]
        else:
            ikHandle = [ik[0], eff, curve]

        cmds.select(clear = 1)
        return ikHandle

    