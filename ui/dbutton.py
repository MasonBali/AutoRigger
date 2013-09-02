from PySide import QtGui, QtCore


class DraggableButton(QtGui.QToolButton):
    """Custom QToolButton that can be dragged and dropped.
    @param spawn_offspring: specifies whether the button shall be duplicated on drag.
    @type spawn_offspring: Boolean 
    """
    def __init__(self, spawn_offspring = True):
        """"""
        super(DraggableButton, self).__init__()
        self.spawn_offspring = spawn_offspring
        self.mouse_offset = None
    # end def __init__()

    def mouseMoveEvent(self, e):
        """##################################################################"""
        if e.buttons() != QtCore.Qt.MiddleButton:
            return
        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        dropAction = drag.start(QtCore.Qt.MoveAction)
        self.mouse_offset = e.pos()
        if self.spawn_offspring:
            self.duplicate_button()
        else:
            self.place_button(self)
    # end def mouseMoveEvent()

    def mousePressEvent(self, e):
        """##################################################################"""
        QtGui.QToolButton.mousePressEvent(self, e)
        parent = self.parent()
    # end def mousePressEvent()

    def duplicate_button(self):
        """Duplicates the current button and calls to place it at the current 
        cursor position.
        """
        target_widget = self.get_widget_at_mouse()
        if target_widget.metaObject().className() != 'DragSupportWidget':
            return
        dbutton = DraggableButton(spawn_offspring = False)
        self.place_button(dbutton)
        target_widget.layout().addWidget(dbutton)
    # end def mouseReleaseEvent()

    def place_button(self, dbutton):
        """Places the given button at the current position of the cursor."""
        target_widget = self.get_widget_at_mouse()
        if target_widget.metaObject().className() != 'DragSupportWidget':
            return
        pos = target_widget.cursor_position
        size = self.geometry()
        dbutton.setGeometry(pos.x()-self.mouse_offset.x(), 
                            pos.y()-self.mouse_offset.y(), size.width(), 
                            size.height())
    # end def place_button()

    def get_focus_widget(self):
        """Get the currently focused widget"""
        return QtGui.qApp.focusWidget()
    # end def get_focus_widget()

    def get_widget_at_mouse(self):
        """Get the widget under the mouse"""
        currentPos = QtGui.QCursor().pos()
        widget = QtGui.qApp.widgetAt(currentPos)
        return widget
    # end def get_widget_at_mouse()
# end class DraggableButton()  