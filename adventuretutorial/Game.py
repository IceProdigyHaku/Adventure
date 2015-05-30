#Game.py
import World
from Player import player

def play():
	World.load_tiles()
	Player = player()
	#These lines load the starting room and display the text
	while Player.is_alive() and not Player.victory:
		room = World.tile_exists(player.location_x, player.location_y)
		room.modify_player(Player)
		#check again since the room could have changed the player's state
		print("choose an action:\n")
		available_actions = room.available_actions()
		for action in available_actions:
			print(action)
		Action_input = input('Action: ')
		for action in available_actions:
			if Action_input == action.hotkey:
				player.do_action(Action, **action.kwargs)
				break
					
if __name__ == "__main__":
	play()
	
