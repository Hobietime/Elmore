# highlevelhelpers.py
# defines the higher level classes of the elmore model
import node.py
class Wire(node.PiNode):
	def __init__(self, fcapacitance, acapacitance, sheetresistance, length, width, parent, children):
		"""
		Creates and instance of a ''wire''

		Args:
			fcapacitance (float, double): wire capacitance in fF/um
			acapacitance (float, double): wire capacitance in fF/um^2
			sheetresistance (float, double): wire resistance in Ohms/[]
			length (float, double): wire length in um
			width (float, double): wire width in um
			parent (Wire, PiNode, RCNode, TransitorNode): the parent of the node
			children (list): the children of the node
		"""
		self.length = length
		self.width = width
		self.resistance = sheetresistance*(length/width)
		self.capacitance = (fcapacitance*length+acapacitance*(length*width))
		super().__init__(self.capacitance, self.resistance, parent, children)



