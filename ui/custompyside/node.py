"""
Created on 20.09.2013
@author: Paul
"""
from PySide import QtGui, QtCore
import nodebackdrop


class Node(QtGui.QWidget):
    """Provides a node for the node backdrop.
    @todo: continuously redrawing
    @todo: provide different styles

    """
    def __init__(self, shape='circle'):
        super(Node, self).__init__()
        #self.setStyleSheet('QWidget{background-color:transparent;}')
        self.setLayout(QtGui.QGridLayout())
        self.resize(30, 30)
        self.input = list()
        self.output = list()
        self.painter = QtGui.QPainter()
        self.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
    # end def __init__

    def add_input(self, widget):
        """Adds an input node widget."""
        self.input.append(widget)
    # end def set_input

    def get_input(self):
        """Returns all input node widgets."""
        return self.input
    # end def get_input

    def add_output(self, widget):
        """Adds an ouptut node widget."""
        self.output.append(widget)
    # end def set_output

    def get_output(self):
        """Returns """
        return self.output
    # end def get_output

    def get_lines(self):
        lines = list()
        start_x = self.geometry().x() + (self.geometry().width() / 2)
        start_y = self.geometry().y() + (self.geometry().height() / 2)
        start = QtCore.QPoint(start_x, start_y)
        for node in self.get_input() + self.get_output():
            end_x = node.geometry().x() + (node.geometry().width() / 2)
            end_y = node.geometry().y() + (node.geometry().height() / 2)
            end = QtCore.QPoint(end_x, end_y)
            ln = QtCore.QLine(start, end)
            lines.append(ln)
        return lines
    # end def get_lines

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

    def paintEvent(self, event):
        size = self.size()
        self.resize(0, 0)
        self.painter.begin(self)
        path = QtGui.QPainterPath()
        path.addEllipse(0, 0, 28, 28)
        self.painter.drawPath(path)
        self.painter.end()
        self.resize(size)



        """
        myGradient = QLinearGradient()
        myPen = QPen()
        boundingRectangle = QRectF()

        myPath = QPainterPath()
        myPath.addEllipse(boundingRectangle)

        QPainter painter(self)
        painter.setBrush(myGradient)
        painter.setPen(myPen)
        painter.drawPath(myPath)
        """




    # end paintEvent

    def draw_background(self):
        # Loop through all nodes and draw the respective lines
        color = QtGui.QColor(120, 180, 0)
        self.painter.setBrush(QtGui.QColor(200, 0, 0))
        self.painter.drawRect(0, 0, 90, 60)
    # end def draw_lines

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
