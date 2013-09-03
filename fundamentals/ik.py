'''
Created on 28.08.2013

@author: Emre Tekinalp
'''

from maya import cmds


class IkHandle(object):
    """this is the base ik class, which will be used to create everything dealing with iks"""

    def __init__(self):
        #vars
        self.ik_name = []
    #end def __init__()

    def check_ik_joints(self, startJoint = None, endEffector = None):
        #check if startJoint and endEffector exists
        if cmds.objExists(startJoint):
            if cmds.objExists(endEffector):
                pass
            else:
                raise Exception('EndEffector to ' + startJoint + ' is missing!')
        else:
            raise Exception('StartJoint is missing, cannot create ik_handle!')        
    #end def check_ik_joints()

    def check_ik_name(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #check if joints exist
        self.check_ik_joints(startJoint = startJoint, endEffector = endEffector)

        #get the side info of the startJoint and store it
        side_list = ['C_', 'L_', 'R_', 'c_', 'l_', 'r_']
        for i in side_list:
            if i in startJoint:
                side = startJoint[0]
                break
            elif i in endEffector:
                side = endEffector[0]
    #end def check_ik_name()

        #check names
        if side == None:
            if name == None:
                if suffix == None:
                    self.ik_name = 'ik_handle'
                else:
                    self.ik_name = 'ik_handle_' + suffix 
            else:
                if suffix == None:
                    self.ik_name = name
                else:
                    self.ik_name = name + '_' + suffix
        else:
            if name == None:
                if suffix == None:
                    self.ik_name = side + '_ik_handle'
                else:
                    self.ik_name = side + '_ik_handle_' + suffix 
            else:
                if suffix == None:
                    self.ik_name = side + '_' + name + '_IK'
                else:
                    self.ik_name = side + '_' + name + '_' + suffix 

        if name == None:
            if side == None:
                if suffix == None:
                    self.ik_name = 'ik_handle'
                else:
                    self.ik_name = 'ik_handle_' + suffix 
            else:
                if suffix == None:
                    self.ik_name = side + '_ik_handle'
                else:
                    self.ik_name = side + '_ik_handle_' + suffix
        else:
            if side == None:
                if suffix == None:
                    self.ik_name = name
                else:
                    self.ik_name = name + '_' + suffix 
            else:
                if suffix == None:
                    self.ik_name = side + '_' + name + '_IK'
                else:
                    self.ik_name = side + '_' + name + '_' + suffix 
    #end def check_ik_name()

    def ikSCsolver(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)

        #create the ik_handle
        ik = cmds.ik_handle(startJoint = startJoint, endEffector = endEffector, name = self.ik_name, solver = 'ikSCsolver')

        #rename the effector
        eff = cmds.rename(ik[-1], ik[0] + 'EFF')

        #store the ik_handle and effector in a list to return
        ik_handle = [ik[0], eff]

        cmds.select(clear = 1)
        return ik_handle
    #end def ikSCsolver()

    def ikRPsolver(self, startJoint = None, endEffector = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)

        #create the ik_handle
        ik = cmds.ik_handle(startJoint = startJoint, endEffector = endEffector, name = self.ik_name, solver = 'ikRPsolver')

        #rename the effector
        eff = cmds.rename(ik[-1], ik[0] + 'EFF')

        #store the ik_handle and effector in a list to return
        ik_handle = [ik[0], eff]

        cmds.select(clear = 1)
        return ik_handle
    #end def ikRPsolver()

    def ikSplineSolver(self, startJoint = None, endEffector = None, curve = None, side = None, name = None, suffix = None):
        #do the proper naming checks
        self.check_ik_name(startJoint = startJoint, endEffector = endEffector, side = side, name = name, suffix = suffix)

        #create the ik_handle
        if curve == None:
            ik = cmds.ik_handle(startJoint = startJoint, endEffector = endEffector, createCurve = True, name = self.ik_name, solver = 'ikSplineSolver')
        else:
            if cmds.objExists(curve):
                ik = cmds.ik_handle(startJoint = startJoint, endEffector = endEffector, curve = curve, createCurve = False, name = self.ik_name, solver = 'ikSplineSolver')
            else:
                raise Exception('There is no specified curve: ' + curve )

        #rename the effector
        eff = cmds.rename(ik[1], ik[0] + 'EFF')

        #store the ik_handle and effector in a list to return
        if curve == None:
            #rename the automated curve
            crv = cmds.rename(ik[-1], ik[0] + 'CRV')
            ik_handle = [ik[0], eff, crv]
        else:
            ik_handle = [ik[0], eff, curve]

        cmds.select(clear = 1)
        return ik_handle
    #end def ikSplineSolver()
