import random

class Goblin():

	def __init__(self):
		self.__name = "goblin"
		self.__health = 80
		self.__experience = 15

	def attack(self):
		damage = random.randint(9, 11)
		print('The goblin slashed you with its axe dealing ' + str(damage) + ' points of damage')
		return damage

	def set_health(self, new_health):
		self.__health = new_health

	def get_health(self):
		return self.__health

	def get_name(self):
		return self.__name

	def get_experience(self):
		return self.__experience
