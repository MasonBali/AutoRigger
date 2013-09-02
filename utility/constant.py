"""
Created on 02.09.2013

@author: Paul
"""

class Constant():

    def __init__(self):
        self.define_constants()
        self.dummy_joint()

    def define_constants(self):
        self.LEFT = 'L'
        self.SEPARATOR = '_'
        self.JOINT = 'JNT'

    def dummy_joint(self):
        joint = '%s%sarm%s%s'%(self.LEFT, self.SEPARATOR, self.SEPARATOR, self.JOINT)
        print joint

Constant()