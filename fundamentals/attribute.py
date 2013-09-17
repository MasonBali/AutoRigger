'''
Created on 01.09.2013

@author: Emre Tekinalp
'''

from maya import cmds


class Attribute(object):
    """
    This class deals with everything concerning attributes of nodes like lock, 
    hide, set, get, add, connect, setDefault
    """

    def __init__(self):
        pass        
    #end def __init__()

    def lockAttr(self, node = None, attribute = [None], lock = False, show = True):
        ########################################################################
        #check if node is valid
        if node:
            #check if the specified node is a list, string or unicode
            if isinstance(node, list):
                for i in node:
                    for attr in attribute:
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
                        elif not attr:
                            raise Exception('No valid attributes specified: ' 
                                            + attr)
                        else:
                            for axis in 'XYZxyz':
                                if cmds.objExists(i + "." + attr + axis):
                                    cmds.setAttr(i + "." + attr + axis, 
                                                 lock = lock, keyable = show)
                                else:
                                    cmds.setAttr(i + "." + attr, lock = lock, 
                                                 keyable = show)                        
            else:
                for attr in attribute:
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
                                cmds.setAttr(node + '.' + attr + axis, 
                                             lock = lock, keyable = show)
                            else:
                                cmds.setAttr(node + '.' + attr, 
                                             lock = lock, keyable = show)  
        else:
            if isinstance(node, list):
                for i in node:
                    raise Exception('Given node: ' + i + ' is not valid or' 
                                    'does not exist!')
            else:
                raise Exception('Given node: ' + node + ' is not valid or' 
                                'does not exist!')
    #end def lockAttribute()

    def getAttr(self, node = None, attribute = [None]):       
        ########################################################################
        value = []
        #check if specified node exists
        if node:
            #check if node is a list or not
            if isinstance(node, list):
                #check if attribute is a list
                if isinstance(attribute, list):
                    for i in node:
                        #check for the main transform attributes
                        for attr in attribute:
                            if attr == 't':
                                if cmds.objExists(i + '.t'):
                                    tx = cmds.getAttr(i + '.tx')
                                    ty = cmds.getAttr(i + '.ty')
                                    tz = cmds.getAttr(i + '.tz')
                                    if len(attribute) > 1:
                                        t = [tx, ty, tz]
                                        value.append(t)
                                    else:
                                        if len(node) > 1:
                                            t = [tx, ty, tz]
                                            value.append(t)
                                        else:
                                            value.append(tx)
                                            value.append(ty)
                                            value.append(tz)
                            elif attr == 'r':
                                if cmds.objExists(i + '.r'):
                                    rx = cmds.getAttr(i + '.rx')
                                    ry = cmds.getAttr(i + '.ry')
                                    rz = cmds.getAttr(i + '.rz')
                                    if len(attribute) > 1:                                
                                        r  = [rx, ry, rz]
                                        value.append(r)                                    
                                    else:
                                        if len(node) > 1:                                
                                            r = [rx, ry, rz]
                                            value.append(r)                                     
                                        else:
                                            value.append(rx)
                                            value.append(ry)
                                            value.append(rz)
                            elif attr == 's':
                                if cmds.objExists(i + '.s'):                            
                                    sx = cmds.getAttr(i + '.sx')
                                    sy = cmds.getAttr(i + '.sy')
                                    sz = cmds.getAttr(i + '.sz')
                                    if len(attribute) > 1:                                
                                        s  = [sx, sy, sz]
                                        value.append(s)                          
                                    else:
                                        if len(node) > 1:                                
                                            s = [sx, sy, sz]
                                            value.append(s)                                     
                                        else:
                                            value.append(sx)
                                            value.append(sy)
                                            value.append(sz)
                            elif attr == 'v':
                                if cmds.objExists(i + '.v'):                       
                                    vis  = cmds.getAttr(i + '.v')
                                    if len(attribute) > 1:
                                        v = [vis]
                                        value.append(v)
                                    else:
                                        if len(node) > 1:
                                            v = [vis]
                                            value.append(v)
                                        else:
                                            value.append(vis)
                            #check if specified attribute is valid
                            elif not attr:
                                if cmds.objExists(i + '.v'):
                                    raise Exception('No valid attribute specified: '
                                                    + attr)
                                else:
                                    raise Exception('Attribute: ' + str(attr) + 
                                                    ' does not exist on ' + i)
                            #get the value of a non standard transform attribute
                            else:
                                lock = 0
                                result = []                            
                                for axis in 'XYZ' or axis in 'xyz':
                                    if cmds.objExists(i + '.' + attr + axis):
                                        val = cmds.getAttr(i + '.' + attr + axis)
                                        if len(attribute) > 1: 
                                            result.append(val)
                                        else:                                       
                                            if len(node) > 1:                            
                                                result.append(val)
                                            else:
                                                value.append(val)
                                        lock = 0
                                    else:
                                        if (cmds.getAttr(i + "." + attr, type = 1) 
                                            == 'message'):
                                            pass
                                        else:
                                            val = cmds.getAttr(i + "." + attr)
                                            lock = 1
                                if len(attribute) > 1:
                                    if result:
                                        value.append(result)
                                else:
                                    if len(node) > 1:
                                        if result:
                                            value.append(result)
                                if lock == 1:
                                    value.append(val)                          
                else:
                    if attribute == 't':
                        for axis in 'xyz':
                            result = cmds.getAttr(i + '.' + attribute + axis)
                            value.append(result)
                    elif attribute == 'r':
                        for axis in 'xyz':
                            result = cmds.getAttr(i + '.' + attribute + axis)
                            value.append(result)
                    elif attribute == 's':
                        for axis in 'xyz':
                            result = cmds.getAttr(i + '.' + attribute + axis)
                            value.append(result)
                    else:
                        result = cmds.getAttr(i + '.' + attribute)
                        if isinstance(result, list):
                            value.append(result[0])
                        value.append(result)
            else:
                if isinstance(attribute, list):
                    #check for the main transform attributes
                    for attr in attribute:
                        if attr == 't':
                            if cmds.objExists(node + '.t'):
                                tx = cmds.getAttr(node + '.tx')
                                ty = cmds.getAttr(node + '.ty')
                                tz = cmds.getAttr(node + '.tz')
                                if len(attribute) > 1:
                                    t = [tx, ty, tz]
                                    value.append(t)
                                else:
                                    if len(node) > 1:
                                        t = [tx, ty, tz]
                                        value.append(t)
                                    else:
                                        value.append(tx)
                                        value.append(ty)
                                        value.append(tz)
                        elif attr == 'r':
                            if cmds.objExists(node + '.r'):
                                rx = cmds.getAttr(node + '.rx')
                                ry = cmds.getAttr(node + '.ry')
                                rz = cmds.getAttr(node + '.rz')
                                if len(attribute) > 1:                                
                                    r  = [rx, ry, rz]
                                    value.append(r)                                    
                                else:
                                    if len(node) > 1:                                
                                        r = [rx, ry, rz]
                                        value.append(r)                                     
                                    else:
                                        value.append(rx)
                                        value.append(ry)
                                        value.append(rz)
                        elif attr == 's':
                            if cmds.objExists(node + '.s'):                            
                                sx = cmds.getAttr(node + '.sx')
                                sy = cmds.getAttr(node + '.sy')
                                sz = cmds.getAttr(node + '.sz')
                                if len(attribute) > 1:                                
                                    s  = [sx, sy, sz]
                                    value.append(s)                          
                                else:
                                    if len(node) > 1:                                
                                        s = [sx, sy, sz]
                                        value.append(s)                                     
                                    else:
                                        value.append(sx)
                                        value.append(sy)
                                        value.append(sz)
                        elif attr == 'v':
                            if cmds.objExists(node + '.v'):                       
                                vis  = cmds.getAttr(node + '.v')
                                if len(attribute) > 1:
                                    v = [vis]
                                    value.append(v)
                                else:
                                    if len(node) > 1:
                                        v = [vis]
                                        value.append(v)
                                    else:
                                        value.append(vis)
                        #check if specified attribute is valid
                        elif not attr:
                            if cmds.objExists(node + '.v'):
                                raise Exception('No valid attribute specified: ' 
                                                + attr)
                            else:
                                raise Exception('Attribute: ' + str(attr) + 
                                                ' does not exist on ' + node)
                        #get the value of a non standard transform attribute
                        else:
                            lock = 0
                            result = []                            
                            for axis in 'XYZ' or axis in 'xyz':
                                if cmds.objExists(node + '.' + attr + axis):
                                    val = cmds.getAttr(node + '.' + attr + axis)
                                    if len(attribute) > 1: 
                                        result.append(val)
                                    else:                                       
                                        if len(node) > 1:                            
                                            result.append(val)
                                        else:
                                            value.append(val)
                                    lock = 0
                                else:
                                    val = cmds.getAttr(node + "." + attr)
                                    lock = 1
                            if len(attribute) > 1:
                                if result:
                                    value.append(result)
                            else:
                                if len(node) > 1:
                                    if result:
                                        value.append(result)
                            if lock == 1:
                                value.append(val)             
                else:
                    if attribute == 't':
                        for axis in 'xyz':
                            result = cmds.getAttr(node + '.' + attribute + axis)
                            value.append(result)
                    elif attribute == 'r':
                        for axis in 'xyz':
                            result = cmds.getAttr(node + '.' + attribute + axis)
                            value.append(result)                            
                    elif attribute == 's':
                        for axis in 'xyz':
                            result = cmds.getAttr(node + '.' + attribute + axis)
                            value.append(result)
                    else:
                        result = cmds.getAttr(node + '.' + attribute)
                        if isinstance(result, list):
                            value.append(result[0])
                        value.append(result)
        else:
            if isinstance(node, list):
                for i in node:
                    raise Exception('Specified node: ' + i + ' is not valid!')
            else:
                raise Exception('Specified node: ' + node + ' is not valid!')

        make_it_a_string_god_damnit = ''.join(map(str, value))
        return make_it_a_string_god_damnit
    #end def getAttribute()

    def setAttr(self, node = None, attribute = [None], value = None, lock = False):
        """
        @todo: add string check
        """

#        #check which kind of value is specified
#        if not isinstance(value, list):
#            try:
#                if int(value):
#                    value = int(value)
##                    print value, 'int'
#            except:
#                pass
#            try:
#                if float(value):
#                    value = float(value)
##                    print value, 'float'
#            except:
#                pass
#            try:
#                if bool(value):
#                    value = bool(value)
##                    print value, 'bool'
#            except:
#                pass
#            try:
#                if double(value):
#                    value = double(value)
##                    print value, 'double'
#            except:
#                print value
#                pass
        #check if node exists
        if node:
            #check if specified node is a list
            if isinstance(node, list):
                for i in range(len(node)):
                    #check if attribute is not empty
                    if attribute:
                        #check if attribute stores lists
                        for attr in range(len(attribute)):
                            if not isinstance(attribute[attr], list):
                                #check if attributes contain 'xyz' or 'XYZ'
                                for axis in range(len('xyz')):
                                    if cmds.objExists(node[i] + '.' + attribute[attr] + 'xyz'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value[i][axis])                                                
                                                else:
                                                    #set the attributes
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value[attr][axis])
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value)
                                    else:
                                        break
                                for axis in range(len('XYZ')):
                                    if cmds.objExists(node[i] + '.' + attribute[attr] + 'XYZ'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value[i][axis])                                                
                                                else:
                                                    #set the attributes 
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value[attr][axis])
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value)
                                    else:
                                        break
                                if cmds.objExists(node[i] + '.' + attribute[attr]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            check = 0                                            
                                            #set the attributes
                                            for axis in range(len('xyz')):
                                                if cmds.objExists(node[i] + '.' + attribute[attr] + 'xyz'[axis]):
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value[axis])
                                                elif cmds.objExists(node[i] + '.' + attribute[attr] + 'XYZ'[axis]):
                                                    cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value[axis])
                                                else:
                                                    check = 1
                                                    break
                                            if check == 1:
                                                cmds.setAttr(node[i] + '.' + attribute[attr], value[attr])
                                        else:
                                            check = 0
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node[i] + '.' + attribute[attr], value[i][attr])                                                
                                            else:
                                                for axis in range(len('xyz')):
                                                    if cmds.objExists(node[i] + '.' + attribute[attr] + 'xyz'[axis]):
                                                        cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value[attr][axis])
                                                    elif cmds.objExists(node[i] + '.' + attribute[attr] + 'XYZ'[axis]):
                                                        cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value[attr][axis])
                                                    else:
                                                        check = 1
                                                        break
                                                if check == 1:
                                                    cmds.setAttr(node[i] + '.' + attribute[attr], value[attr])                                                
                                    else:
                                        check = 0                                            
                                        #set the attributes
                                        for axis in range(len('xyz')):
                                            if cmds.objExists(node[i] + '.' + attribute[attr] + 'xyz'[axis]):
                                                cmds.setAttr(node[i] + '.' + attribute[attr] + 'xyz'[axis], value)
                                            elif cmds.objExists(node[i] + '.' + attribute[attr] + 'XYZ'[axis]):
                                                cmds.setAttr(node[i] + '.' + attribute[attr] + 'XYZ'[axis], value)
                                            else:
                                                check = 1
                                                break
                                        if check == 1:
                                            cmds.setAttr(node[i] + '.' + attribute[attr], value)
                            else:
                                #check if attributes contain 'xyz' or 'XYZ'
                                for axis in range(len('xyz')):
                                    if cmds.objExists(node[i] + '.' + attribute[i][attr] + 'xyz'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'xyz'[axis], value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'xyz'[axis], value[i][axis])                                                
                                                else:
                                                    #set the attributes
                                                    cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'xyz'[axis], value[attr][axis])                                                
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'xyz'[axis], value)                                            
                                    else:
                                        break
                                for axis in range(len('XYZ')):
                                    if cmds.objExists(node[i] + '.' + attribute[i][attr] + 'XYZ'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'XYZ'[axis], value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'XYZ'[axis], value[i][axis])                                                
                                                else:
                                                    #set the attributes 
                                                    cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'XYZ'[axis], value[attr][axis])                                    
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + attribute[i][attr] + 'xyz'[axis], value)
                                    else:
                                        break
                        if isinstance(attribute[0], list):
                            for attr in range(len(attribute[i])):
                                if cmds.objExists(node[i] + '.' + attribute[i][attr]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + attribute[i][attr], value[i][attr])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node[i] + '.' + attribute[i][attr], value[i][attr])                                                
                                            else:
                                                #set the attributes
                                                for axis in range(len('xyz')):
                                                    if cmds.objExists(node[i] + '.' + attribute[i][attr] + axis):
                                                        cmds.setAttr(node[i] + '.' + attribute[i][attr] + axis, value[i][attr])                                    
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node[i] + '.' + attribute[i][attr], value)
                    else:
                        raise Excpetion('Specified attribute is not valid or does not exist!')
            else:
                #check if attribute is not empty
                if attribute:
                    #check if attribute stores lists
                    for attr in range(len(attribute)):
                        if not isinstance(attribute[attr], list):
                            #check if attributes contain 'xyz' or 'XYZ'
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attribute[attr] + 'xyz'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists 
                                        #are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value[0][axis])                                                
                                            else:
                                                #set the attributes
                                                cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value)
                                else:
                                    break
                            for axis in range(len('XYZ')):
                                if cmds.objExists(node + '.' + attribute[attr] + 'XYZ'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value[0][axis])                                                
                                            else:
                                                #set the attributes 
                                                cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value)                                                
                                else:
                                    break
                            if cmds.objExists(node + '.' + attribute[attr]):
                                #check type of value
                                if isinstance(value, list):
                                    #check if more lists are stored in value
                                    if not isinstance (value[0], list):
                                        check = 0                                            
                                        #set the attributes
                                        for axis in range(len('xyz')):
                                            if cmds.objExists(node + '.' + attribute[attr] + 'xyz'[axis]):
                                                cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value[axis])
                                            elif cmds.objExists(node + '.' + attribute[attr] + 'XYZ'[axis]):
                                                cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value[axis])
                                            else:
                                                check = 1
                                                break
                                        if check == 1:
                                            cmds.setAttr(node + '.' + attribute[attr], value[attr])
                                    else:
                                        check = 0
                                        if not len(attribute) > 1:
                                            cmds.setAttr(node + '.' + attribute[attr], value[0][attr])                                                
                                        else:
                                            for axis in range(len('xyz')):
                                                if cmds.objExists(node + '.' + attribute[attr] + 'xyz'[axis]):
                                                    cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value[attr][axis])
                                                elif cmds.objExists(node + '.' + attribute[attr] + 'XYZ'[axis]):
                                                    cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value[attr][axis])
                                                else:
                                                    check = 1                                                    
                                                    break
                                            if check == 1:
                                                cmds.setAttr(node + '.' + attribute[attr], value[attr])
                                else:
                                    check = 0                                            
                                    #set the attributes
                                    for axis in range(len('xyz')):
                                        if cmds.objExists(node + '.' + attribute[attr] + 'xyz'[axis]):
                                            cmds.setAttr(node + '.' + attribute[attr] + 'xyz'[axis], value)
                                        elif cmds.objExists(node + '.' + attribute[attr] + 'XYZ'[axis]):
                                            cmds.setAttr(node + '.' + attribute[attr] + 'XYZ'[axis], value)
                                        else:
                                            check = 1
                                            break
                                    if check == 1:
                                        cmds.setAttr(node + '.' + attribute[attr], bool(value))
                        else:
                            #check if attributes contain 'xyz' or 'XYZ'
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attribute[0][attr] + 'xyz'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' + attribute[i][attr] + 'xyz'[axis], value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' + attribute[i][attr] + 'xyz'[axis], value[0][axis])                                                
                                            else:
                                                #set the attributes
                                                cmds.setAttr(node + '.' + attribute[i][attr] + 'xyz'[axis], value[attr][axis])                                                
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[i][attr] + 'xyz'[axis], value)                                        
                                else:
                                    break
                            for axis in range(len('XYZ')):
                                if cmds.objExists(node + '.' + attribute[0][attr] + 'XYZ'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' + attribute[0][attr] + 'XYZ'[axis], value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' + attribute[0][attr] + 'XYZ'[axis], value[0][axis])                                                
                                            else:
                                                #set the attributes 
                                                cmds.setAttr(node + '.' + attribute[0][attr] + 'XYZ'[axis], value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[0][attr] + 'XYZ'[axis], value)                                                
                                else:
                                    break
                    if isinstance(attribute[0], list):
                        for attr in range(len(attribute[0])):
                            if cmds.objExists(node + '.' + attribute[0][attr]):
                                #check type of value
                                if isinstance(value, list):
                                    #check if more lists are stored in value
                                    if not isinstance (value[0], list):
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[0][attr], value[0][attr])
                                    else:
                                        if not len(attribute) > 1:
                                            cmds.setAttr(node + '.' + attribute[0][attr], value[0][attr])                                                
                                        else:
                                            #set the attributes
                                            for axis in range(len('xyz')):
                                                if cmds.objExists(node + '.' + attribute[0][attr] + axis):
                                                    cmds.setAttr(node + '.' + attribute[0][attr] + axis, value[0][attr])
                                                elif cmds.objExists(node + '.' + attribute[0][attr] + axis.upper()):
                                                    cmds.setAttr(node + '.' + attribute[0][attr] + axis.upper(), value[0][attr])                                                    
                                else:
                                    #set the attributes
                                    cmds.setAttr(node + '.' + attribute[0][attr], value)
        else:
            raise Exception('Specified node is not valid or does not exist!')
    #end def setAttribute()

    def connectAttr(self, node = [None, None], attribute = [None, None]):
        """
        @todo: add multiNodes in node, ie. node = [[list],[list]]
        @todo: add multiAttributes in attribute, ie. attribute = [[list],[list]]
        """
        #check if node exist
        if node:
            #check if attribute exist
            if attribute:
                if isinstance(node, list):
                    #check len of node
                    if not isinstance(node[0], list):
                        #check len of attribute
                        if not isinstance(attribute[0], list):
                            if not isinstance(attribute[1], list):
                                check = 0
                                for axis in range(len('xyz')):
                                    if cmds.objExists(node[0] + '.' + attribute[0] + 'xyz'[axis]):
                                        if cmds.objExists(node[1] + '.' + attribute[1] + 'xyz'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'xyz'[axis], node[1] + '.' + attribute[1] + 'xyz'[axis])
                                            except:
                                                raise Exception(node[0] + '.' + attribute[0] + 'xyz'[axis] + ' is already connected to ' + node[1] + '.' + attribute[1] + 'xyz'[axis])
                                        elif cmds.objExists(node[1] + '.' + attribute[1] + 'XYZ'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'xyz'[axis], node[1] + '.' + attribute[1] + 'XYZ'[axis])
                                            except:
                                                raise Exception(node[0] + '.' + attribute[0] + 'xyz'[axis] + ' is already connected to ' + node[1] + '.' + attribute[1] + 'XYZ'[axis])
                                        else:
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'xyz'[axis], node[1] + '.' + attribute[1])
                                            except:
                                                raise Exception(node[0] + '.' + attribute[0] + 'xyz'[axis] + ' is already connected to ' + node[1] + '.' + attribute[1])
                                    elif cmds.objExists(node[0] + '.' + attribute[0] + 'XYZ'[axis]):
                                        if cmds.objExists(node[1] + '.' + attribute[1] + 'xyz'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'XYZ'[axis], node[1] + '.' + attribute[1] + 'xyz'[axis])
                                            except:
                                                raise Exception(node[0] + '.' + attribute[0] + 'XYZ'[axis] + ' is already connected to ' + node[1] + '.' + attribute[1] + 'xyz'[axis])
                                        elif cmds.objExists(node[1] + '.' + attribute[1] + 'XYZ'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'XYZ'[axis], node[1] + '.' + attribute[1] + 'XYZ'[axis])
                                            except:
                                                raise Exception(node[0] + '.' + attribute[0] + 'XYZ'[axis] + ' is already connected to ' + node[1] + '.' + attribute[1] + 'XYZ'[axis])
                                        else:
                                            try:
                                                cmds.connectAttr(node[0] + '.' + attribute[0] + 'XYZ'[axis], node[1] + '.' + attribute[1])
                                            except:
                                                check = 1
                                    else:
                                        check = 1
                                if check == 1:
                                    try:
                                        cmds.connectAttr(node[0] + '.' + attribute[0], node[1] + '.' + attribute[1])
                                    except:
                                        raise Exception(node[0] + '.' + attribute[0] + ' is already connected to ' + node[1] + '.' + attribute[1])
                        else:
                            print '@todo: multiAttributes'
                    else:
                        print '@todo: multiNodes'
            else:
                raise Exception('Specified attributes: ' + attribute + ' are not valid!')
        else:
            raise Exception('Specified nodes: ' + node + ' are not valid!')
    #end def connectAttr()

    def addAttr(self, node = None, attrName = None, attrType = 'float', min = 0, max = 1, default = 1, enum = [None, None], keyable = True, channelBox = False):
        ########################################################################
        #check if node exists
        if node:
            #check if node is list
            if isinstance(node, list):
                for i in node:
                    if not attrType == 'string':
                        if not channelBox:
                            if attrType == 'enum':
                                enumList = []
                                for e in range(len(enum)):
                                    if e == (len(enum) - 1):
                                        enumList.append(enum[e])   
                                    else:
                                        enumList.append(enum[e] + ':')
                                enumList = ''.join(enumList)
                                cmds.addAttr(i, longName = attrName, shortName = attrName, attributeType = 'enum', enumerator = enumList, min = min, max = max, defaultValue = default, keyable = keyable)
                            elif attrType == 'vector':
                                cmds.addAttr(i, longName = attrName, shortName = attrName, attributeType = 'double3', min = min, max = max, defaultValue = default, keyable = keyable)
                                for axis in 'XYZ':
                                    cmds.addAttr(i, longName = attrName + axis, shortName = attrName + axis, attributeType = 'double', parent = attrName, keyable = keyable)
                            else:
                                cmds.addAttr(i, longName = attrName, shortName = attrName, attributeType = attrType, min = min, max = max, defaultValue = default, keyable = keyable)
                        else:
                            cmds.addAttr(i, longName = attrName, shortName = attrName, attributeType = attrType, min = min, max = max, defaultValue = default, keyable = keyable)
                            cmds.addAttr(i, edit = True, channelBox = True)
                    else:
                        if not channelBox:
                            cmds.addAttr(i, longName = attrName, shortName = attrName, dataType = attrType, keyable = keyable)
                        else:
                            cmds.addAttr(i, longName = attrName, shortName = attrName, dataType = attrType, keyable = keyable)
                            cmds.addAttr(i, edit = True, channelBox = True)
            else:
                if not attrType == 'string' or attrType == 'separator':
                    if not channelBox:
                        if attrType == 'enum':
                            enumList = []
                            for e in range(len(enum)):
                                if e == (len(enum) - 1):
                                    enumList.append(enum[e])   
                                else:
                                    enumList.append(enum[e] + ':')
                            enumList = ''.join(enumList)
                            cmds.addAttr(node, longName = attrName, shortName = attrName, attributeType = 'enum', enumerator = enumList, min = min, max = max, defaultValue = default, keyable = keyable)
                        elif attrType == 'vector':
                            cmds.addAttr(node, longName = attrName, shortName = attrName, attributeType = 'double3', min = min, max = max, defaultValue = default, keyable = keyable)
                            for axis in 'XYZ':
                                cmds.addAttr(node, longName = attrName + axis, shortName = attrName + axis, attributeType = 'double', parent = attrName, keyable = keyable)
                        else:
                            cmds.addAttr(node, longName = attrName, shortName = attrName, attributeType = attrType, min = min, max = max, defaultValue = default, keyable = keyable)
                    else:
                        cmds.addAttr(node, longName = attrName, shortName = attrName, attributeType = attrType, min = min, max = max, defaultValue = default, keyable = keyable)
                        cmds.addAttr(node, edit = True, channelBox = True)
                else:
                    if not channelBox:
                        cmds.addAttr(node, longName = attrName, shortName = attrName, dataType = attrType, keyable = keyable)
                    else:
                        cmds.addAttr(node, longName = attrName, shortName = attrName, dataType = attrType, keyable = keyable)
                        cmds.addAttr(node, edit = True, channelBox = True)
        else:
            raise Exception('Specified node: ' + 'node' + ' is not valid!') 
    #end def addAttr()

    def setDefault(self, node = None):
        ########################################################################
        #check if node exists
        if node:
            #check if node is a list
            if isinstance(node, list):
                for i in node:
                    #list attributes, get their default values and set them
                    list_attrs = cmds.listAttr(i, keyable = True)
                    for attr in list_attrs:
                        attr_query = cmds.attributeQuery(attr, node = i,
                                                        listDefault = True)[0]
                        cmds.setAttr(i + '.' + attr, attr_query)
            else:
                #list attributes, get their default values and set them
                list_attrs = cmds.listAttr(node, keyable = True)
                for attr in list_attrs:
                    attr_query = cmds.attributeQuery(attr, node = node,
                                                    listDefault = True)[0]
                    cmds.setAttr(node + '.' + attr, attr_query)
        else:
            raise Exception('Specified node: ' + node + ' is not valid!')
    #end def setDefault()

"""
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