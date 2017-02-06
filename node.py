# node.py
# defines the node classes of the elmore model


class elmorenode:
	"""
		Base class for all RC nodes

	"""
	def __init__(self, capacitance, resistance, parent, children):
		"""
		Creates and instance of an ''elmorenode''

		Args:
			capacitance (float, double): node capacitance in fF
			resistance (float, double): node resistance in Ohms
			parent (elmorenode, gatenode): the parent of the node
			children (list): the children of the node
		"""
		self.capacitance = capacitance
		self.resistance = resistance
		self.parent = parent
		self.children = children
		self.ptau = None
		elif (self.children == None):
			self.cumCap = capacitance	
		else:
			self.cumCap = None
			

	def calcptau(self):
		self.cumCap = capacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcptau()
			self.cumCap += child.cumCap
		self.ptau = resistance*cumCap

	
	

