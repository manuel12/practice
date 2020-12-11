'''
	GOAL:
	
	  apples	Alice	 dogs
	 oranges	  Bob	 cats
	cherries	Carol	moose
	  banana	David	goose
'''
table_data = [	
	['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']]

'''
	INDEXES:

	apples = table_data[0][0]
	Alice = table_data[1][0]
	dogs = table_data[2][0]

'''
	
def get_longest_str_in_list(items):
	lengths = [len(item) for item in items]
	return sorted(lengths, reverse=True)[0]

def print_table(_list):
	row = ''
	for i in range(len(_list) + 1):
		for sub_list in _list:
			right_width = get_longest_str_in_list(sub_list)
			row += sub_list[i].rjust(right_width, ' ') + ' '
		print(row)
		row = ''
