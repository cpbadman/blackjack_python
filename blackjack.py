#blackjack
from random import shuffle, randint
ValMap = {
	1: 'Ace',
	11: 'Jack',
	12: 'Queen',
	13: 'King'
}

NameMap = {
	0: 'DEALER',
	1: 'CIARAN',
	2: 'ADRIAN',
	3: 'ZHANET',
	4: 'OLLIE',
	5: 'ALISON',
	6: 'DOG',
	7: 'NANCY',
	8: 'OLIVIA',
}

NDecks = 3
NPlayers = 1

print("***Welcome to Blackjack***\n\n")

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


class Deck:
	def __init__(self):
		self.cards = []

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return str(len(self.cards)) + " cards:\n" + str(self.cards)

	def populate(self):
		for num in range(NDecks):
			for suit in ['Spades','Hearts','Clubs','Diamonds']: #emoji?
				for i in range (13):
			
					#append to cards
					self.cards.append(Card(suit,i+1))

	def shuffle(self):
		#fisher yates
		shuffle(self.cards)

	def get_top_card(self):
		return self.cards.pop()

	def cut(self):
		pos = randint(1,len(self.cards))

		self.cards = self.cards[pos:] + self.cards[:pos]

	def append(self,card):
		self.cards.append(card)

class Player:
	def __init__(self): #(self,index)

		self.cards = []
		self.dealer = False
		self.playername = ""
		self.balance = 100 #do this via dictionary maybe?
		self.term = False
		self.bust = False
		self.fold = False
		self.stick = False

		self.value = 0
		self.id = 0



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


class Game:

	def __init__(self,myDeck,disDeck):


		self.playerhands = [Player() for _ in range(NPlayers + 1)]
		self.cardsontable = []

		index = 0
		for hands in self.playerhands:
			hands.id = index
			if index == 0:
				hands.dealer = True
			index = index + 1
		
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
		input("Game over")
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

class Match:
	
	def __init__(self):
		self.myDeck = Deck()
		self.disDeck = Deck()
		self.myDeck.populate()
		self.play = True
		#print(self.myDeck)
		while len(self.myDeck.cards) > 4*(NPlayers + 1) and self.play == True:
			Game(self.myDeck,self.disDeck)
			play = input("Continue? [y/n]")
			if play != "y":
				self.play = False


Match()