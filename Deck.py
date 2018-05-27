from random import shuffle, randint
from blackjack.Card import Card

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