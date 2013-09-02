'''
Created on 01.09.2013

@author: Emre Tekinalp
'''

from maya import cmds


class Attribute():
    """This class deals with everything concerning attributes of nodes, like lock, hide, set, get, add, connect, setDefault"""
    def __init__(self):
#        vars

#        methods
        pass        
    
    
    def lockAttribute(self, node = None, attrs = [None], lock = False, show = True):
        #check if node is valid
        if node != None:
            #check if the specified node is a list, string or unicode
            if type(node).__name__ == 'list':
                for i in node:
                    for attr in attrs:
                        if attr == 't':
                            cmds.setAttr(i + '.tx', lock = lock, keyable = show)
                            cmds.setAttr(i + '.ty', lock = lock, keyable = show)
                            cmds.setAttr(i + '.tz', lock = lock, keyable = show)
                        elif attr == 'r':
                            cmds.setAttr(i + '.rx', lock = lock, keyable = show)
                            cmds.setAttr(i + '.ry', lock = lock, keyable = show)
                            cmds.setAttr(i + '.rz', lock = lock, keyable = show)
                        elif attr == 's':                                        
                            cmds.setAttr(i + '.sx', lock = lock, keyable = show)
                            cmds.setAttr(i + '.sy', lock = lock, keyable = show)
                            cmds.setAttr(i + '.sz', lock = lock, keyable = show)
                        elif attr == 'v':
                            cmds.setAttr(i + '.v', lock = lock, keyable = show)
                        elif attr == None:
                            raise Exception('No valid attributes specified: ' + attr)
                        else:
                            for axis in 'XYZxyz':
                                if cmds.objExists(i + "." + attr + axis):
                                    cmds.setAttr(i + "." + attr + axis, lock = lock, keyable = show)
                                else:
                                    cmds.setAttr(i + "." + attr, lock = lock, keyable = show)                        
            else:
                for attr in attrs:
                    if attr == 't':
                        cmds.setAttr(node + '.tx', lock = lock, keyable = show)
                        cmds.setAttr(node + '.ty', lock = lock, keyable = show)
                        cmds.setAttr(node + '.tz', lock = lock, keyable = show)
                    elif attr == 'r':
                        cmds.setAttr(node + '.rx', lock = lock, keyable = show)
                        cmds.setAttr(node + '.ry', lock = lock, keyable = show)
                        cmds.setAttr(node + '.rz', lock = lock, keyable = show)
                    elif attr == 's':                                        
                        cmds.setAttr(node + '.sx', lock = lock, keyable = show)
                        cmds.setAttr(node + '.sy', lock = lock, keyable = show)
                        cmds.setAttr(node + '.sz', lock = lock, keyable = show)
                    elif attr == 'v':
                        cmds.setAttr(node + '.v', lock = lock, keyable = show)
                    else:
                        for axis in 'XYZxyz':
                            if cmds.objExists(node + '.' + attr + axis):
                                cmds.setAttr(node + '.' + attr + axis, lock = lock, keyable = show)
                            else:
                                cmds.setAttr(node + '.' + attr, lock = lock, keyable = show)  
        else:
            raise Exception('Given node: ' + node + ' is not valid or does not exist!' )
        

    def getAttribute(self):
        pass


"""                     
    def attrConnect(self, nodeA = None, attrA = None, nodeB = None, attrB = None):
        self.check.checkExisting(obj = nodeA)
        self.check.checkExisting(obj = nodeB)
        
        print type(nodeA).__name__, type(nodeB).__name__
        
        if type(nodeA).__name__ == 'list':
            if type(nodeB).__name__ == 'list':
                for a, b in zip(nodeA, nodeB):
                    cmds.connectAttr(a +"."+ attrA +"x", b +"."+ attrB +"x")
                    cmds.connectAttr(a +"."+ attrA +"y", b +"."+ attrB +"y")
                    cmds.connectAttr(a +"."+ attrA +"z", b +"."+ attrB +"z") 
                
            elif type(nodeB).__name__ == 'str':
                for a in nodeA:
                    cmds.connectAttr(a +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                    cmds.connectAttr(a +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                    cmds.connectAttr(a +"."+ attrA +"z", nodeB +"."+ attrB +"z")                                      
                
            elif type(nodeB).__name__ == 'unicode':
                    cmds.connectAttr(nodeA +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                    cmds.connectAttr(nodeA +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                    cmds.connectAttr(nodeA +"."+ attrA +"z", nodeB +"."+ attrB +"z")                                    
                
        elif type(nodeA).__name__ == 'str':
            if type(nodeB).__name__ == 'list':
                for b in nodeB:
                    cmds.connectAttr(nodeA +"."+ attrA +"x", b +"."+ attrB +"x")
                    cmds.connectAttr(nodeA +"."+ attrA +"y", b +"."+ attrB +"y")
                    cmds.connectAttr(nodeA +"."+ attrA +"z", b +"."+ attrB +"z") 
                    
            elif type(nodeB).__name__ == 'str':
                cmds.connectAttr(nodeA +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                cmds.connectAttr(nodeA +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                cmds.connectAttr(nodeA +"."+ attrA +"z", nodeB +"."+ attrB +"z")   
    
            elif type(nodeB).__name__ == 'unicode':
                    cmds.connectAttr(nodeA +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                    cmds.connectAttr(nodeA +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                    cmds.connectAttr(nodeA +"."+ attrA +"z", nodeB +"."+ attrB +"z")
                                                        
        elif type(nodeA).__name__ == 'unicode':
            if type(nodeB).__name__ == 'list':
                for b in nodeB:
                    cmds.connectAttr(nodeA +"."+ attrA +"x", b +"."+ attrB +"x")
                    cmds.connectAttr(nodeA +"."+ attrA +"y", b +"."+ attrB +"y")
                    cmds.connectAttr(nodeA +"."+ attrA +"z", b +"."+ attrB +"z") 
                    
            elif type(nodeB).__name__ == 'str':
                cmds.connectAttr(nodeA +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                cmds.connectAttr(nodeA +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                cmds.connectAttr(nodeA +"."+ attrA +"z", nodeB +"."+ attrB +"z")   
    
            elif type(nodeB).__name__ == 'unicode':
                    cmds.connectAttr(nodeA +"."+ attrA +"x", nodeB +"."+ attrB +"x")
                    cmds.connectAttr(nodeA +"."+ attrA +"y", nodeB +"."+ attrB +"y")
                    cmds.connectAttr(nodeA +"."+ attrA +"z", nodeB +"."+ attrB +"z")   
    
    
    
    def attrSetAll(self, node = None, attrs = None, value = 0.0): 
        if type(node).__name__ == 'list':
            for n in node:
                if type(attrs).__name__ == 'list':
                    for attr in attrs:
                        cmds.setAttr(n +"."+ attr +"x", value)
                        cmds.setAttr(n +"."+ attr +"y", value)
                        cmds.setAttr(n +"."+ attr +"z", value) 
                else:
                    cmds.setAttr(n +"."+ attrs +"x", value)
                    cmds.setAttr(n +"."+ attrs +"y", value)
                    cmds.setAttr(n +"."+ attrs +"z", value) 
        
        elif type(node).__name__ == 'unicode' or type(node).__name__ == "str":
            if type(attrs).__name__ == 'list':
                for attr in attrs:
                    cmds.setAttr(node +"."+ attr +"x", value)
                    cmds.setAttr(node +"."+ attr +"y", value)
                    cmds.setAttr(node +"."+ attr +"z", value) 
            else:
                cmds.setAttr(node +"."+ attrs +"x", value)
                cmds.setAttr(node +"."+ attrs +"y", value)
                cmds.setAttr(node +"."+ attrs +"z", value) 

        
    
    def addIdentity(self, obj = None, side = None, name = None, ident = None, typ = None, hook = None):
        self.check.checkExisting(obj = obj)
        
        ident = str(side) + "_" + str(ident)
        hook  = str(side) + "_" + str(name) + "_" + str(hook)
        
        cmds.addAttr(str(obj), longName = "side", shortName = "side", dataType = 'string', keyable = False)
        cmds.addAttr(str(obj), longName = "name", shortName = "name", dataType = 'string', keyable = False)
        cmds.addAttr(str(obj), longName = "id",   shortName = "id",   dataType = 'string', keyable = False)
        cmds.addAttr(str(obj), longName = "type", shortName = "type", dataType = 'string', keyable = False)
        cmds.addAttr(str(obj), longName = "hook", shortName = "hook", dataType = 'string', keyable = False)
        
        cmds.setAttr(str(obj) + ".side", side,  type = "string", lock = 1)
        cmds.setAttr(str(obj) + ".name", name,  type = "string", lock = 1)
        cmds.setAttr(str(obj) + ".id",   ident, type = "string", lock = 1)
        cmds.setAttr(str(obj) + ".type", typ,   type = "string", lock = 1)        
        cmds.setAttr(str(obj) + ".hook", hook,  type = "string", lock = 1)   
        
        
        
    def rotateOrder(self, obj = None, rotateOrder = None):
        self.check.checkExisting(obj = obj)

        if type(obj).__name__ == 'list':
            for i in obj:
                if rotateOrder == "xyz" or rotateOrder == None:
                    cmds.setAttr(i + ".rotateOrder", 0)
                elif rotateOrder == "yzx":
                    cmds.setAttr(i + ".rotateOrder", 1)
                elif rotateOrder == "zxy":
                    cmds.setAttr(i + ".rotateOrder", 2)
                elif rotateOrder == "xzy":
                    cmds.setAttr(i + ".rotateOrder", 3)    
                elif rotateOrder == "yxz":
                    cmds.setAttr(i + ".rotateOrder", 4)
                elif rotateOrder == "zyx":
                    cmds.setAttr(i + ".rotateOrder", 5)
                else:
                    self.check.checkExisting(info = "You have to specify 'xyz', 'yzx', 'zxy', xzy'', 'yxz', 'zyx', dude!")                                    

        else:
            if rotateOrder == "xyz" or rotateOrder == None:
                cmds.setAttr(obj + ".rotateOrder", 0)
            elif rotateOrder == "yzx":
                cmds.setAttr(obj + ".rotateOrder", 1)
            elif rotateOrder == "zxy":
                cmds.setAttr(obj + ".rotateOrder", 2)
            elif rotateOrder == "xzy":
                cmds.setAttr(obj + ".rotateOrder", 3)    
            elif rotateOrder == "yxz":
                cmds.setAttr(obj + ".rotateOrder", 4)
            elif rotateOrder == "zyx":
                cmds.setAttr(obj + ".rotateOrder", 5)
            else:
                self.check.checkExisting(info = "You have to specify 'xyz', 'yzx', 'zxy', xzy'', 'yxz', 'zyx', dude!")                                    



    def ihi(self, obj = None):
        if type(obj).__name__ == "list":
            for o in obj:
                sel = cmds.listRelatives(o, allDescendents = 1)
                for i in sel:
                    cmds.setAttr(i + ".ihi", 0)
        else:
            sel = cmds.listRelatives(obj, allDescendents = 1)
            for i in sel:
                cmds.setAttr(i + ".ihi", 0)



    def objectColor(self, obj = None, color = None):
        self.check.checkExisting(obj = obj)
        
        if type(obj).__name__ == "list":
            for i in obj:
                if color != None:
                    cmds.setAttr(i + ".overrideEnabled", 1)
                    if color == "grey":
                        cmds.setAttr(i + ".overrideColor", 0)
                    elif color == "black":
                        cmds.setAttr(i + ".overrideColor", 1)
                    elif color == "darkGrey":
                        cmds.setAttr(i + ".overrideColor", 2)
                    elif color == "lightGrey":
                        cmds.setAttr(i + ".overrideColor", 3)
                    elif color == "vineRed":
                        cmds.setAttr(i + ".overrideColor", 4)
                    elif color == "darkBlue":
                        cmds.setAttr(i + ".overrideColor", 5)                                                                                                                
                    elif color == "blue":
                        cmds.setAttr(i + ".overrideColor", 6)                                                                                                                
                    elif color == "darkGreen":
                        cmds.setAttr(i + ".overrideColor", 7)                                                                                                                
                    elif color == "darkViolett":
                        cmds.setAttr(i + ".overrideColor", 8)                                                                                                                
                    elif color == "pink":
                        cmds.setAttr(i + ".overrideColor", 9)                                                                                                                
                    elif color == "lightBrown":
                        cmds.setAttr(i + ".overrideColor", 10) 
                    elif color == "darkBrown":
                        cmds.setAttr(i + ".overrideColor", 11) 
                    elif color == "orange":
                        cmds.setAttr(i + ".overrideColor", 12) 
                    elif color == "red":
                        cmds.setAttr(i + ".overrideColor", 13) 
                    elif color == "green":
                        cmds.setAttr(i + ".overrideColor", 14) 
                    elif color == "darkPastelBlue":
                        cmds.setAttr(i + ".overrideColor", 15) 
                    elif color == "white":
                        cmds.setAttr(i + ".overrideColor", 16) 
                    elif color == "yellow":
                        cmds.setAttr(i + ".overrideColor", 17) 
                    elif color == "lightBlue":
                        cmds.setAttr(i + ".overrideColor", 18) 
                    elif color == "turqouis":
                        cmds.setAttr(i + ".overrideColor", 19) 
                    elif color == "lightRed":
                        cmds.setAttr(i + ".overrideColor", 20) 
                    elif color == "lightOrange":
                        cmds.setAttr(i + ".overrideColor", 21)                                                                                                                                                                                                     
                    elif color == "lightYellow":
                        cmds.setAttr(i + ".overrideColor", 22)                                                                                                                                                                                                     
                    elif color == "pastelGreen":
                        cmds.setAttr(i + ".overrideColor", 23)                                                                                                                                                                                                     
                    elif color == "pastelOrange":
                        cmds.setAttr(i + ".overrideColor", 24) 
                    elif color == "dirtyYellow":
                        cmds.setAttr(i + ".overrideColor", 25)
                    elif color == "lightGreen":
                        cmds.setAttr(i + ".overrideColor", 26)
                    elif color == "pastelTurqouis":
                        cmds.setAttr(i + ".overrideColor", 27) 
                    elif color == "marineBlue":
                        cmds.setAttr(i + ".overrideColor", 28) 
                    elif color == "pastelBlue":
                        cmds.setAttr(i + ".overrideColor", 29)                                                                                                                                                                                                                                                                                                                  
                    elif color == "pastelViolett":
                        cmds.setAttr(i + ".overrideColor", 30)                                                                                                                                                                                                                                                                                                                  
                    elif color == "pastelPink":
                        cmds.setAttr(i + ".overrideColor", 31)
                    else:
                        self.check.checkExisting(info = "Check out attributes.objectColor. You have to specify one of the given colors, dude!")                                                                                                                                                                                                                                                                                                                                                                       
                    cmds.setAttr(i + ".overrideEnabled", lock = 1)                               
                elif color == None:
                    cmds.setAttr(i + ".overrideEnabled", 1)
                    
                else:
                    self.check.checkExisting(info = "Check out attributes.objectColor. You have to specify one of the given colors, dude!")                                                                                                                                                                                                                                                                                                                                                                       
        
        else:
            if color != None:
                cmds.setAttr(obj + ".overrideEnabled", 1)
                if color == "grey":
                    cmds.setAttr(obj + ".overrideColor", 0)
                elif color == "black":
                    cmds.setAttr(obj + ".overrideColor", 1)
                elif color == "darkGrey":
                    cmds.setAttr(obj + ".overrideColor", 2)
                elif color == "lightGrey":
                    cmds.setAttr(obj + ".overrideColor", 3)
                elif color == "vineRed":
                    cmds.setAttr(obj + ".overrideColor", 4)
                elif color == "darkBlue":
                    cmds.setAttr(obj + ".overrideColor", 5)                                                                                                                
                elif color == "blue":
                    cmds.setAttr(obj + ".overrideColor", 6)                                                                                                                
                elif color == "darkGreen":
                    cmds.setAttr(obj + ".overrideColor", 7)                                                                                                                
                elif color == "darkViolett":
                    cmds.setAttr(obj + ".overrideColor", 8)                                                                                                                
                elif color == "pink":
                    cmds.setAttr(obj + ".overrideColor", 9)                                                                                                                
                elif color == "lightBrown":
                    cmds.setAttr(obj + ".overrideColor", 10) 
                elif color == "darkBrown":
                    cmds.setAttr(obj + ".overrideColor", 11) 
                elif color == "orange":
                    cmds.setAttr(obj + ".overrideColor", 12) 
                elif color == "red":
                    cmds.setAttr(obj + ".overrideColor", 13) 
                elif color == "green":
                    cmds.setAttr(obj + ".overrideColor", 14) 
                elif color == "darkPastelBlue":
                    cmds.setAttr(obj + ".overrideColor", 15) 
                elif color == "white":
                    cmds.setAttr(obj + ".overrideColor", 16) 
                elif color == "yellow":
                    cmds.setAttr(obj + ".overrideColor", 17) 
                elif color == "lightBlue":
                    cmds.setAttr(obj + ".overrideColor", 18) 
                elif color == "turqouis":
                    cmds.setAttr(obj + ".overrideColor", 19) 
                elif color == "lightRed":
                    cmds.setAttr(obj + ".overrideColor", 20) 
                elif color == "lightOrange":
                    cmds.setAttr(obj + ".overrideColor", 21)                                                                                                                                                                                                     
                elif color == "lightYellow":
                    cmds.setAttr(obj + ".overrideColor", 22)                                                                                                                                                                                                     
                elif color == "pastelGreen":
                    cmds.setAttr(obj + ".overrideColor", 23)                                                                                                                                                                                                     
                elif color == "pastelOrange":
                    cmds.setAttr(obj + ".overrideColor", 24) 
                elif color == "dirtyYellow":
                    cmds.setAttr(obj + ".overrideColor", 25)
                elif color == "lightGreen":
                    cmds.setAttr(obj + ".overrideColor", 26)
                elif color == "pastelTurqouis":
                    cmds.setAttr(obj + ".overrideColor", 27) 
                elif color == "marineBlue":
                    cmds.setAttr(obj + ".overrideColor", 28)                                                                                                                                                                                                                                                                                                                  
                elif color == "pastelBlue":
                    cmds.setAttr(obj + ".overrideColor", 29)                                                                                                                                                                                                                                                                                                                  
                elif color == "pastelViolett":
                    cmds.setAttr(obj + ".overrideColor", 30)
                elif color == "pastelPink":
                    cmds.setAttr(obj + ".overrideColor", 31)
                else:
                    self.check.checkExisting(info = "Check out attributes.objectColor. You have to specify one of the given colors, dude!")                                                                                                                                                                                                                                                                                                                                                                       
                
                cmds.setAttr(obj + ".overrideEnabled", lock = 1)                                                                                                                                                                                                                                                                                                                                             
                                                
            elif color == None:
                cmds.setAttr(obj + ".overrideEnabled", 1)
                
            else:
                self.check.checkExisting(info = "Check out attributes.objectColor. You have to specify one of the given colors, dude!")                                                                                                                                                                                                                                                                                                                                                                       
            
            
            
"""