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
        self.painter.setClipping(True)
        self.painter.setClipRect(0, 0, 1000, 1000)
        self.painter.begin(self)
        self.painter.setBrush(QtGui.QBrush(QtCore.Qt.SolidPattern))
        self.draw_lines()
        self.painter.end()
    # end paintEvent
        
    def draw_lines(self):
        # Loop through all nodes and draw the respective lines
        children = self.children()
        lines = list()
        for c in children:
            if type(c) is not node.Node:
                continue
            inp = c.get_input()
            outp = c.get_output()
            start_x = c.geometry().x()+30
            start_y = c.geometry().y()+30
            start = QtCore.QPoint(start_x, start_y)
            c.children()[1].setText('%s %s' % (start_x, start_y))
            if inp is not None:
                end_x = inp.geometry().x()+30
                end_y = inp.geometry().y()+30
                end = QtCore.QPoint(end_x, end_y)
                ln = QtCore.QLine(start, end)
                lines.append(ln)
            if outp is not None:
                end_x = outp.geometry().x()+30
                end_y = outp.geometry().y()+30
                end = QtCore.QPoint(end_x, end_y)
                ln = QtCore.QLine(start, end)
                lines.append(ln)
        self.painter.drawLines(lines)       
    # end def draw_lines
# end class NodeBackDrop
