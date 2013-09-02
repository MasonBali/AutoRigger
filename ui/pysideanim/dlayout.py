from PySide import QtCore, QtGui


class DragSupportLayout(QtGui.QLayout):
    """A custom flow layout"""
    def __init__(self, parent = None, margin = 0, spacing = 0):
        super(DragSupportLayout, self).__init__(parent)
        if parent is not None:
            self.setMargin(margin)
        self.setSpacing(spacing)
        self.itemList = []
    # end def __init__()

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)
    # end def __del__()

    def addItem(self, item):
        self.itemList.append(item)
    # end def addItem()

    def count(self):
        return len(self.itemList)
    # end def count()

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]
        return None
    # end def itemAt()

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)
        return None
    # end def takeAt()

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))
    # end def expandingDirections()

    def hasHeightForWidth(self):
        return True
    # end def hasHeightForWidth()

    def heightForWidth(self, width):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height
    # end def heightForWidth()

    def setGeometry(self, rect):
        super(DragSupportLayout, self).setGeometry(rect)
        self.doLayout(rect, False)
    # end def setGeometry()

    def sizeHint(self):
        return self.minimumSize()
    # end def sizeHint()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
        # end for item in self.itemList
        return size
    # end def minimumSize()

    def doLayout(self, rect, testOnly):
        return 0
    # end def doLayout()
# end class FlowLayout()