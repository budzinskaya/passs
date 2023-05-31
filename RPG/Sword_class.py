import random

class Sword():

	def __init__(self):
		self.__name = "sword"

	def damage(self):
		return random.randint(8, 12)

	def get_name(self):
		return self.__name