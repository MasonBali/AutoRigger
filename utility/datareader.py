"""
Created on 21.09.2013
@author: Paul Schweizer
"""
import os
from utility import path
from xml.dom import minidom
reload(path)


class DataReader():
    def __init__(self):
        pass
    # end def __init__

    def parse_xml(self, datatype, module):
        xml_path = os.path.join(path.Path().get_root_path(), 'data', datatype,
                                 ('%s.xml' % module))
        xmldoc = minidom.parse(xml_path)
        root = xmldoc.firstChild
        for node in root.childNodes:
            if node.nodeType == 1 and node.hasAttributes():
                attributes = node.attributes
                for key in attributes.keys():
                    print attributes[key].value
            
            
    # end def parse_xml
# end class DataReader()

dr = DataReader()
dr.parse_xml('modules', 'arm')
