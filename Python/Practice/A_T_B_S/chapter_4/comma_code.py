spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(_list):
	last_index = _list[-1]
	comma_list = ['and ' + str(index) if index == last_index else str(index) for index in _list]
	return ", ".join(comma_list)

