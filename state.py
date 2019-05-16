from copy import deepcopy

class State:
	def __init__(self, pos, treasures):
		self.pos = deepcopy(pos)
		self.treasures = deepcopy(treasures)

		if list(pos) in treasures:
			del self.treasures[self.treasures.index(list(pos))]

	def __eq__(self, other):
		return isinstance(other, State) and self.pos == other.pos and self.treasures == other.treasures

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash((self.pos, self.treasures))

	def __str__(self):
		return str(self.pos) + ' ' + str(self.treasures)