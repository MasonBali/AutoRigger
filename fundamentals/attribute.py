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
        #--- check if node is valid
        if node:
            #--- check if the specified node is a list, string or unicode
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

    def getAttr(self, node = None, attribute = None):
        ########################################################################
        #--- final values will be stored in this list
        value = []
        #--- check if node and attributes are given
        if node:
            if attribute:
                #--- check nodes' and attributes' type
                if not isinstance(node, list):
                    if not isinstance(attribute, list):
                        #--- if attribute IS NOT a list
                        #--- check if arrays exist at given attribute
                        check = 0
                        for axis in range(len('xyz')):
                            if cmds.objExists(node + '.' + attribute
                                              + 'xyz'[axis]):
                                val = cmds.getAttr(node + '.' + attribute
                                                   + 'xyz'[axis])
                                value.append(val)
                            elif cmds.objExists(node + '.' + attribute
                                                + 'XYZ'[axis]):
                                val = cmds.getAttr(node + '.' + attribute
                                                   + 'XYZ'[axis])
                                value.append(val)
                            elif cmds.objExists(node + '.' + attribute
                                                + 'RGB'[axis]):
                                val = cmds.getAttr(node + '.' + attribute
                                                   + 'RGB'[axis])
                                value.append(val)
                            else:
                                check = 1
                        if check == 1:
                            val = cmds.getAttr(node + '.' + attribute)
                            value.append(val)
                    else:
                        #--- if attribute IS a list
                        for attr in attribute:
                            #--- check if arrays exist at given attribute
                            check = 0
                            vals = []
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attr
                                                  + 'xyz'[axis]):
                                    val = cmds.getAttr(node + '.' + attr
                                                       + 'xyz'[axis])
                                    vals.append(val)
                                elif cmds.objExists(node + '.' + attr
                                                    + 'XYZ'[axis]):
                                    val = cmds.getAttr(node + '.' + attr
                                                       + 'XYZ'[axis])
                                    vals.append(val)
                                elif cmds.objExists(node + '.' + attr
                                                    + 'RGB'[axis]):
                                    val = cmds.getAttr(node + '.' + attr
                                                       + 'RGB'[axis])
                                    vals.append(val)
                                else:
                                    check = 1
                            if check == 1:
                                val = cmds.getAttr(node + '.' + attr)
                                value.append(val)
                            else:
                                value.append(vals)
                else:
                    raise Exception('Please specify just strings or unicodes, '
                                    'not lists! Specified node is in a list!')
        if not len(value) > 1:
            return value[0]
        else:
            return value
    #end def getAttr()

    def setAttr(self, node = None, attribute = None, value = None):
        ########################################################################
        #--- check if node, attribute and value exists
        if node:
            if attribute:
                if value:
                    if isinstance(attribute, list):
                        for attr in attribute:
                            check = 0
                            #--- get the type of the attribute
                            info = cmds.getAttr(node + '.' + attr, type = True)
                            #--- check for arrays
                            for axis in range(len('xyz')):
                                if cmds.objExists(node + '.' + attr
                                                  + 'xyz'[axis]):
                                    if info == 'string':
                                        cmds.setAttr(node + '.' + attr
                                                     + 'xyz'[axis], str(value),
                                                     type = 'string')
                                    elif info == 'bool':
                                        cmds.setAttr(node + '.' + attr
                                                     + 'xyz'[axis], bool(value))
                                    else:
                                        cmds.setAttr(node + '.' + attr +
                                                     'xzy'[axis], value)
                                elif cmds.objExists(node + '.' + attr
                                                    + 'XYZ'[axis]):
                                    if info == 'string':
                                        cmds.setAttr(node + '.' + attr +
                                                     'XYZ'[axis], str(value),
                                                     type = 'string')
                                    elif info == 'bool':
                                        cmds.setAttr(node + '.' + attr +
                                                     'XYZ'[axis], bool(value))
                                    else:
                                        cmds.setAttr(node + '.' + attr +
                                                     'XYZ'[axis], value)
                                elif cmds.objExists(node + '.' + attr
                                                    + 'RGB'[axis]):
                                    if info == 'string':
                                        cmds.setAttr(node + '.' + attr +
                                                     'RGB'[axis], str(value),
                                                     type = 'string')
                                    elif info == 'bool':
                                        cmds.setAttr(node + '.' + attr +
                                                     'RGB'[axis], bool(value))
                                    else:
                                        cmds.setAttr(node + '.' + attr +
                                                     'RGB'[axis], value)
                                else:
                                    check = 1
                            if check == 1:
                                if info == 'string':
                                    cmds.setAttr(node + '.' + attr, str(value),
                                                 type = 'string')
                                elif info == 'bool':
                                    cmds.setAttr(node + '.' + attr, bool(value))
                                else:
                                    cmds.setAttr(node + '.' + attr, value)
                    else:
                        check = 0
                        #--- get the type of the attribute
                        info = cmds.getAttr(node + '.' + attribute, type = True)
                        #--- check for arrays
                        for axis in range(len('xyz')):
                            if cmds.objExists(node + '.' + attribute
                                              + 'xyz'[axis]):
                                if info == 'string':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'xyz'[axis], str(value),
                                                 type = 'string')
                                elif info == 'bool':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'xyz'[axis], bool(value))
                                else:
                                    cmds.setAttr(node + '.' + attribute +
                                                 'xyz'[axis], value)
                            elif cmds.objExists(node + '.' + attribute
                                                + 'XYZ'[axis]):
                                if info == 'string':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'XYZ'[axis], str(value),
                                                 type = 'string')
                                elif info == 'bool':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'XYZ'[axis], bool(value))
                                else:
                                    cmds.setAttr(node + '.' + attribute +
                                                 'XYZ'[axis], value)
                            elif cmds.objExists(node + '.' + attribute
                                                + 'RGB'[axis]):
                                if info == 'string':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'RGB'[axis], str(value),
                                                 type = 'string')
                                elif info == 'bool':
                                    cmds.setAttr(node + '.' + attribute +
                                                 'RGB'[axis], bool(value))
                                else:
                                    cmds.setAttr(node + '.' + attribute +
                                                 'RGB'[axis], value)
                            else:
                                check = 1
                        if check == 1:
                            if info == 'string':
                                cmds.setAttr(node + '.' + attribute, str(value),
                                             type = 'string')
                            elif info == 'bool':
                                cmds.setAttr(node + '.' + attribute, bool(value))
                            elif info == 'short':
                                cmds.setAttr(node + '.' + attribute, int(value))
                            else:
                                cmds.setAttr(node + '.' + attribute, 
                                             float(value))
            else:
                raise Exception('You have to specify a valid attribute. '
                                'Current attribute: ' + attribute)
        else:
            raise Exception('You have to specify a valid node. Current node: '
                            + node)
    #end def setAttr()

    def connectAttr(self, node = [None, None], attribute = [None, None]):
        """
        @todo: add multiNodes in node, ie. node = [[list],[list]]
        @todo: add multiAttributes in attribute, ie. attribute = [[list],[list]]
        """
        #--- check if node exist
        if node:
            #--- check if attribute exist
            if attribute:
                if isinstance(node, list):
                    #--- check len of node
                    if not isinstance(node[0], list):
                        #--- check len of attribute
                        if not isinstance(attribute[0], list):
                            if not isinstance(attribute[1], list):
                                check = 0
                                for axis in range(len('xyz')):
                                    if cmds.objExists(node[0] + '.' 
                                                      + attribute[0] + 
                                                      'xyz'[axis]):
                                        if cmds.objExists(node[1] + '.' 
                                                          + attribute[1] 
                                                          + 'xyz'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] 
                                                                 + '.' + 
                                                                 attribute[0] 
                                                                 + 'xyz'[axis], 
                                                                 node[1] + '.' 
                                                                 + attribute[1] 
                                                                 + 'xyz'[axis])
                                            except:
                                                raise Exception(node[0] + '.' 
                                                                + attribute[0] 
                                                                + 'xyz'[axis] + 
                                                                ' is already '
                                                                'connected to ' 
                                                                + node[1] + '.' 
                                                                + attribute[1] 
                                                                + 'xyz'[axis])
                                        elif cmds.objExists(node[1] + '.' 
                                                            + attribute[1] 
                                                            + 'XYZ'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' 
                                                                 + attribute[0] 
                                                                 + 'xyz'[axis], 
                                                                 node[1] + '.' 
                                                                 + attribute[1] 
                                                                 + 'XYZ'[axis])
                                            except:
                                                raise Exception(node[0] + '.' 
                                                                + attribute[0] 
                                                                + 'xyz'[axis] 
                                                                + ' is already' 
                                                                ' connected to ' 
                                                                + node[1] + '.' 
                                                                + attribute[1] 
                                                                + 'XYZ'[axis])
                                        else:
                                            try:
                                                cmds.connectAttr(node[0] + '.' 
                                                                 + attribute[0] 
                                                                 + 'xyz'[axis], 
                                                                 node[1] + '.' 
                                                                 + attribute[1])
                                            except:
                                                raise Exception(node[0] + '.' 
                                                                + attribute[0] 
                                                                + 'xyz'[axis] 
                                                                + ' is already '
                                                                'connected to ' 
                                                                + node[1] + '.' 
                                                                + attribute[1])
                                    elif cmds.objExists(node[0] + '.' 
                                                        + attribute[0] 
                                                        + 'XYZ'[axis]):
                                        if cmds.objExists(node[1] + '.' 
                                                          + attribute[1] 
                                                          + 'xyz'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.'
                                                                 + attribute[0] 
                                                                 + 'XYZ'[axis], 
                                                                 node[1] + '.' 
                                                                 + attribute[1] 
                                                                 + 'xyz'[axis])
                                            except:
                                                raise Exception(node[0] + '.' 
                                                                + attribute[0] 
                                                                + 'XYZ'[axis] 
                                                                + ' is already '
                                                                'connected to ' 
                                                                + node[1] + '.' 
                                                                + attribute[1] 
                                                                + 'xyz'[axis])
                                        elif cmds.objExists(node[1] + '.' 
                                                            + attribute[1] 
                                                            + 'XYZ'[axis]):
                                            try:
                                                cmds.connectAttr(node[0] + '.' 
                                                                 + attribute[0] 
                                                                 + 'XYZ'[axis], node[1] 
                                                                 + '.' + attribute[1] 
                                                                 + 'XYZ'[axis])
                                            except:
                                                raise Exception(node[0] + '.' 
                                                                + attribute[0]
                                                                + 'XYZ'[axis] 
                                                                + ' is already '
                                                                'connected to ' 
                                                                + node[1] + '.' 
                                                                + attribute[1] 
                                                                + 'XYZ'[axis])
                                        else:
                                            try:
                                                cmds.connectAttr(node[0] + '.' 
                                                                 + attribute[0] 
                                                                 + 'XYZ'[axis], 
                                                                 node[1] + '.' 
                                                                 + attribute[1])
                                            except:
                                                check = 1
                                    else:
                                        check = 1
                                if check == 1:
                                    try:
                                        cmds.connectAttr(node[0] + '.' + 
                                                         attribute[0], 
                                                         node[1] + '.' + 
                                                         attribute[1])
                                    except:
                                        raise Exception(node[0] + '.' + 
                                                        attribute[0] + 
                                                        ' is already '
                                                        'connected to ' 
                                                        + node[1] + '.' 
                                                        + attribute[1])
                        else:
                            print '@todo: multiAttributes'
                    else:
                        print '@todo: multiNodes'
            else:
                raise Exception('Specified attributes: ' + 
                                attribute + ' are not valid!')
        else:
            raise Exception('Specified nodes: ' + node + ' are not valid!')
    #end def connectAttr()

    def addAttr(self, node = None, attrName = None, attrType = 'float', 
                 min = 0, max = 1, default = 1, enum = [None, None], 
                 keyable = True, channelBox = False):
        ########################################################################
        #--- check if node exists
        if node:
            #--- check if node is list
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
                                cmds.addAttr(i, longName = attrName, 
                                             shortName = attrName, 
                                             attributeType = 'enum', 
                                             enumerator = enumList, 
                                             min = min, max = max, 
                                             defaultValue = default, 
                                             keyable = keyable)
                            elif attrType == 'vector':
                                cmds.addAttr(i, longName = attrName, 
                                             shortName = attrName, 
                                             attributeType = 'double3',
                                             min = min, max = max, 
                                             defaultValue = default, 
                                             keyable = keyable)
                                for axis in 'XYZ':
                                    cmds.addAttr(i, longName = attrName + axis, 
                                                 shortName = attrName + axis, 
                                                 attributeType = 'double', 
                                                 parent = attrName, 
                                                 keyable = keyable)
                            else:
                                cmds.addAttr(i, longName = attrName, 
                                             shortName = attrName, 
                                             attributeType = attrType, 
                                             min = min, max = max, 
                                             defaultValue = default, 
                                             keyable = keyable)
                        else:
                            cmds.addAttr(i, longName = attrName, 
                                         shortName = attrName, 
                                         attributeType = attrType, 
                                         min = min, max = max, 
                                         defaultValue = default, 
                                         keyable = keyable)
                            cmds.addAttr(i, edit = True, channelBox = True)
                    else:
                        if not channelBox:
                            cmds.addAttr(i, longName = attrName, 
                                         shortName = attrName, 
                                         dataType = attrType, 
                                         keyable = keyable)
                        else:
                            cmds.addAttr(i, longName = attrName, 
                                         shortName = attrName, 
                                         dataType = attrType, 
                                         keyable = keyable)
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
                            cmds.addAttr(node, longName = attrName, 
                                         shortName = attrName, 
                                         attributeType = 'enum', 
                                         enumerator = enumList, 
                                         min = min, max = max, 
                                         defaultValue = default, 
                                         keyable = keyable)
                        elif attrType == 'vector':
                            cmds.addAttr(node, longName = attrName, 
                                         shortName = attrName, 
                                         attributeType = 'double3', 
                                         min = min, max = max, 
                                         defaultValue = default, 
                                         keyable = keyable)
                            for axis in 'XYZ':
                                cmds.addAttr(node, longName = attrName + axis, 
                                             shortName = attrName + axis, 
                                             attributeType = 'double', 
                                             parent = attrName, 
                                             keyable = keyable)
                        else:
                            cmds.addAttr(node, longName = attrName, 
                                         shortName = attrName, 
                                         attributeType = attrType, 
                                         min = min, max = max, 
                                         defaultValue = default, 
                                         keyable = keyable)
                    else:
                        cmds.addAttr(node, longName = attrName, 
                                     shortName = attrName, 
                                     attributeType = attrType, 
                                     min = min, max = max, 
                                     defaultValue = default, 
                                     keyable = keyable)
                        cmds.addAttr(node, edit = True, channelBox = True)
                else:
                    if not channelBox:
                        cmds.addAttr(node, longName = attrName, 
                                     shortName = attrName, 
                                     dataType = attrType, 
                                     keyable = keyable)
                    else:
                        cmds.addAttr(node, longName = attrName, 
                                     shortName = attrName, 
                                     dataType = attrType, 
                                     keyable = keyable)
                        cmds.addAttr(node, edit = True, channelBox = True)
        else:
            raise Exception('Specified node: ' + 'node' + ' is not valid!') 
    #end def addAttr()

    def setDefault(self, node = None):
        ########################################################################
        #--- check if node exists
        if node:
            #--- check if node is a list
            if isinstance(node, list):
                for i in node:
                    #--- list attributes, get their default values and set them
                    list_attrs = cmds.listAttr(i, keyable = True)
                    for attr in list_attrs:
                        attr_query = cmds.attributeQuery(attr, node = i,
                                                        listDefault = True)[0]
                        cmds.setAttr(i + '.' + attr, attr_query)
            else:
                #--- list attributes, get their default values and set them
                list_attrs = cmds.listAttr(node, keyable = True)
                for attr in list_attrs:
                    attr_query = cmds.attributeQuery(attr, node = node,
                                                    listDefault = True)[0]
                    cmds.setAttr(node + '.' + attr, attr_query)
        else:
            raise Exception('Specified node: ' + node + ' is not valid!')
    #end def setDefault()

