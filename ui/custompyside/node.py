"""
Created on 20.09.2013
@author: Paul
"""
from PySide import QtGui, QtCore
from maya import cmds
import dwidget, nodebackdrop


class Node(QtGui.QWidget):
    def __init__(self):
        super(Node, self).__init__()
        self.setStyleSheet('QWidget{background-color:#f00;}')
        self.setLayout(QtGui.QGridLayout())
        self.resize(70, 70)
        self.input = None
        self.output = None
    # end def __init__
    
    def set_input(self, widget):
        """#################################################################"""
        self.input = widget
    # end def set_input

    def get_input(self):
        """#################################################################"""
        return self.input
    # end def get_input

    def set_output(self, widget):
        """#################################################################"""
        self.output = widget
    # end def set_output

    def get_output(self):
        """#################################################################"""
        return self.output
    # end def get_output

    def mouseMoveEvent(self, event):
        """#################################################################"""
        if event.buttons() != QtCore.Qt.MiddleButton:
            return
        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        dropAction = drag.start(QtCore.Qt.MoveAction)
        self.mouse_offset = event.pos()
        self.place_button(self)
    # end def mouseMoveEvent

    def mousePressEvent(self, event):
        """#################################################################"""
        QtGui.QWidget.mousePressEvent(self, event)
    # end def mousePressEvent
    
    def place_button(self, btn):
        """Places the given button at the current position of the cursor."""
        target_widget = self.get_widget_at_mouse()
        if type(target_widget) != nodebackdrop.NodeBackDrop:
            if type(target_widget.parent().parent()) == nodebackdrop.NodeBackDrop:
                target_widget = target_widget.parent().parent()
            else:
                return
        pos = target_widget.cursor_position
        size = self.geometry()
        btn.setGeometry(pos.x()-self.mouse_offset.x(), 
                        pos.y()-self.mouse_offset.y(), size.width(), 
                        size.height())
    # end def place_button
    
    def get_focus_widget(self):
        """Get the currently focused widget"""
        return QtGui.qApp.focusWidget()
    # end def get_focus_widget

    def get_widget_at_mouse(self):
        """Get the widget under the mouse"""
        currentPos = QtGui.QCursor().pos()
        widget = QtGui.qApp.widgetAt(currentPos)
        return widget
    # end def get_widget_at_mouse
# end class Node
