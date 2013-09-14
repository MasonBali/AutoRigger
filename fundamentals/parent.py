'''
Created on 12.09.2013

@author: Emre Tekinalp
'''

from maya import cmds


class Parent(object):
    """
    This class deals with everything concerning parenting operations
    """

    def __init__(self, child = None, parent = None):
        self.set_parent(child = child, parent = parent)
    #end def __init()

    def set_parent(self, child = None, parent = None):
        #check if child exists
        if child:
            #check if parent exists
            if parent:
                #check type of child 
                if isinstance(child, list):
                    #check type of parent 
                    if isinstance(parent, list):
                        #check length of child and parent
                        if len(child) == len(parent):
                            for c, p in zip(child, parent):
                                #check if child is already parented
                                rel = cmds.listRelatives(c, parent = True)
                                if not rel:
                                    cmds.parent(c, p)
                                else:
                                    if not rel == p:
                                        cmds.parent(c, p)
                            cmds.select(parent)
                        else:
                            for c in child:
                                for p in parent:
                                    if cmds.parent(c, p):
                                        cmds.parent(c, p)
                            cmds.select(parent[-1])
                    else:
                        for c in child:
                            rel = cmds.listRelatives(c, parent = True)
                            if not rel:
                                cmds.parent(c, parent)
                                cmds.select(parent)
                else:
                    #check if child is already parented
                    rel = cmds.listRelatives(child, parent = True)
                    if not rel:
                        cmds.parent(child, parent)
                    else:
                        if not rel == parent:
                            cmds.parent(child, parent)
                            cmds.select(parent)
            else:
                raise Exception('Specified parent: ' + parent + ' is not valid!')
        else:
            raise Exception('Specified child: ' + child + ' is not valid!')
    #end def set_parent()