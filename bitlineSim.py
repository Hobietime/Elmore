#bitlinesim.py
#simulates a biline of a register file
import inspect
import elmore


class BitlineWrite:
	def __init__(self, numBits, driveCap, driveRes, wirePitch, memCap,\
	wireThicc, fCap, aCap, sheetRes):

		self.bitline = []
		self.bitline.append(elmore.RCNode(driveCap, driveRes, None, []))
		
		for i in range(numBits*2):
			if (i%2 == 0):
				self.bitline.append(elmore.Wire(fCap, aCap, sheetRes, wirePitch, wireThicc, self.bitline[-1], []))
				self.bitline[-2].addChild(self.bitline[-1])
			if (i%2 == 1):
				self.bitline.append(elmore.RCNode(memCap, 0, self.bitline[-1], []))
				self.bitline[-2].addChild(self.bitline[-1])

	def worstCase(self):
		return self.bitline[-1].calcTau()

	def bestCase(self):
		return self.bitline[1].calcTau()




bitline = BitlineWrite(20, 1, 1, 1, 1, 1, 1, 1, 1)


print(bitline.worstCase())

print(bitline.bestCase())




