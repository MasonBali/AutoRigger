'''
Created on 01.09.2013

@author: Emre Tekinalp
'''



from maya import cmds
from cmds import legCmds, footCmds, armCmds, spineCmds, neckCmds, headCmds


class build(object):
    def __init__(self):
        """DOCUMENTATION"""
        #vars
        
        #methods
        self.__create()
       
        
    def reload_modules(self):
        reload(legCmds)
        reload(footCmds)
        reload(armCmds)
        reload(spineCmds)
        reload(neckCmds)
        reload(headCmds)

    
    def guides(self):
        pass
        
        
    def puppets(self):
        puppetFoot  = footCmds.BipedFootPuppet(side = 'L', name = ['footAnkle', 'footBall', 'footToe'],    
                                               position = [[2, 1, 0], [2, 0, 2], [2, 0, 3]])
        
        puppetLeg   = legCmds.BipedLegPuppet(side = 'L', name = ['legThigh', 'legKnee', 'legAnkle'],     
                                             position = [[2, 11, 0], [2, 6, 1], [2, 1, 0]])    
        
        puppetSpine = spineCmds.BipedSpinePuppet(side = 'C', name = ['spinePelvis', 'spineVertebraeA', 'spineVertebraeB', 'spineVertebraeC'], 
                                                 position = [[0, 12, 0], [0, 14, 0], [0, 16, 0], [0, 18, 0]])
        
        puppetArm   = armCmds.BipedArmPuppet(side = 'L', name = ['armShoulder', 'armElbow', 'armWrist'], 
                                             position = [[3, 20, 0], [8, 20, -1], [12, 20, 0]])
        
        puppetNeck  = neckCmds.BipedNeckPuppet(side = 'C', name = ['neckBase', 'neckMid', 'neckEnd'], 
                                               position = [[0, 20, 0], [0, 21, 0], [0, 22, 0]])
        
        puppetHead  = headCmds.BipedHeadPuppet(side = 'C', name = ['headBase', 'headSkull', 'headTop'], 
                                               position = [[0, 22, 0], [0, 24, 0], [0, 27, 1]])
        
        
    def __create(self):
        self.reload_modules()
        self.guides()
        self.puppets()
        
        
build()