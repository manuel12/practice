table_data = [	
						['apples', 'oranges', 'cherries', 'banana'],
						['Alice', 'Bob', 'Carol', 'David'],
						['dogs', 'cats', 'moose', 'goose']]

def print_table(list_):
	col_widths = [0] * len(table_data)
	for sub_list in list_:
		longest_str = get_longest_str_in_list(sub_list)
		
	pass

def get_longest_str_in_list(items):
	lengths = [len(item) for item in items]
	longest_length = sorted(lengths, reverse=True)[0]
	longest = [item for item in items if len(item) == longest_length]
	return longest[0]
