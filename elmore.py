# node.py
# defines the node classes of the elmore model

class PiNode:
	def __init__(self, capacitance, resistance, parent, children):
		"""
		Creates and instance of a PiNode, making a good approximation for a wire with the given capacitance and resistance values

		Args:
			capacitance (float, double): node capacitance in fF
			resistance (float, double): node resistance in Ohms
			parent (RCNode, TransitorNode): the parent of the node
			children (list): the children of the node
		"""
		self.parent = parent
		self.children = children
		self.cumCap = None
		self.n1 = RCNode(capacitance/2, resistance/3, self.parent, [])
		self.n2 = RCNode(capacitance/2, resistance/3, self.n1, [])
		self.n3 = RCNode(0, resistance/3, self.n2, self.children)
		self.n1.addChild(self.n2)
		self.n2.addChild(self.n3)
		
		

	def addChild(self, child):
		self.n3.addChild(child)

	def calcpTau(self):
		self.n1.calcpTau()
		self.cumCap = self.n1.cumCap

	def calcTau(self):
		return self.n3.calcTau()
		

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
		if (self.children == None):
			self.cumCap = capacitance	
		else:
			self.cumCap = None


			
	def addChild(self, child):
		self.children.append(child)

	def calcpTau(self):
		self.cumCap = self.capacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcpTau()
			self.cumCap += child.cumCap
		self.ptau = self.resistance*self.cumCap

	def calcTau(self):
		if (self.ptau == None):
			self.calcpTau()
		cumTau = self.ptau
		if (self.parent != None):
			cumTau += self.parent.calcTau()
		return cumTau

	def dity(self):
		self.cumTau = None
		for child in self.children:
			child.cumTau = None
			child.dity()

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

	def addChild(self, child):
		self.children.append(child)
			
	def calcpTau(self):
		cumCap = self.outputCapacitance
		for child in self.children:
			if (child.cumCap == None):
				child.calcpYau()
			cumCap += child.cumCap
		self.ptau = self.outputResistance*cumCap

	def calcTau(self):
		if (self.ptau == None):
			self.calcpTau()
		cumTau = self.ptau
		if (self.parent != None):
			cumTau += parent.calcTau()
		return cumTau

	

class Wire(PiNode):
	def __init__(self, fcapacitance, acapacitance, sheetresistance, length, width, parent, children):
		"""
		Creates and instance of a pinode, but takes physical dimensions instead of the electrical.

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
