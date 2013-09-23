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
sys.path.append("C:/Users/Isaac Clark/Documents/GitHub/AutoRigger/ui/custompyside")
from custompyside import *
reload(dbutton)
form_class, base_class = convenience.load_ui_type(
                         os.path.join("C:/Users/Isaac Clark/Documents/GitHub/AutoRigger/ui", 'res',
                                      'autorigger.ui'))



class AutoRiggerUI(base_class, form_class):
    """This displays the auto rigger ui.
    @todo: format buttons
    @todo: mirroring
    @todo: background for mirroring
    """
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

        for module in self.get_rigging_modules():
            btn = dbutton.DraggableButton()
            btn.setText(module)
            self.btnlay.insertWidget(0, btn)
        # end for module in self.get_rigging_modules()

    # end def setup_widgets()

    def get_rigging_modules(self):
        """Retrieves a list of all available rigging modules."""
        modules_path = os.listdir(os.path.join(os.path.dirname("C:/Users/Isaac Clark/Documents/GitHub/AutoRigger/ui"), 'commands'))
        modules = list()
        for module in modules_path:
            if module == '__init__.py':
                continue
            modules.append(module[:-3])
        # end for module in modules_path
        return modules
    # end def get_rigging_modules()    
    
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
main()
