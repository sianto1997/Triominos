import random

class Triominos():
	blocks = {}
	def __init__(self):
		self.create_blocks()
		return

	def create_blocks(self):
		iter = 0
		for iter1 in range(0,6):
			for iter2 in range(iter1,6):
				for iter3 in range(iter2,6):
					self.blocks.update({iter:{	1:iter1, 
												2:iter2,
												3:iter3,
												'used':False,
												'c12':None,
												'c13':None,
												'c23':None}})
					iter = iter + 1

	#get a block into the game (TODO: requires a randomizer)
	def get_block(self, f=[], connect=False):
		iterf = 0
		happened=False
		#TODO: doorschuiven
		while happened == False:
			for iter in range(0,56):
				if self.blocks.get(iter).get(1) == f[0] and self.blocks.get(iter).get(2) == f[1] and self.blocks.get(iter).get(3) == f[2]:
					self.blocks.get(iter).update({'used':True})
					happened = True
					a = iter

			# push a thing through, make this better
			f = [f[2],f[0],f[1]]
			iterf +=1
			if iterf == 3:
				happened = True

		if connect:
			self.connect_parent(a)

	def connect_parent(self, a):
		#TODO:create a method to obtain a block with 
		b = 55
		self.connect_block(a,b, way='c23')

	def connect_block(self, a, b, way='c12'):
		iterf = 0
		happened = False
		block = self.blocks.get(a)

		f = [block.get(1),block.get(2),block.get(3)]

		while happened == False:
			if self.blocks.get(b).get(1) == f[0] and self.blocks.get(b).get(2) == f[1] and self.blocks.get(b).get(3) == f[2]:
				self.blocks.get(iter).update({way:a})
				print self.blocks.get(iter)
				happened = True

			
			f = [f[2],f[0],f[1]]

			iterf +=1

			if iterf == 3:
				happened = True

		return


inc = Triominos()

#get block
inc.get_block([5,5,5])

inc.get_block([5,5,4],connect=True)