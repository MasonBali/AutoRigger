'''
Created on 31.08.2013

@author: Emre Tekinalp
'''

from maya import cmds
from fundamentals import joint, ik
        
        
class Chain(object):
    """this is the base jointChain class, which will be used to create jointChains"""
    def __init__(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        #vars
        self.jointNames         = []
        self.mirroredJointNames = []
        
        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, offset = offset, amount = amount, mirror = mirror, radius = radius)
        
        
    def reload_modules(self):
        reload(joint)
        
        
    def create_chain(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        jntChain = []
        
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                        jntChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                            jntChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                            jntChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    jntChain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                        jntChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                            jntChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jntChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                            jntChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    jntChain.append(jnt.name)

        cmds.select(clear = 1)
        self.jointNames = jntChain
        
        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)

        return jntChain
    
    
    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmpJnt = cmds.joint(position = [0, 0, 0])
        
        #parent the chain to that joint
        cmds.parent(self.jointNames[0], tmpJnt)
        
        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirroredJointNames = cmds.mirrorJoint(self.jointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirroredJointNames = cmds.mirrorJoint(self.jointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirroredJointNames = cmds.mirrorJoint(self.jointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirroredJointNames = cmds.mirrorJoint(self.jointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirroredJointNames = cmds.mirrorJoint(self.jointNames[0], mirrorYZ = 1, mirrorBehavior = 1)
        
        #unparent the chain and delete the temporary joint
        cmds.parent(self.jointNames[0], self.mirroredJointNames[0], world = 1)        
        cmds.delete(tmpJnt)
        
        cmds.select(clear = 1)        
        return self.mirroredJointNames
        
        
    def __create(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)





class FkChain(object):
    """this is the fkChain class, which will be used to create fk based jointChains with fkControls"""
    def __init__(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        #vars
        self.fkJointNames         = []
        self.mirroredFkJointNames = []
        
        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, offset = offset, amount = amount, mirror = mirror, radius = radius)
        
        
    def reload_modules(self):
        reload(joint)
        
        
    def create_chain(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        fkChain = []
        
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                        fkChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fkChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fkChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    fkChain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                        fkChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fkChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fkChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fkChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    fkChain.append(jnt.name)

        cmds.select(clear = 1)
        self.fkJointNames = fkChain
        
        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)
        
        return fkChain
        

    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmpJnt = cmds.joint(position = [0, 0, 0])
        
        #parent the chain to that joint
        cmds.parent(self.fkJointNames[0], tmpJnt)
        
        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirroredFkJointNames = cmds.mirrorJoint(self.fkJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirroredFkJointNames = cmds.mirrorJoint(self.fkJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirroredFkJointNames = cmds.mirrorJoint(self.fkJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirroredFkJointNames = cmds.mirrorJoint(self.fkJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirroredFkJointNames = cmds.mirrorJoint(self.fkJointNames[0], mirrorYZ = 1, mirrorBehavior = 1)
        
        #unparent the chain and delete the temporary joint
        cmds.parent(self.fkJointNames[0], self.mirroredFkJointNames[0], world = 1)        
        cmds.delete(tmpJnt)
        
        cmds.select(clear = 1)        
        return self.mirroredFkJointNames
    
    
    def __create(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)
        




class IkChain(object):
    """this is the ikChain class, which will be used to create an ik based jointChain with an specified ikSolver"""
    def __init__(self, side = None, name = [], suffix = None, position = [], ikSolver = 'ikRPSolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        #vars
        self.ikJointNames   = []
        self.ikHandleNames  = []
        
        self.mirroredIkJointNames  = []
        self.mirroredIkHandleNames = []        
        
        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, ikSolver = ikSolver, ikCurve = ikCurve, ikName = ikName, offset = offset, amount = amount, mirror = mirror, radius = radius)
        
        
    def reload_modules(self):
        reload(joint)
        reload(ik)
        
        
    def create_chain(self, side = None, name = [], suffix = None, position = [], ikSolver = 'ikRPsolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        ikChain = []
        
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                        ikChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                        else:
                            off = [0 + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ikChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ikChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    ikChain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                        ikChain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ikChain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ikChain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ikChain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    ikChain.append(jnt.name)

        cmds.select(clear = 1)
        self.ikJointNames = ikChain
        
        #create ikHandle
        self.create_ik_handle(side = side, name = name, suffix = suffix, ikSolver = ikSolver, ikCurve = ikCurve, ikName = ikName)
        
        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)
                    
        return ikChain


    def create_ik_handle(self, side = None, name = [], suffix = None, ikSolver = 'ikRPSolver', ikCurve = None, ikName = None):
        ikH = ik.IkHandle()
        if ikName == None:
            if ikSolver == 'ikSCSolver':
                self.ikHandleNames = ikH.ikSCsolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], side = side, name = name[0], suffix = suffix)
            elif ikSolver == 'ikSplineSolver':
                self.ikHandleNames = ikH.ikSplineSolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], curve = ikCurve, side = side, name = name[0], suffix = suffix)
            else:
                self.ikHandleNames = ikH.ikRPsolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], side = side, name = name[0], suffix = suffix)
        else:
            if ikSolver == 'ikSCSolver':
                self.ikHandleNames = ikH.ikSCsolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], side = side, name = ikName, suffix = suffix)
            elif ikSolver == 'ikSplineSolver':
                self.ikHandleNames = ikH.ikSplineSolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], curve = ikCurve, side = side, name = ikName, suffix = suffix)
            else:
                self.ikHandleNames = ikH.ikRPsolver(startJoint = self.ikJointNames[0], endEffector = self.ikJointNames[-1], side = side, name = ikName, suffix = suffix)
        
        return self.ikHandleNames
    
    
    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmpJnt = cmds.joint(position = [0, 0, 0])
        
        #parent the chain to that joint
        cmds.parent(self.ikJointNames[0], tmpJnt)
        
        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirroredIkJointNames = cmds.mirrorJoint(self.ikJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirroredIkJointNames = cmds.mirrorJoint(self.ikJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirroredIkJointNames = cmds.mirrorJoint(self.ikJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirroredIkJointNames = cmds.mirrorJoint(self.ikJointNames[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirroredIkJointNames = cmds.mirrorJoint(self.ikJointNames[0], mirrorYZ = 1, mirrorBehavior = 1)
        
        #unparent the chain and delete the temporary joint
        cmds.parent(self.ikJointNames[0], self.mirroredIkJointNames[0], world = 1)        
        cmds.delete(tmpJnt)
        
        cmds.select(clear = 1)
        
        #rename the side of the mirrored effector correctly and store the ik and effector in a list
        mirroredIk  = self.mirroredIkJointNames[0][0] + self.ikHandleNames[-1][1:]
        mirroredEff = cmds.rename(self.mirroredIkJointNames[-1], self.mirroredIkJointNames[0][0] + self.ikHandleNames[-1][1:])
        self.mirroredIkHandleNames = [mirroredIk, mirroredEff]
        self.mirroredIkJointNames.pop(-1)
    
        
    def __create(self, side = None, name = [], suffix = None, position = [], ikSolver = 'ikRPsolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)

