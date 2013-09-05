import os
import sys
from PySide import QtGui, QtCore

sys.path.append('C:\PROJECTS\AutoRigger\ui')
from pysideanim import *

form_class, base_class = convenience.load_ui_type('C:\PROJECTS\AutoRigger\ui\demo.ui')

class PySideDemo(base_class, form_class):
    """This displays a pyside window inside maya. Needs a .ui file from the qt 
    designer.
    """
    def __init__(self, parent=None):
        super(PySideDemo, self).__init__(parent)
        self.setupUi(self)
        
        self.dsw = dwidget.DragSupportWidget()
        dlay = dlayout.DragSupportLayout()
        self.dsw.setLayout(dlay)
        self.draglay.addWidget(self.dsw)
        
        self.d_btn = dbutton.DraggableButton()
        self.btnlay.insertWidget(0, self.d_btn)
    # end def __init__()
# end class PySideDemo()


def main():
    global my_win
    try:
        my_win.close()
    except:
        pass
    my_win = PySideDemo()
    my_win.show()


main()