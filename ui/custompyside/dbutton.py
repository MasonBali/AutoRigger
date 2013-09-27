"""
Created on 17.09.2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: A draggable PySide button.
"""

from PySide import QtGui, QtCore
import dwidget, nodebackdrop


class DraggableButton(QtGui.QToolButton):
    """Custom QToolButton that can be dragged and dropped.
    @param spawn_offspring: specifies whether the button shall be duplicated on drag.
    @type spawn_offspring: Boolean 
    @todo: add right click menu
    @todo: add icon
    """
    def __init__(self, spawn_offspring=True):
        super(DraggableButton, self).__init__()
        self.spawn_offspring = spawn_offspring
        self.mouse_offset = None
    # end def __init__()

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
        if self.spawn_offspring:
            self.duplicate_button()
        else:
            self.place_button(self)
    # end def mouseMoveEvent()

    def mousePressEvent(self, event):
        """#################################################################"""
        QtGui.QToolButton.mousePressEvent(self, event)
    # end def mousePressEvent()

    def duplicate_button(self):
        """Duplicates the current button and calls to place it at the current 
        cursor position.
        """
        target_widget = self.get_widget_at_mouse()
        if type(target_widget) != nodebackdrop.NodeBackDrop:
            if type(target_widget.parent()) == nodebackdrop.NodeBackDrop:
                target_widget = target_widget.parent()
            else:
                return
        btn = DraggableButton(spawn_offspring=False)
        btn.setText(self.text())
        self.place_button(btn)
        target_widget.layout().addWidget(btn)
    # end def mouseReleaseEvent()

    def place_button(self, btn):
        """Places the given button at the current position of the cursor."""
        target_widget = self.get_widget_at_mouse()
        if type(target_widget) != nodebackdrop.NodeBackDrop:
            if type(target_widget.parent()) == nodebackdrop.NodeBackDrop:
                target_widget = target_widget.parent()
            else:
                return
        pos = target_widget.cursor_position
        size = self.geometry()
        btn.setGeometry(pos.x()-self.mouse_offset.x(), 
                        pos.y()-self.mouse_offset.y(), size.width(), 
                        size.height())
    # end def place_button()

    def get_focus_widget(self):
        """Get the currently focused widget."""
        return QtGui.qApp.focusWidget()
    # end def get_focus_widget()

    def get_widget_at_mouse(self):
        """Get the widget under the mouse."""
        currentPos = QtGui.QCursor().pos()
        widget = QtGui.qApp.widgetAt(currentPos)
        return widget
    # end def get_widget_at_mouse()
# end class DraggableButton()
