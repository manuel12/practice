
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
	print("Inventory:")
	num_items = sum(inventory.values())

	for k, v in inventory.items():
		print(v, k)

	print("Total number of items: "+str(num_items))
