import random
from Warrior_class import Warrior
from Wizard_class import Wizard
from Skeleton_class import Skeleton
from Goblin_class import Goblin
from Sword_class import Sword
from Magic_staff_class import Magic_staff

class RPG_Game:

	def __init__(self):
		self.__game_over = False
		print("Welcome to the arena. Solve math problems to defeat enemies.")

	def character_creation(self):
		print("What is your name, adventurer?")
		name = input()
		print('Choose your class: print 1 to be a Warrior (more accurate), print 2 to be a Wizard (stronger, but less accurate)')
		while True:
			temp = input()
			if temp == '1':
				character = Warrior(name)
				character.take_weapon(Sword())
				return character
				break
			elif temp == '2':
				character = Wizard(name)
				character.take_weapon(Magic_staff())
				return character
				break
			else:
				print('Please print 1 to be a Warrior, print 2 to be a Wizard')

	def fight(self, attacker, defender):
		new_health = defender.get_health() - attacker.attack()
		defender.set_health(new_health)
		print(defender.get_name() + ': ' + str(defender.get_health()) + ' HP')

	def arena(self, hero):
		enemy = random.choice([Skeleton(), Goblin()])
		print('A scary ' + enemy.get_name() + ' steps into the arena')
		while True:
			self.fight(hero, enemy)
			if enemy.get_health() <= 0:
				hero.set_experience(enemy.get_experience())
				print('You killed the monster and gained ' + str(enemy.get_experience()) + ' XP')
				print('You now have ' + str(hero.get_experience()) + ' XP')
				break
			self.fight(enemy, hero)
			if hero.get_health() <= 0:
				print('Game Over')
				self.__game_over = True
				break

	def is_game_over(self):
		if self.__game_over:
			return True
		else:
			return False