"""
Created on 21.09.2013
@author: Paul Schweizer
"""
import os
from utility import path
from xml.dom import minidom
reload(path)


class DataReader():
    """"""
    def __init__(self):
        pass
    # end def __init__

    def parse_xml(self, datatype, module):
        """"""
        rigmodule = RigModule() 
        xml_result = dict()
        xml_path = os.path.join(path.Path().get_root_path(), 'data', datatype,
                                 ('%s.xml' % module))
        xmldoc = minidom.parse(xml_path)
        root = xmldoc.firstChild
        
        # moduletype
        module = self.get_attributes(xmldoc.getElementsByTagName('rigmodule')[0], rigmodule)
        self.set_attribute(rigmodule, 'moduletype', module['moduletype'])

        #joints
        for joint in xmldoc.getElementsByTagName('joint'):
            self.set_attribute(rigmodule, 'joints', list())
        
        
        
        print dir(rigmodule)
    # end def parse_xml
    
    def get_attributes(self, node, rigmodule):
        """"""
        attributes = dict()
        if node.nodeType == 1 and node.hasAttributes():
            for key in node.attributes.keys():
                attributes[key] = node.attributes[key].value
            # end for key in node.attributes.keys()
        return attributes
    # end def get_attributes
    
    def set_attribute(self, rigmodule, attribute, value):
        """"""
        setattr(rigmodule, attribute, value)
    # end def set_attribute
# end class DataReader


class RigModule():
    def __init__(self):
        self.module = 'arm'
        self.joints = [] # list of joints





dr = DataReader()
dr.parse_xml('modules', 'arm')
