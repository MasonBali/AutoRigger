"""
Created on 10/04/2013
@author: Paul Schweizer
@email: paulschweizer@gmx.net
@brief: The UI for the AutoRigger system.
"""


from PySide import QtGui


class NodeGraphicsScene(QtGui.QGraphicsScene):
	"""Sets up the graphics scene for the graphics view.
	@todo: set scene rect
	@todo: accept drops

	"""
	def __init__(self):
		super(NodeGraphicsScene, self).__init__()
		self.setStickyFocus(True)
	# end def __init__

	def set_scene_rect(self):
		pass

	def mousePressEvent(self, event):
		print event

	def mouseMoveEvent(self, event):
		pass

	def dragEnterEvent(self, event):
		print 'dragenter'

	def dropEvent(self, event):
		print 'dropevent'
