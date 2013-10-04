"""
Created on 21.09.2013
@author: Paul Schweizer
"""
import os
import sys
import xml.etree.ElementTree as et
sys.path.append('//Rocky/CINE/User/schweipa/scripts/AutoRigger')
from utility import path
reload(path)


class DataReader():
    """"""
    def __init__(self):
        pass
    # end def __init__

    def parse_xml_etree(self, datatype, module):
        """"""
        xml_path = os.path.join(path.Path().get_root_path(), 'data', datatype,
                                 ('%s.xml' % module))
        tree = et.parse(xml_path)
        modules = tree.getroot()
        module_data = list()
        for module in modules:
            module_data.append(self.build_data_object(module))
        return module_data
    # end def parse_xml_etree

    def build_data_object(self, xml_tree):
        data = DataClass()
        for elem in xml_tree:
            attr = elem.tag
            if len(elem) > 0:
                value = list()
                for subelem in elem:
                    value.append(self.build_data_object(subelem))
            else:
                value = elem.text
            setattr(data, attr, value)
        return data
    # end def build_data_object
# end class DataReader


class DataClass():
    """"""
    def __init__(self):
        pass
    # end def __init__
# end class DataClass


dr = DataReader()
data_classes = dr.parse_xml_etree('modules', 'arm')
for d in data_classes:
    print dir(d)
    for j in d.joints:
        print dir(j)




