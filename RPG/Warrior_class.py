from Player_class import Player 

class Warrior(Player):
	def __init__(self, name):
		super().__init__(name)
		self.__player_class = "Warrior"