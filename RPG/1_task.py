import random
from RPG_game_class import RPG_Game
from Player_class import Player
from Warrior_class import Warrior
from Wizard_class import Wizard
from Skeleton_class import Skeleton
from Goblin_class import Goblin
from Sword_class import Sword
from Magic_staff_class import Magic_staff

if __name__ == "__main__":
	game = RPG_Game()
	hero = game.character_creation()
	while True:
		game.arena(hero)
		if game.is_game_over():
			break