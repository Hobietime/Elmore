#bitlinesim.py
#simulates a biline of a register file
import numpy as np
import matplotlib.pyplot as plt
import inspect
import elmore
import sys
sys.setrecursionlimit(1500)


class Bitline:
	def __init__(self, numWords, driveCap, driveRes, wirePitch, memCap,\
	wireThicc, fCap, aCap, sheetRes):
		"""
		Creates and chain of nodes that model a bitline

		Args:
			numWords (int): number of words (or rows) in a memory
			driveCap (float, double): node resistance in Ohms
			parent (RCNode, TransitorNode): the parent of the node
			children (list): the children of the node
		"""


		self.bitline = []
		self.driveCap = driveCap
		self.driveRes = driveRes
		self. scale = 1
		self.bitline.append(elmore.RCNode(driveCap, driveRes, None, []))
		
		for i in range(numWords*2):
			if (i%2 == 0):
				self.bitline.append(elmore.Wire(fCap, aCap, sheetRes, wirePitch, wireThicc, self.bitline[-1], []))
				self.bitline[-2].addChild(self.bitline[-1])
			if (i%2 == 1):
				self.bitline.append(elmore.RCNode(memCap, 0, self.bitline[-1], []))
				self.bitline[-2].addChild(self.bitline[-1])

	def worstCase(self): 
		"""
		returns the worst case delay of a bitline
		"""
		return self.bitline[-1].calcTau()

	def bestCase(self):
		"""
		returns the best case delay of a bitline
		"""
		return self.bitline[1].calcTau()

	def derWorstCase(self):
		"""
		returns the derivative of the worst case delay of a bitline
		"""
		self.bitline[1].calcpTau()
		return self.bitline[1].cumCap

	def newtons_method(self, targetDelay, scale):
		"""
		preforms one iteration of newtons method, adjusting the scale of the drive resistor to get closer to the target delay
		Args:
			targetDelay(float, double): ideal delay
			scale(float, double): transistor scale
		"""
		self.scale = scale
		self.bitline[0] = elmore.RCNode(self.driveCap*scale, self.driveRes*scale, None, [self.bitline[0]])
		self.bitline[0].dirty()
		derivative = self.derWorstCase()
		actual = self.worstCase() - targetDelay
		newscale = self.scale - derivative/actual
		new_zero = actual
		return 










bitlineWrite = Bitline(64, 2, .005, 1, 2, .1, .1, 0, 1)


#print(bitlineWrite.worstCase())

#print(bitlineWrite.bestCase())



bitlineRead = Bitline(255, 2, .005, 1, 2, .1, .1, 0, 1)


#print(bitlineRead.worstCase())
bitlineRead.derWorstCase()

bittest = []
scale= []
for i in range(1,200):
	bittest.append(Bitline(255, 1*(.01*i), .5/(.01*i), 10, .5, .1, .1, 0, 1))
	scale.append((.01*i))
numbers = [x.worstCase()/1000000 for x in bittest]

print(numbers)
t = np.array(numbers)

# red dashes, blue squares and green triangles
plt.plot( scale, t, 'r--')
plt.xlabel("Driver Scale")
plt.ylabel("Delay (ns)")
plt.title("Worst case delay as a funtion of driver scale")

plt.show()

bittest = []
scale= []
for i in range(1,200):
	bittest.append(Bitline(255, 1, .5, 10, .5, .16+(.01*i), .1, 0, 1))
	scale.append((.16+.01*i))
numbers = [x.worstCase()/1000000 for x in bittest]

print(numbers)
t = np.array(numbers)

# red dashes, blue squares and green triangles
plt.plot( scale, t, 'r--')
plt.xlabel("Wire thickness (um)")
plt.ylabel("Delay (ns)")
plt.title("Worst case delay as a funtion of wire thickness")

plt.show()

bittest = []
scale= []
for i in range(16,256):
	bittest.append(Bitline(i, 1, .5, 10, .5, .16, .1, 0, 1))
	scale.append((i))
numbers = [x.worstCase()/1000000 for x in bittest]

print(numbers)
t = np.array(numbers)

# red dashes, blue squares and green triangles
plt.plot( scale, t, 'r--')
plt.xlabel("Row count")
plt.ylabel("Delay (ns)")
plt.title("Worst case delay as a funtion of row size")

plt.show()



