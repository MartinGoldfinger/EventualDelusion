"""
Character creation class

"""

import random
import tkinter

class Character:
	"""
	Functions:
		__init__ : initalize all the character variables
		attack_phase : character is on defense character class
			 that is called as an arguement is the attacker,
			 Character1.take_damage(Character2)
		heal_self : allows character to regenerate HP
		__str__ : default string when using:
			 print(character)

	"""
	def __init__(self, name="Character", hit_points=0, lives=1, power=1, defense=1):
		"""
		Attributes:
			_name (str): name of character
			_max_hp (int): character maximium hit points
			_current_hp (int): character current hit points
			_lives (int): number of times character can resurrect
			_alive (bool): True means character is alive,
				False means character is dead with no more lives
			_attack_power (int): Character offensive strength
			_defense (int): Character defensive strength
			_evade (int): Character ability to dodge,
				the lower the better, 1 is dodging like Neo in The Matrix
			_dexterity (int): number of times a character will hit opponent
			_healing (int): How many times a character can heal themselves,
				limited to player characters at this point
			_taunt (str): Character taunt
			battle_text (str): Updates on battle progress,
				example - "Player took X damage!"

		"""
		self._name = name
		self._max_hp = hit_points
		self._current_hp = hit_points
		self._lives = lives
		self._alive = True
		self._attack_power = power
		self._defense = defense
		self._evade = 20
		self._dexterity = 1
		self._healing = 5
		self._taunt = "..."
		self.battle_text = ""


	def attack_phase(self, opponent):
		"""Intakes attack power, creates a random number off that and subtracts it
		from remaining HP and display remaining or kills the Enemy"""

		#D&D style dice roll
		damage = 0
		hit_count = 0
		dodge_count = 0
		for dice in range(1, opponent._dexterity):
			#Checks evade and allows to dodge.
			if random.randint(1, self._evade) == self._evade:
				dodge_count += 1
			else:
				damage += random.randint(1, opponent._attack_power)
				hit_count += 1
		total_count = hit_count + dodge_count

		remaining_hp = self._current_hp - damage

		if remaining_hp > 0:
			self._current_hp = remaining_hp
			self.battle_text = "Hit {0} out of {1} times!\n{2._name} took {3} damage!".format(hit_count, total_count, self, damage)
		else:
			self._lives -= 1
			self.battle_text = "{0._name} took {1} damage\nand has been slain.".format(self, damage)
			if self._lives >= 0:
				self.battle_text = "{0._name} lives on.\n{0._lives} remaining.".format(self)
				#reset HP to inital value
				self._current_hp = self._max_hp
			else:
				self._alive = False


	def heal_self(self):
		"""checks if character can heal and then does so."""
		if self._healing > 0:
			#heals half of max hp
			healing_value = self._max_hp // 2

			#If healing value will take current HP beyond the max HP
			if (healing_value + self._current_hp) >= self._max_hp:
				self._current_hp = self._max_hp
				self.battle_text = "{0._name} heals to max! {0._current_hp}HP".format(self)
			else:
				self._current_hp += healing_value
				self.battle_text = "{0._name} heals for {1}. ".format(self, healing_value)

		else:
			self.battle_text = "Out of potions."


	def __str__(self):
		"""When a string value is needed to display the class"""
		return "Name: {0._name}\n{0._current_hp}/{0._max_hp} HP\nLives: {0._lives}\n".format(self)



class Golbez(Character):
	"""The Dark Knight and main enemy"""

	def __init__(self):
		super().__init__(name="Golbez")
		"""defining variables here due looks over inhertance"""
		self._max_hp = 200
		self._current_hp = 200
		self._attack_power = 10
		self._defense = 4
		self._evade = 5
		self._dexterity = 3
		self._lives = 1

		"""loading images, I KNOW I should go more dynamic but here we are.
		String values pointing to the path of each image file"""

		self._image_attack = "images\\Golbez\\g_attack.png"
		self._image_heal = "images\\Golbez\\g_heal.png"
		self._image_hit = "images\\Golbez\\g_hit.png"
		self._image_ko = "images\\Golbez\\g_ko.png"
		self._image_ready = "images\\Golbez\\g_ready.png"
		self._image_stand = "images\\Golbez\\g_stand.png"
		self._image_victory = "images\\Golbez\\g_victory.png"



class Paladin(Character):
	"""Paladin class"""
	def __init__(self, name):
		"""Paladin has higher health and attack, unable to dodge, has heal spell"""
		super().__init__(name=name)
		self._max_hp = 200
		self._current_hp = 200
		self._attack_power = 10
		self._defense = 4
		self._evade = 5
		self._dexterity = 3
		self._lives = 1

		self._taunt = "I will destroy you!"

		"""loading images, I KNOW I should go more dynamic but here we are.
		String values pointing to the path of each image file """

		self._image_attack = "images\\Paladin\\p_attack.png"
		self._image_heal = "images\\Paladin\\p_heal.png"
		self._image_hit = "images\\Paladin\\p_hit.png"
		self._image_ko = "images\\Paladin\\p_ko.png"
		self._image_ready = "images\\Paladin\\p_ready.png"
		self._image_stand = "images\\Paladin\\p_stand.png"
		self._image_victory = "images\\Paladin\\p_victory.png"

