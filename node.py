# node.py
# defines the node classes of the elmore model

class PiNode:
	def __init__(self, capacitance, resistance, parent, children):
		"""
		Creates and instance of a ''PiNode''

		Args:
			capacitance (float, double): node capacitance in fF
			resistance (float, double): node resistance in Ohms
			parent (RCNode, TransitorNode): the parent of the node
			children (list): the children of the node
		"""
		self.parent = parent
		self.children = children
		self.n3 = RCNode(0, resistance/3, n2, self.children)
		self.n2 = RCNode(capacitance/2, resistance/3, n1, n3)
		self.n1 = RCNode(capacitance/2, resistance/3, self.parent, n1)

	def calcpTau(self):
		self.n1.calcptau()
		self.cumCap = self.n1.cumCap

	def calcTau(self):
		return n3.calcTau()
		

class RCNode:
	"""
		Base class for all RC nodes

	"""
	def __init__(self, capacitance, resistance, parent, children):
		"""
		Creates and instance of an ''RCNode''

		Args:
			capacitance (float, double): node capacitance in fF
			resistance (float, double): node resistance in Ohms
			parent (RCNode, TransitorNode): the parent of the node
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
			
	def calcpTau(self):
		self.cumCap = capacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcptau()
			self.cumCap += child.cumCap
		self.ptau = resistance*self.cumCap

	def calcTau(self):
		if (self.ptau == None):
			self.calcpTau()
		cumTau = self.ptau
		cumTau += parent.calcTau()
		return cumTau

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
			parent (RCNode, gatenode): the parent of the node
			children (list): the children of the node
		"""
		self.outputCapacitance = outputCapacitance
		self.outputResistance = outputResistance
		self.parent = parent
		self.children = children
		self.ptau = None
		self.cumCap = inputCapacitance
			
	def calcpTau(self):
		cumCap = self.outputCapacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcptau()
			cumCap += child.cumCap
		self.ptau = outputResistance*cumCap

	def calcTau(self):
		if (self.ptau == None):
			self.calcpTau()
		cumTau = self.ptau
		cumTau += parent.calcTau()
		return cumTau

	
	
