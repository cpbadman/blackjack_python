class Game:

	def __init__(self,myDeck,disDeck,players):


		self.playerhands = players
		self.cardsontable = []

		# index = 0
		# for hands in self.playerhands:
		# 	hands.id = index
		# 	if index == 0:
		# 		hands.dealer = True
		# 	index = index + 1
		
		self.myDeck = myDeck
		self.disDeck = disDeck
		#self.tabCards = []

		#self.myDeck.populate()
		self.myDeck.shuffle()
		self.myDeck.cut()
		self.deal()
		self.evaluate()
		self.status()
		self.turn()
		input("Adrian Wins!")
		self.discard()


	def __repr__(self):
		pass
		

	def status(self):


		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print("CARDS:	")
		print("	Deck:		{}".format(len(self.myDeck.cards)))
		print("	On Table:	{}".format(len(self.cardsontable)))
		print("	Discarded:	{}".format(len(self.disDeck.cards)))
		print("\n\n")

		#print("\nDealer:")
		#print(self.dealerhand, end = "")
		#print("Value: " + str(self.dealerhand.value) + "\nBust: " + str(self.dealerhand.bust) + "\n")

		for i,hand in enumerate(self.playerhands):
			print(str(hand), end = "")
		#print("Deck: \n\n" + str(self.myDeck))

	def evaluate(self):

		#self.dealerhand.evaluate()
		cardsontable = []
		print(str(self.cardsontable))
		for hand in self.playerhands:
			hand.evaluate()
			#print(hand.cards)
			#print(self.cardsontable)
			cardsontable += hand.cards
			self.cardsontable = cardsontable

	def deal(self):
		#taking top card and giving to players (2 per player)
		for i in range (2):
			for hand in self.playerhands:
				card = self.myDeck.get_top_card()
				if hand.dealer == False or i == 1:
					card.showcard()
				hand.append(card)

			#card = self.myDeck.get_top_card()
			#if i == 1:
			#	card.showcard()
			#self.dealerhand.append(card)
