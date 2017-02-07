# node.py
# defines the node classes of the elmore model


class ElmoreNode:
	"""
		Base class for all RC nodes

	"""
	def __init__(self, capacitance, resistance, parent, children):
		"""
		Creates and instance of an ''ElmoreNode''

		Args:
			capacitance (float, double): node capacitance in fF
			resistance (float, double): node resistance in Ohms
			parent (ElmoreNode, TransitorNode): the parent of the node
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
		self.ptau = resistance*self.cumCap

class TransitorNode:
	"""
		Base class for all transistor nodes

	"""
	def __init__(self, inputCapacitance, outputCapacitance, outputResistance, parents, children):
		"""
		Creates and instance of an ''TransitorNode''

		Args:
			inputCapacitance (float, double): input capacitance in fF
			outputCapacitance (float, double): output capacitance in fF
			outputResistance (float, double): output resistance in Ohms (not sure if this is right yet)
			parent (elmorenode, gatenode): the parent of the node
			children (list): the children of the node
		"""
		self.capacitance = outputCapacitance
		self.resistance = resistance
		self.parent = parent
		self.children = children
		self.ptau = None
		self.cumCap = inputCapacitance
			
	def calcptau(self):
		cumCap = capacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcptau()
			cumCap += child.cumCap
		self.ptau = resistance*cumCap

	
	
