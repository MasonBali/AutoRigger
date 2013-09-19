'''
Created on 16.09.2013

@author: Isaac Clark
'''

import os, json
from maya import cmds
from fundamentals import attribute


class Data(object):
    """
    This class handles all the data which will be created to use the auto rigger.
    It contains saving and loading data. You can also choose between json and
    xml files.
    """

    def __init__(self):
        ########################################################################
        #vars

        #methods
        self._reload_modules()
    #end def __init__()

    def _reload_modules(self):
        reload(attribute)
    #end def _reload_modules()

    def _new_data_folder(self, dirName = None):
        ########################################################################
        if not os.path.isdir('C:/Users/Isaac Clark/Documents/GitHub/AutoRigger'
                             '/data/' + str(dirName)):
           os.mkdir('C:/Users/Isaac Clark/Documents/GitHub/AutoRigger/data/' 
                    + str(dirName))
    #end def new_data_folder()

    def _write_data(self, obj = None, dirName = None, fileName = None):
        ########################################################################
        self._new_data_folder(dirName = dirName)
        path = os.path.abspath('C:/Users/Isaac Clark/Documents/GitHub/'
                               'AutoRigger/data/' + dirName)

        output = open(path + '/' + fileName + '.json', 'w')
        json.dump(obj, output)
    #end def write_data()

    def _read_data(self, dirName = None, fileName = None):
        ########################################################################
        path = os.path.abspath('C:/Users/Isaac Clark/Documents/GitHub/'
                               'AutoRigger/data/' + dirName)
        data = open(path + '/' + fileName + '.json', 'r')
        output = json.load(data)
        return output
    #end def read_data()

    def save(self, dirName = None, assetName = None, dataType = None):        
        ########################################################################
        attr = attribute.Attribute()
        sel = cmds.ls(selection = True)
        data = []
        if dataType == 'attribute':
            for i in sel:
                list_attr = cmds.listAttr(i, keyable = True, visible = True)
                for attrs in list_attr:
                    value = attr.getAttr(node = i, attribute = attrs)
                    result = (str(i) + '.' + str(attrs) + ', ' + str(value))
                    data.append(result)
        elif dataType == 'shape':
            for i in sel:
                shape_type = cmds.listRelatives(i, allDescendents = 1, shapes = 1)
                obj_type = cmds.objectType(shapeType)
                if obj_type == 'nurbsCurve' or obj_type == 'nurbsSurface':
                    curve = cmds.ls(i + '.cv[*]', flatten = 1)
                    for cv in curve:
                        pos = cmds.xform(cv, query = True, translation = True, 
                                         worldSpace = True)
                        data.append(pos)
                elif obj_type == 'mesh':
                    vertices = cmds.ls(i + '.vtx[*]', flatten = 1)
                    for vtx in vertices:
                        pos = cmds.xform(vtx, query = True, translation = True, 
                                         worldSpace = True)
                        data.append(pos)
                else:
                    raise Exception('There is not component mode of this node!')
        self._write_data(obj = data, dirName = dirName, fileName = assetName)
    #end def save()

    def load(self, dirName = None, assetName = None, dataType = 'attribute'):        
        ########################################################################
        attr = attribute.Attribute()
        result = self._read_data(dirName = dirName, fileName = assetName)
        if dataType == 'attribute':
            for i in result:
                if cmds.objExists(i.split(',')[0]):
                   attr.setAttr(node = i.split(',')[0].split('.')[0], 
                                attribute = i.split(',')[0].split('.')[1], 
                                value = i.split(', ')[1])
        elif dataType == 'shape':
            return result
    #end def load()
#end class Data()

#Data().save(dirName = 'guideData', assetName = 'test', dataType = 'attribute')
Data().load(dirName = 'guideData', assetName = 'test', dataType = 'attribute')