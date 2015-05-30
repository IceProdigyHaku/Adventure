#actions
from Player import player


class action():
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs
		
	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(action):
	def __init__(self):
		super().__init__(method=player.move_north, name='Move north', hotkey='n')

class MoveSouth(action):
	def __init__(self):
		super().__init__(method=player.move_south, name='Move south', hotkey='s')
		
class MoveWest(action):
	def __init__(self):
		super().__init__(method=player.move_west, name='Move west', hotkey='w')
		
class MoveEast(action):
	def __init__(self):
		super().__init__(method=player.move_east, name='Move east', hotkey='e')
		
class ViewInventory(action):
	def __init__(self):
		super().__init__(method=player.print_inventory, name='View Inventory', hotkey='i')
		
class Attack(action):
	def __init__(self, enemy):
		super().__init__(method=player.attack, name='Attack', hotkey='a', enemy=enemy)
		
class Flee(action):
	def __init__(self, tile):
		super().__init__(method=player.flee, name="Flee", hotkey='f', tile=tile)