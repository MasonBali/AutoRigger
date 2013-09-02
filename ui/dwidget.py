from PySide import QtGui


class DragSupportWidget(QtGui.QWidget):
    """##################################################################"""
    def __init__(self):
        """##################################################################"""
        super(DragSupportWidget, self).__init__()
        self.dragged_element = None
        self.setAcceptDrops(True)
        self.cursor_position = None
    # end def __init__()

    def set_dragged_element(self, dragged_element):
        """Sets the currently dragged element
        @param dragged_element: the currently dragged element
        @type dragged_element: QWidget
        """
        self.dragged_element = dragged_element        
    # end def set_dragged_button()

    def dropEvent(self, e):
        """Handles the drop event and places the currently active element at the 
        drop position.
        @param e: the drop event
        """
        self.cursor_position = e.pos()
    # end def dropEvent()

    def dragEnterEvent(self, e):
        """Accepts the drag event."""
        e.accept()
    # end def dragEnterEvent()
# end class DragSupportWidget()