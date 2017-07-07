"""
Eventual Delusion v2

Battle game modeling after Final Fantasy 1 screen

Building the GUI"""

import tkinter
import time


#character class
from character import Golbez, Paladin

def player_frame_refresh(load_image):
	"""
	Destroys and rebuilds the player frame so the image
	can refresh without	creating multiple images

	load_image (str) - path to the image to load
	"""

	global player_frame
	global set_player_image

	player_frame.destroy()
	player_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
	player_frame.grid(row=1, column=3, sticky='e', columnspan=2, rowspan=2)
	set_player_image = tkinter.PhotoImage(file=load_image)
	tkinter.Label(player_frame, image=set_player_image, borderwidth=0).pack(padx=90, pady=70)



def enemy_frame_refresh(load_image):
	"""
	Destroys and rebuilds the enemy frame so the image
	can refresh without	creating multiple images

	load_image (str) - path to the image to load
	"""

	global enemy_frame
	global set_enemy_image

	enemy_frame.destroy()
	enemy_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
	enemy_frame.grid(row=1, column=0, sticky='w', columnspan=2, rowspan=2)	
	set_enemy_image = tkinter.PhotoImage(file=load_image)
	tkinter.Label(enemy_frame, image=set_enemy_image, borderwidth=0).pack(padx=90, pady=70)



def enemy_attack():
	"""Enemy counterattack
	Show enemy taking attack stance, lag for a few seconds
	refresh the text and show enemy avatar attacking and player avatar taking damage
	then back to standoff
	"""

	enemy_frame_refresh(enemy._image_attack)
	player_frame_refresh(player._image_hit)
	player.attack_phase(enemy)
	battle_message_text.set(player.battle_text)
	player_display_text.set(player)
	main_window.update()
	time.sleep(1)
	player_frame_refresh(player._image_stand)
	enemy_frame_refresh(enemy._image_stand)
	main_window.update()
	time.sleep(2)
	battle_message_text.set("")


def button_attack():
	"""When Attack button is pressed
	lag for a few seconds to show character avatar stance change,
	refresh the battle text, show character avatar attacking and enemy avatar taking damage
	and if the enemy is still alive counterattack
	"""

	button_disable()

	#Refresh player frame and set image to ready
	player_frame_refresh(player._image_ready)
	main_window.update()
	time.sleep(1)

	#player attack, enemy getting hit
	enemy.attack_phase(player)
	player_frame_refresh(player._image_attack)
	enemy_frame_refresh(enemy._image_hit)
	battle_message_text.set(enemy.battle_text)
	enemy_display_text.set(enemy)
	main_window.update()
	time.sleep(1)

	#Resets player and enemy back to standoff and display round results
	player_frame_refresh(player._image_stand)
	enemy_frame_refresh(enemy._image_stand)
	main_window.update()
	time.sleep(1)

	#Enemy attacks if alive
	if enemy._alive:
		enemy_attack()
		button_enable()
	elif not enemy._alive:
		#enemy ko'ed, player wins
		enemy_frame_refresh(enemy._image_ko)
		player_frame_refresh(player._image_victory)
	else:
		pass

	if not player._alive:
		enemy_frame_refresh(enemy._image_victory)
		player_frame_refresh(player._image_ko)
	main_window.update()


def button_heal():
	"""When heal button is pressed"""
	button_disable()
	player.heal_self()
	player_frame_refresh(player._image_heal)
	main_window.update()
	time.sleep(1)

	player_frame_refresh(player._image_stand)
	battle_message_text.set(player.battle_text)
	player_display_text.set(player)
	main_window.update()

	if enemy._alive:
		enemy_attack()
	button_enable()


def button_disable():
	attack_button.config(state='disabled')
	heal_button.config(state='disabled')

def button_enable():
	attack_button.config(state='active')
	heal_button.config(state='active')


enemy = Golbez()
player = Paladin(name="Marty")

"""set image variables allow the frame refresh functions maintain the image variables outside
of the function
http://effbot.org/tkinterbook/photoimage.htm
"""
set_player_image = ""
set_enemy_image = ""


#building main window, and not allow to resize
main_window = tkinter.Tk()
main_window.title("Battle")
main_window.geometry("600x600")
main_window.resizable(width=False, height=False)
main_window.configure(background='black')

#setting the background
background_file = "images\\background.png"
background_image = tkinter.PhotoImage(file=background_file)
background_frame = tkinter.Frame()
background_frame.grid(row=0, column=0, sticky='nwe', columnspan=4, rowspan=3)
tkinter.Label(background_frame, image=background_image).pack()

#Enemy character viewing frame
enemy_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
enemy_frame.grid(row=1, column=0, sticky='w', columnspan=2, rowspan=2)
enemy_stand_image = tkinter.PhotoImage(file=enemy._image_stand)
tkinter.Label(enemy_frame, image=enemy_stand_image, borderwidth=0).pack(padx=90, pady=70)

#User character viewing frame
player_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
player_frame.grid(row=1, column=3, sticky='e', columnspan=2, rowspan=2)
player_stand_image = tkinter.PhotoImage(file=player._image_stand)
tkinter.Label(player_frame, image=player_stand_image, borderwidth=0).pack(padx=90, pady=70)

main_font = "Courier", 15

#Enemy name and hit point display
enemy_display_text = tkinter.StringVar()
enemy_display_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
tkinter.Label(main_window, textvariable=enemy_display_text, bg="black", fg="white", font=main_font).grid(row=3, column=0)
enemy_display_text.set(enemy)

#User name and hit point display
player_display_text = tkinter.StringVar()
player_display_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
tkinter.Label(main_window, textvariable=player_display_text, bg="black", fg="white", font=main_font).grid(row=3, column=3)
player_display_text.set(player)

#user interaction buttons
button_frame = tkinter.Frame(background="black")
button_frame.grid(row=5, column=3, columnspan=1)

#Attack button, deals damage to enemy
attack_button = tkinter.Button(button_frame, text='Attack', bg="black", fg="white", font=main_font, command=button_attack)
attack_button.grid(row=0, column=0)

#Heal button, heals player
heal_button = tkinter.Button(button_frame, text='Heal', bg="black", fg="white",font=main_font, command=button_heal)
heal_button.grid(row=1, column=0)

battle_message_text = tkinter.StringVar()
battle_message_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=10, background="black")
tkinter.Label(main_window, textvariable=battle_message_text, bg="black", fg="white", font=main_font).grid(row=5, column=0)


main_window.mainloop()
