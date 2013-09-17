"""
Created on 17.09.2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: The UI for the AutoRigger system.
"""

import os
import sys
from PySide import QtGui, QtCore
from maya import cmds
#sys.path.append('C:\PROJECTS\AutoRigger\ui')
#form_class, base_class = convenience.load_ui_type('C:\PROJECTS\AutoRigger\ui\res\demo.ui')
sys.path.append(os.path.dirname(__file__))
from custompyside import *
form_class, base_class = convenience.load_ui_type(os.path.join(os.path.dirname(__file__), 'res', 'autorigger.ui'))


class AutoRiggerUI(base_class, form_class):
    """This displays the auto rigger ui."""
    def __init__(self, parent=None):
        super(AutoRiggerUI, self).__init__(parent)
        self.setupUi(self)
        self.setup_variables()
        self.setup_widgets()
    # end def __init__()

    def setup_variables(self):
        """#################################################################"""
    # end def setup_variables()

    def setup_widgets(self):
        """#################################################################"""
        self.dsw = dwidget.DragSupportWidget()
        dlay = dlayout.DragSupportLayout()
        self.dsw.setLayout(dlay)
        self.draglay.addWidget(self.dsw)
        self.d_btn = dbutton.DraggableButton()
        self.btnlay.insertWidget(0, self.d_btn)
    # end def setup_widgets()

    
    
    
    
    
    
# end class AutoRiggerUI()


def main():
    global autorigger_win
    try:
        autorigger_win.close()
    except:
        pass
    autorigger_win = AutoRiggerUI()
    autorigger_win.show()
# end def main()
