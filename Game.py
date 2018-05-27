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

	def turn(self):
		for hand in self.playerhands:

			if hand.dealer == False:

				while hand.term == False:
					move = input("Would {} like a card?".format(hand.playername))
					print(move)
					
					if move == "h":
						card = self.myDeck.get_top_card()
						card.showcard()
						hand.append(card)
						self.evaluate()
					
					elif move == "f":
						hand.fold = True
						self.evaluate()
					else:
						hand.stick = True
						self.evaluate()
					

					if hand.bust == True or hand.stick == True or hand.fold == True:
						hand.term = True

					self.status()
		
		hand = self.playerhands[0]

		while hand.term == False:

			card = hand.cards[0]
			card.showcard()
			input("Press enter for Dealer hand")
					
			if hand.value < 17:
				card = self.myDeck.get_top_card()
				card.showcard()
				hand.append(card)
				self.evaluate()
			
			else:
				hand.stick = True
				self.evaluate()
					

			if hand.bust == True or hand.stick == True:
				hand.term = True
				
			self.evaluate()
			self.status()

	def discard(self):
		for hand in self.playerhands:
			for i in range(len(hand.cards)):
				card = hand.get_top_card()
				self.disDeck.append(card)
				#print(self.disDeck)
				#hand.refresh()
				hand.refresh()
		self.evaluate()
		self.status()


