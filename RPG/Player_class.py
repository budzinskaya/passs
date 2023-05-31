import random

class Player:

	def __init__(self, name):
		self.__name = name
		self.__health = 100
		self.__experience = 0

	def take_weapon(self, weapon):
		self.__weapon = weapon

	def attack(self):
		a = random.randint(1,9)
		b = random.randint(1,9)
		print(str(a) + ' * ' +  str(b) + ' =')
		while True:
			try:	
				answer = int(input())
				break
			except:
				print('please write only in digits')
		if answer == a * b:
			damage = self.__weapon.damage()
			print('You hit the monster with your ' + self.__weapon.get_name() + ' dealing ' + str(damage) + ' points of damage')
		else:
			damage = 0
			print('You missed')
		return damage

	def set_health(self, new_health):
		self.__health = new_health

	def get_health(self):
		return self.__health

	def set_experience(self, new_experience):
		self.__experience += new_experience

	def get_experience(self):
		return self.__experience

	def get_name(self):
		return self.__name
