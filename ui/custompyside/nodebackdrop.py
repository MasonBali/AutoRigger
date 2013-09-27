"""
Created on 20.09.2013
@author: Paul
"""
from PySide import QtGui, QtCore
import dlayout
reload(dlayout)
import node
reload(node)


class NodeBackDrop(QtGui.QWidget):
    """##################################################################"""
    def __init__(self):
        """#################################################################"""
        super(NodeBackDrop, self).__init__()
        self.setAcceptDrops(True)
        self.setLayout(dlayout.DragSupportLayout())
        self.dragged_element = None
        self.cursor_position = None
        self.painter = QtGui.QPainter()
    # end def __init__

    def set_dragged_element(self, dragged_element):
        """Sets the currently dragged element
        @param dragged_element: the currently dragged element
        @type dragged_element: QWidget
        """
        self.dragged_element = dragged_element
    # end def set_dragged_button

    def dropEvent(self, event):
        """Handles the drop event and places the currently active element at
        the drop position.
        @param event: the drop event
        """
        self.cursor_position = event.pos()
    # end def dropEvent

    def dragEnterEvent(self, event):
        """Accepts the drag event."""
        event.accept()
    # end def dragEnterEvent
    
    def paintEvent(self, event):
        size = self.size()
        self.resize(0, 0)
        self.painter.begin(self)
        self.draw_lines()
        self.painter.end()
        self.resize(size)
    # end paintEvent
        
    def draw_lines(self):
        # Loop through all nodes and draw the respective lines
        children = self.children()
        lines = list()
        for c in children:
            if type(c) is not node.Node:
                continue 
            lines += c.get_lines()
        self.painter.drawLines(lines) 
    # end def draw_lines
# end class NodeBackDrop
