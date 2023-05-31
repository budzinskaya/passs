from Player_class import Player 

class Wizard(Player):
	def __init__(self, name):
		super().__init__(name)
		self.__player_class = "Wizard"