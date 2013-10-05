"""
Created on 21.09.2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: Reads data from xml files and provides them as a RigData object.
"""
import os
import sys
import xml.etree.ElementTree as et
sys.path.append('//Rocky/CINE/User/schweipa/scripts/AutoRigger')
from utility import path
reload(path)


class DataReader():
    """Reads data from xml files and returns the information as RigData class
    objects.
    @todo: support json
    @todo: read attributes from xml tags (elem.keys())

    """
    def __init__(self):
        pass
    # end def __init__

    def parse_xml_etree(self, datatype, module):
        """Parses an autorigger xml document. and returns a list of data
        objects with all the information in the xml document.

        """
        xml_path = os.path.join(path.Path().get_root_path(), 'data', datatype,
                                 ('%s.xml' % module))
        tree = et.parse(xml_path)
        modules = tree.getroot()
        module_data = list()
        for module in modules:
            module_data.append(self.build_data_object(module))
        # end for module in modules
        return module_data
    # end def parse_xml_etree

    def build_data_object(self, xml_tree):
        """Builds the RigData object from the xml file.
        @param xml_tree: A xml tree
        @type xml_tree: xml

        """
        data = RigData()
        for elem in xml_tree:
            attr = elem.tag
            if len(elem) > 0:
                value = list()
                for subelem in elem:
                    value.append(self.build_data_object(subelem))
            else:
                value = self.convert_value(elem.text)
            setattr(data, attr, value)
        # end for elem in xml_tree
        return data
    # end def build_data_object

    def convert_value(self, value):
        """Converts the value from String into the correct data format.
        @param value: The value to check for the data type and change it
                      accordingly
        @type value: String

        """
        # Boolean
        if value == 'True':
             return True
        elif value == 'False':
            return False
        # Integer
        elif value.isdigit():
            return int(value)
        # Float
        elif value.replace('.','',1).isdigit():
            return float(value)
        else:
            return value
    # end def convert_value
# end class DataReader


class RigData():
    """This class represents a default class, that gets filled with attributes
    by the DataReader.

    """
    def __init__(self):
        pass
    # end def __init__
# end class RigData


dr = DataReader()
data_classes = dr.parse_xml_etree('modules', 'arm')
for d in data_classes:
    print dir(d)
    if d.ik == True:
        print d.ik
    #for j in d.joints:
        #print dir(j)

