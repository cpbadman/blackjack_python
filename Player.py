from Config import NameMap

class Player:
	def __init__(self,id): #(self,index)

		self.cards = []
		self.id = id
		self.dealer = not bool(id)
		self.playername = ""
		self.balance = 1000000 if self.dealer else 100 #do this via dictionary maybe?
		self.term = False
		self.bust = False
		self.fold = False
		self.stick = False

		self.value = 0



	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		

		cardstr = str(self.playername)  #+ " " + str(self.value)

		if self.bust == True:
			cardstr += " 					BUST!"
		elif self.stick == True:
			cardstr += "					STICK!"
		elif self.fold == True:
			cardstr += "					FOLD!"

		cardstr += "\n	Balance:		£" + str(self.balance)
		
		known = True

		for card in self.cards:
			if card.visible == False:
				known = False

		if known == False:
			cardstr += "\n 	Hand Value: 		?"
		else: 
			cardstr += "\n	Hand Value:		" + str(self.value)
		

		cardstr += "\n\n"
		
		for card in self.cards:
			cardstr += "	" + str(card)

		cardstr += "\n\n"

		#cardstr += "Value: " + str(self.value) + "\nBust: " + str(self.bust) 

		return cardstr

	def get_top_card(self):
		return self.cards.pop()

	def refresh(self):
		self.term = False
		self.bust = False
		self.stick = False

	def evaluate(self):
		self.value = 0
		self.playername = NameMap[self.id] #ASK ADRIAN ABOUT THIS. I KNOW IT'S TERRIBLE

		aces = 0
		for card in self.cards:

			if card.value == 1:
				self.value = self.value + 11
				aces = aces + 1

			elif card.value >= 10:
				self.value = self.value + 10

			else: 
				self.value = self.value + card.value 

			
		while self.value > 21 and aces != 0:
			self.value = self.value - 10
			aces = aces - 1

		if self.value > 21:
			self.bust = True

		else:
			self.bust = False
				# TODO: edge case aces /no bust


	def append(self,card):
		self.cards.append(card)