import random

class Skeleton():

	def __init__(self):
		self.__name = "skeleton" 
		self.__health = 50		
		self.__experience = 10

	def attack(self):
		damage = random.randint(5, 10)
		print('The skeleton pierced you with its spear dealing ' + str(damage) + ' points of damage')
		return damage

	def set_health(self, new_health):
		self.__health = new_health

	def get_health(self):
		return self.__health

	def get_name(self):
		return self.__name

	def get_experience(self):
		return self.__experience