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
        self.joint_names         = []
        self.mirrored_joint_names = []

        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __init__()

    def reload_modules(self):
        reload(joint)
    #end def reload_modules()

    def create_chain(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        jnt_chain = []
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                        jnt_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                            jnt_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = off, parent = True, radius = radius)
                            jnt_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i], suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    jnt_chain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                        jnt_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                            jnt_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                                jnt_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = off, parent = True, radius = radius)
                            jnt_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i`, suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    jnt_chain.append(jnt.name)

        cmds.select(clear = 1)
        self.joint_names = jnt_chain

        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)

        return jnt_chain
    #end def create_chain()

    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmp_jnt = cmds.joint(position = [0, 0, 0])

        #parent the chain to that joint
        cmds.parent(self.joint_names[0], tmp_jnt)

        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirrored_joint_names = cmds.mirrorJoint(self.joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirrored_joint_names = cmds.mirrorJoint(self.joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirrored_joint_names = cmds.mirrorJoint(self.joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirrored_joint_names = cmds.mirrorJoint(self.joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirrored_joint_names = cmds.mirrorJoint(self.joint_names[0], mirrorYZ = 1, mirrorBehavior = 1)

        #unparent the chain and delete the temporary joint
        cmds.parent(self.joint_names[0], self.mirrored_joint_names[0], world = 1)        
        cmds.delete(tmp_jnt)

        cmds.select(clear = 1)        
        return self.mirrored_joint_names
    #end def mirror_chain()

    def __create(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __create()


class FkChain(object):
    """this is the fk_chain class, which will be used to create fk based jointChains with fkControls"""

    def __init__(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        #vars
        self.fk_joint_names         = []
        self.mirrored_fk_joint_names = []

        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __init__()

    def reload_modules(self):
        reload(joint)
    #end def reload_modules()

    def create_chain(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        fk_chain = []
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                        fk_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fk_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fk_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i] + 'FK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    fk_chain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                        fk_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fk_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                                fk_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = off, parent = True, radius = radius)
                            fk_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i` + 'FK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    fk_chain.append(jnt.name)

        cmds.select(clear = 1)
        self.fk_joint_names = fk_chain

        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)

        return fk_chain
    #end def create_chain()

    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmp_jnt = cmds.joint(position = [0, 0, 0])

        #parent the chain to that joint
        cmds.parent(self.fk_joint_names[0], tmp_jnt)

        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirrored_fk_joint_names = cmds.mirrorJoint(self.fk_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirrored_fk_joint_names = cmds.mirrorJoint(self.fk_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirrored_fk_joint_names = cmds.mirrorJoint(self.fk_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirrored_fk_joint_names = cmds.mirrorJoint(self.fk_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirrored_fk_joint_names = cmds.mirrorJoint(self.fk_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1)

        #unparent the chain and delete the temporary joint
        cmds.parent(self.fk_joint_names[0], self.mirrored_fk_joint_names[0], world = 1)        
        cmds.delete(tmp_jnt)

        cmds.select(clear = 1)        
        return self.mirrored_fk_joint_names
    #end def mirror_chain()

    def __create(self, side = None, name = [], suffix = None, position = [], offset = [0, 0, 0], amount = 3, mirror = False, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __create()




class IkChain(object):
    """this is the ik_chain class, which will be used to create an ik based jointChain with an specified ik_solver"""

    def __init__(self, side = None, name = [], suffix = None, position = [], ik_solver = 'ikRPSolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        #vars
        self.ik_joint_names   = []
        self.ik_handle_names  = []

        self.mirrored_ik_joint_names  = []
        self.mirrored_ik_handle_names = []        

        #methods
        self.__create(side = side, name = name, suffix = suffix, position = position, ik_solver = ik_solver, ikCurve = ikCurve, ikName = ikName, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __init__()

    def reload_modules(self):
        reload(joint)
        reload(ik)
    #end def reload_modules()

    def create_chain(self, side = None, name = [], suffix = None, position = [], ik_solver = 'ikRPsolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        ik_chain = []
        if type(name).__name__ == 'list':
            for i in range(len(name)):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                        ik_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                        else:
                            off = [0 + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ik_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ik_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name[i] + 'IK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    ik_chain.append(jnt.name)
        else:
            for i in range(amount):
                if position == []:
                    if offset == [0, 0, 0]:
                        off = [0, 0 + i, 0]
                        jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                        ik_chain.append(jnt.name)                        
                    elif offset[0] > 0:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [offset[0] + i, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                            else:
                                off = [offset[0] + i, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                        else:
                            off = [offset[0] + i, 0, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ik_chain.append(jnt.name)
                    else:
                        if offset[1] > 0:
                            if offset[2] > 0:
                                off = [0, offset[1] + i, offset[2] + i]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                            else:
                                off = [0, offset[1] + i, 0]
                                jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                                ik_chain.append(jnt.name)
                        else:
                            off = [0, 0 + i, 0]
                            jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = off, parent = True, radius = radius)
                            ik_chain.append(jnt.name)
                else:
                    jnt = joint.Joint(side = side, name = name + `i` + 'IK', suffix = suffix, position = position[i], parent = True, radius = radius)                    
                    ik_chain.append(jnt.name)

        cmds.select(clear = 1)
        self.ik_joint_names = ik_chain

        #create ikHandle
        self.create_ik_handle(side = side, name = name, suffix = suffix, ik_solver = ik_solver, ikCurve = ikCurve, ikName = ikName)

        #mirror joints if specified
        if mirror == True:
            self.mirror_chain(side = side)

        return ik_chain
    #end def create_chain()

    def create_ik_handle(self, side = None, name = [], suffix = None, ik_solver = 'ikRPSolver', ikCurve = None, ikName = None):
        ikH = ik.IkHandle()
        if ikName == None:
            if ik_solver == 'ikSCSolver':
                self.ik_handle_names = ikH.ikSCsolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], side = side, name = name[0], suffix = suffix)
            elif ik_solver == 'ikSplineSolver':
                self.ik_handle_names = ikH.ikSplineSolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], curve = ikCurve, side = side, name = name[0], suffix = suffix)
            else:
                self.ik_handle_names = ikH.ikRPsolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], side = side, name = name[0], suffix = suffix)
        else:
            if ik_solver == 'ikSCSolver':
                self.ik_handle_names = ikH.ikSCsolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], side = side, name = ikName, suffix = suffix)
            elif ik_solver == 'ikSplineSolver':
                self.ik_handle_names = ikH.ikSplineSolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], curve = ikCurve, side = side, name = ikName, suffix = suffix)
            else:
                self.ik_handle_names = ikH.ikRPsolver(startJoint = self.ik_joint_names[0], endEffector = self.ik_joint_names[-1], side = side, name = ikName, suffix = suffix)

        return self.ik_handle_names
    #end def create_ik_handle()

    def mirror_chain(self, side = None):
        #create one temporary joint at the origin
        tmp_jnt = cmds.joint(position = [0, 0, 0])

        #parent the chain to that joint
        cmds.parent(self.ik_joint_names[0], tmp_jnt)

        #mirror the chain and rename the mirrored side
        if side == 'L':
            self.mirrored_ik_joint_names = cmds.mirrorJoint(self.ik_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'R'))
        elif side == 'l':
            self.mirrored_ik_joint_names = cmds.mirrorJoint(self.ik_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'r'))
        elif side == 'R':
            self.mirrored_ik_joint_names = cmds.mirrorJoint(self.ik_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'L'))
        elif side == 'r':
            self.mirrored_ik_joint_names = cmds.mirrorJoint(self.ik_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1, searchReplace = (side, 'l'))
        else:
            self.mirrored_ik_joint_names = cmds.mirrorJoint(self.ik_joint_names[0], mirrorYZ = 1, mirrorBehavior = 1)

        #unparent the chain and delete the temporary joint
        cmds.parent(self.ik_joint_names[0], self.mirrored_ik_joint_names[0], world = 1)        
        cmds.delete(tmp_jnt)

        cmds.select(clear = 1)

        #rename the side of the mirrored effector correctly and store the ik and effector in a list
        mirrored_ik  = self.mirrored_ik_joint_names[0][0] + self.ik_handle_names[-1][1:]
        mirrored_eff = cmds.rename(self.mirrored_ik_joint_names[-1], self.mirrored_ik_joint_names[0][0] + self.ik_handle_names[-1][1:])
        self.mirrored_ik_handle_names = [mirrored_ik, mirrored_eff]
        self.mirrored_ik_joint_names.pop(-1)
    #end def mirror_chain()

    def __create(self, side = None, name = [], suffix = None, position = [], ik_solver = 'ikRPsolver', ikCurve = None, ikName = None, offset = [0, 0, 0], amount = 3, mirror = True, radius = 1):
        self.reload_modules()
        self.create_chain(side, name, suffix, position, offset = offset, amount = amount, mirror = mirror, radius = radius)
    #end def __create()
