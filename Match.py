from Player import Player
from Deck import Deck
from Game import Game
from Config import NPlayers, NDecks

class Match:
	
	def __init__(self):
		self.players = [Player(id) for id in range(NPlayers + 1)]
		self.myDeck = Deck()
		self.disDeck = Deck()
		self.myDeck.populate()
		self.play = True
		#print(self.myDeck)
		while len(self.myDeck.cards) > 4*(NPlayers + 1) and self.play == True:
			
			Game(self.myDeck,self.disDeck,self.players)
			play = input("Continue? [y/n]")
			if play != "y":
				self.play = False