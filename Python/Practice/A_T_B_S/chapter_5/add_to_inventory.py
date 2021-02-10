from collections import Counter
from inventory import display_inventory

def add_to_inventory(inventory, add_items):
	item_quantities = Counter(add_items)

	for k in item_quantities.keys():
		inventory.setdefault(k, 0)
		inventory[k] += item_quantities[k]
	return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)