import random

class Magic_staff():

	def __init__(self):
		self.__name = "magic staff"

	def damage(self):
		return random.randint(6,14)

	def get_name(self):
		return self.__name