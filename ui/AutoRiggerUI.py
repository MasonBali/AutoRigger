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
from custompyside import node
reload(node)
from custompyside import nodebackdrop
reload(nodebackdrop)
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
        # 0. Add buttons for the rigging modules
        for module in self.get_rigging_modules():
            btn = dbutton.DraggableButton()
            btn.setText(module)
            self.btnlay.insertWidget(0, btn)
        # end for module in self.get_rigging_modules()

        #--- 1. A backdrop where the connections between the nodes get drawn
        self.backdrop = nodebackdrop.NodeBackDrop()
        self.backdrop.setLayout(dlayout.DragSupportLayout())
        self.draglay.addWidget(self.backdrop)
        
        #--- 2. Create some test nodes
        main_node = node.Node()
        mid_node = node.Node()
        end_node = node.Node()
        nodes = [main_node, mid_node, end_node]
        main_node.add_output(mid_node)
        main_node.add_output(end_node)
        mid_node.add_input(main_node)
        mid_node.add_output(end_node) 
        end_node.add_input(mid_node)  
        end_node.add_input(main_node)     
        for i, n in enumerate(nodes):
            self.backdrop.layout().addWidget(n)
            n.layout().addWidget(QtGui.QPushButton('%s' % i))
        # end for i, n in enumerate(nodes)

    # end def setup_widgets()

    def get_rigging_modules(self):
        """Retrieves a list of all available rigging modules."""
        modules_path = os.listdir(os.path.join(os.path.dirname("C:/Users/Isaac Clark/Documents/GitHub/AutoRigger/ui"), 'commands'))
        modules = list()
        for module in modules_path:
            if '__init__' in module or '.pyc' in module:
                continue
            modules.append(module[:-3])
        # end for module in modules_path
        return modules
    # end def get_rigging_modules
# end class AutoRiggerUI


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
