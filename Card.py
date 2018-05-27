class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		self.visible = False

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		name = self.value
		if self.value not in range(2,11):

			name = ValMap[self.value]

		if self.visible == True:

			return "[ " + str(name) + " of " + self.suit + " ]\n"

		else:

			return "[ CARD HIDDEN ]\n"

	def showcard(self):
		self.visible = True
	def hidecard(self):
		self.visible = False