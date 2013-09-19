import PySide
print(PySide.__version__)

from maya import cmds

cmds.joint()

print 'asdasd'
"""
data.load() backup
"""
#
#                    if not i.split(', ')[1].isdigit():
#                        if i.split(', ')[1] == str(True) or i.split(', ')[1] == str(False):
#                            attr.setAttr(node = i.split(',')[0].split('.')[0], 
#                                         attribute = i.split(',')[0].split('.')[1], 
#                                         value = i.split(', ')[1])
#                        else:
#                            attr.setAttr(node = i.split(',')[0].split('.')[0], 
#                                         attribute = i.split(',')[0].split('.')[1], 
#                                         value = i.split(', ')[1])
#                    else:
#                        attr.setAttr(node = i.split(',')[0].split('.')[0], 
#                                     attribute = i.split(',')[0].split('.')[1], 
#                                     value = i.split(', ')[1])
"""
attribute backup
"""

"""
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

    def setAttr(self, node = None, attribute = [None], value = None):

        @todo: add string check


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
                                    if cmds.objExists(node[i] + '.' + 
                                                      attribute[attr] + 
                                                      'xyz'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[attr] + 
                                                             'xyz'[axis], 
                                                             value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' + 
                                                                 attribute[attr] 
                                                                 + 'xyz'[axis], 
                                                                 value[i][axis])                                                
                                                else:
                                                    #set the attributes
                                                    cmds.setAttr(node[i] + '.' + 
                                                                 attribute[attr] 
                                                                 + 'xyz'[axis], 
                                                                 value[attr][axis])
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + 
                                                         attribute[attr] + 
                                                         'xyz'[axis], value)
                                    else:
                                        break
                                for axis in range(len('XYZ')):
                                    if cmds.objExists(node[i] + '.' + 
                                                      attribute[attr] + 
                                                      'XYZ'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are 
                                            #stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[attr] + 
                                                             'XYZ'[axis], 
                                                             value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[i][axis])                                                
                                                else:
                                                    #set the attributes 
                                                    cmds.setAttr(node[i] + '.' + 
                                                                 attribute[attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[attr][axis])
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' + 
                                                         attribute[attr] + 
                                                         'XYZ'[axis], value)
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
                                                if cmds.objExists(node[i] + '.' 
                                                                  + attribute[attr] 
                                                                  + 'xyz'[axis]):
                                                    cmds.setAttr(node[i] + '.' + 
                                                                 attribute[attr] 
                                                                 + 'xyz'[axis], 
                                                                 value[axis])
                                                elif cmds.objExists(node[i] + '.' 
                                                                    + attribute[attr] 
                                                                    + 'XYZ'[axis]):
                                                    cmds.setAttr(node[i] + '.' + 
                                                                 attribute[attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[axis])
                                                else:
                                                    check = 1
                                                    break
                                            if check == 1:
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[attr], 
                                                             value[attr])
                                        else:
                                            check = 0
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[attr], 
                                                             value[i][attr])                                                
                                            else:
                                                for axis in range(len('xyz')):
                                                    if cmds.objExists(node[i] + 
                                                                      '.' + 
                                                                      attribute[attr] 
                                                                      + 'xyz'[axis]):
                                                        cmds.setAttr(node[i] + 
                                                                     '.' + 
                                                                     attribute[attr] 
                                                                     + 'xyz'[axis], 
                                                                     value[attr][axis])
                                                    elif cmds.objExists(node[i] + 
                                                                        '.' + 
                                                                        attribute[attr] 
                                                                        + 'XYZ'[axis]):
                                                        cmds.setAttr(node[i] + '.' 
                                                                     + attribute[attr] 
                                                                     + 'XYZ'[axis], 
                                                                     value[attr][axis])
                                                    else:
                                                        check = 1
                                                        break
                                                if check == 1:
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[attr], 
                                                                 value[attr])                                                
                                    else:
                                        check = 0                                            
                                        #set the attributes
                                        for axis in range(len('xyz')):
                                            if cmds.objExists(node[i] + '.' 
                                                              + attribute[attr] 
                                                              + 'xyz'[axis]):
                                                cmds.setAttr(node[i] + '.' 
                                                             + attribute[attr] 
                                                             + 'xyz'[axis], value)
                                            elif cmds.objExists(node[i] + '.' 
                                                                + attribute[attr] 
                                                                + 'XYZ'[axis]):
                                                cmds.setAttr(node[i] + '.' 
                                                             + attribute[attr] 
                                                             + 'XYZ'[axis], value)
                                            else:
                                                check = 1
                                                break
                                        if check == 1:
                                            cmds.setAttr(node[i] + '.' + 
                                                         attribute[attr], value)
                            else:
                                #check if attributes contain 'xyz' or 'XYZ'
                                for axis in range(len('xyz')):
                                    if cmds.objExists(node[i] + '.' + 
                                                      attribute[i][attr] + 
                                                      'xyz'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[i][attr] 
                                                             + 'xyz'[axis],
                                                             value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[i][attr] 
                                                                 + 'xyz'[axis], 
                                                                 value[i][axis])                                                
                                                else:
                                                    #set the attributes
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[i][attr] 
                                                                 + 'xyz'[axis], 
                                                                 value[attr][axis])                                                
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' 
                                                         + attribute[i][attr] 
                                                         + 'xyz'[axis], value)                                            
                                    else:
                                        break
                                for axis in range(len('XYZ')):
                                    if cmds.objExists(node[i] + '.' 
                                                      + attribute[i][attr] + 
                                                      'XYZ'[axis]):
                                        #check type of value
                                        if isinstance(value, list):
                                            #check if more lists are stored in value
                                            if not isinstance (value[0], list):
                                                #set the attributes
                                                cmds.setAttr(node[i] + '.' + 
                                                             attribute[i][attr] 
                                                             + 'XYZ'[axis], 
                                                             value[axis])
                                            else:
                                                if not len(attribute) > 1:
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[i][attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[i][axis])                                                
                                                else:
                                                    #set the attributes 
                                                    cmds.setAttr(node[i] + '.' 
                                                                 + attribute[i][attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[attr][axis])                                    
                                        else:
                                            #set the attributes
                                            cmds.setAttr(node[i] + '.' 
                                                         + attribute[i][attr] 
                                                         + 'xyz'[axis], value)
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
                                            cmds.setAttr(node[i] + '.' 
                                                         + attribute[i][attr], 
                                                         value[i][attr])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node[i] + '.' 
                                                             + attribute[i][attr], 
                                                             value[i][attr])                                                
                                            else:
                                                #set the attributes
                                                for axis in range(len('xyz')):
                                                    if cmds.objExists(node[i] 
                                                                      + '.' + 
                                                                      attribute[i][attr] 
                                                                      + axis):
                                                        cmds.setAttr(node[i] 
                                                                     + '.' + 
                                                                     attribute[i][attr] 
                                                                     + axis, 
                                                                     value[i][attr])                                    
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node[i] + '.' 
                                                     + attribute[i][attr], value)
                    else:
                        raise Excpetion('Specified attribute is not' 
                                        'valid or does not exist!')
            else:
                #check if attribute is not empty
                if attribute:
                    #check if attribute stores lists
                    for attr in range(len(attribute)):
                        if not isinstance(attribute[attr], list):
                            #check if attributes contain 'xyz' or 'XYZ'
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attribute[attr] 
                                                  + 'xyz'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr] 
                                                         + 'xyz'[axis], 
                                                         value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr] 
                                                             + 'xyz'[axis], 
                                                             value[0][axis])                                                
                                            else:
                                                #set the attributes
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr] 
                                                             + 'xyz'[axis], 
                                                             value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[attr] 
                                                     + 'xyz'[axis], value)
                                else:
                                    break
                            for axis in range(len('XYZ')):
                                if cmds.objExists(node + '.' + attribute[attr] 
                                                  + 'XYZ'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr] 
                                                         + 'XYZ'[axis], 
                                                         value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr] 
                                                             + 'XYZ'[axis], 
                                                             value[0][axis])                                                
                                            else:
                                                #set the attributes 
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr] 
                                                             + 'XYZ'[axis], 
                                                             value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' + attribute[attr] 
                                                     + 'XYZ'[axis], value)                                                
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
                                            if cmds.objExists(node + '.' 
                                                              + attribute[attr] 
                                                              + 'xyz'[axis]):
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr] 
                                                             + 'xyz'[axis], 
                                                             value[axis])
                                            elif cmds.objExists(node + '.' 
                                                                + attribute[attr] 
                                                                + 'XYZ'[axis]):
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr]
                                                             + 'XYZ'[axis], 
                                                             value[axis])
                                            else:
                                                check = 1
                                                break
                                        if check == 1:
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr], 
                                                         value[attr])
                                    else:
                                        check = 0
                                        if not len(attribute) > 1:
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr], 
                                                         value[0][attr])                                                
                                        else:
                                            for axis in range(len('xyz')):
                                                if cmds.objExists(node + '.' 
                                                                  + attribute[attr] 
                                                                  + 'xyz'[axis]):
                                                    cmds.setAttr(node + '.' 
                                                                 + attribute[attr] 
                                                                 + 'xyz'[axis],
                                                                 value[attr][axis])
                                                elif cmds.objExists(node + '.' 
                                                                    + attribute[attr] 
                                                                    + 'XYZ'[axis]):
                                                    cmds.setAttr(node + '.' 
                                                                 + attribute[attr] 
                                                                 + 'XYZ'[axis], 
                                                                 value[attr][axis])
                                                else:
                                                    check = 1                                                    
                                                    break
                                            if check == 1:
                                                cmds.setAttr(node + '.' 
                                                             + attribute[attr], 
                                                             value[attr])
                                else:
                                    check = 0                                            
                                    #set the attributes
                                    for axis in range(len('xyz')):
                                        if cmds.objExists(node + '.' 
                                                          + attribute[attr] 
                                                          + 'xyz'[axis]):
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr] 
                                                         + 'xyz'[axis], value)
                                        elif cmds.objExists(node + '.' 
                                                            + attribute[attr] 
                                                            + 'XYZ'[axis]):
                                            cmds.setAttr(node + '.' 
                                                         + attribute[attr] 
                                                         + 'XYZ'[axis], value)
                                        else:
                                            check = 1
                                            break
                                    if check == 1:
                                        cmds.setAttr(node + '.' 
                                                     + attribute[attr], 
                                                     bool(value))
                        else:
                            #check if attributes contain 'xyz' or 'XYZ'
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attribute[0][attr] 
                                                  + 'xyz'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' 
                                                         + attribute[i][attr] 
                                                         + 'xyz'[axis], 
                                                         value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' 
                                                             + attribute[i][attr] 
                                                             + 'xyz'[axis], 
                                                             value[0][axis])                                                
                                            else:
                                                #set the attributes
                                                cmds.setAttr(node + '.' 
                                                             + attribute[i][attr] 
                                                             + 'xyz'[axis], 
                                                             value[attr][axis])                                                
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' 
                                                     + attribute[i][attr] 
                                                     + 'xyz'[axis], value)                                        
                                else:
                                    break
                            for axis in range(len('XYZ')):
                                if cmds.objExists(node + '.' + attribute[0][attr] 
                                                  + 'XYZ'[axis]):
                                    #check type of value
                                    if isinstance(value, list):
                                        #check if more lists are stored in value
                                        if not isinstance (value[0], list):
                                            #set the attributes
                                            cmds.setAttr(node + '.' 
                                                         + attribute[0][attr] 
                                                         + 'XYZ'[axis], 
                                                         value[axis])
                                        else:
                                            if not len(attribute) > 1:
                                                cmds.setAttr(node + '.' 
                                                             + attribute[0][attr] 
                                                             + 'XYZ'[axis], 
                                                             value[0][axis])                                                
                                            else:
                                                #set the attributes 
                                                cmds.setAttr(node + '.' 
                                                             + attribute[0][attr] 
                                                             + 'XYZ'[axis], 
                                                             value[attr][axis])
                                    else:
                                        #set the attributes
                                        cmds.setAttr(node + '.' 
                                                     + attribute[0][attr] 
                                                     + 'XYZ'[axis], value)                                                
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
                                        cmds.setAttr(node + '.' 
                                                     + attribute[0][attr], 
                                                     value[0][attr])
                                    else:
                                        if not len(attribute) > 1:
                                            cmds.setAttr(node + '.' 
                                                         + attribute[0][attr], 
                                                         value[0][attr])                                                
                                        else:
                                            #set the attributes
                                            for axis in range(len('xyz')):
                                                if cmds.objExists(node + '.' 
                                                                  + attribute[0][attr] + 
                                                                  axis):
                                                    cmds.setAttr(node + '.' 
                                                                 + attribute[0][attr] 
                                                                 + axis, 
                                                                 value[0][attr])
                                                elif cmds.objExists(node + '.' 
                                                                    + attribute[0][attr] 
                                                                    + axis.upper()):
                                                    cmds.setAttr(node + '.' 
                                                                 + attribute[0][attr] 
                                                                 + axis.upper(), 
                                                                 value[0][attr])                                                    
                                else:
                                    #set the attributes
                                    cmds.setAttr(node + '.' + attribute[0][attr], 
                                                 value)
        else:
            raise Exception('Specified node is not valid or does not exist!')
    #end def setAttribute()

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