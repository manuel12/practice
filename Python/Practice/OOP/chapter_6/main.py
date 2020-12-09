# class MyObject:
# 	pass


# import datetime

# def middle(stock, date):
# 	symbol, current, high, low = stock
# 	return (((high + low) / 2), date)

# mid_value, date = middle(("FB", 75.00, 75.03, 74.90), 
# 	datetime.date(2014, 10, 31))


# from collections import namedtuple
# Stock = namedtuple("Stock", "symbol current high low")
# stock = Stock("FB", 75.00, high=75.03, low=74.90)


# stocks = {"GOOG": (613.30, 625.86, 610.50, ),
# 					"MSFT": (30.25, 30.70, 30.19)}


# random_keys = {}
# random_keys["astring"] = "somestring"
# random_keys[5] = "aninteger"
# random_keys[25.2] = "floats work too"
# random_keys[("abc", 123)] = "so do tuples"

# class AnObject:
# 	def __init__(self, avalue):
# 		self.avalue = avalue


# my_object = AnObject(14)
# random_keys[my_object] = "We can even store objects"
# my_object.avalue = 12

# try:
# 	random_keys[[1,2,3]] = "we cant store lists though"
# except:
# 	print("unable to store list\n")

# for key, value in random_keys.items():
# 	print("{} has value {}".format(key, value))


# def letter_frequency(sentence):
# 	frequencies = {}
# 	for letter in sentence:
# 		frequency = frequencies.setdefault(letter, 0)
# 		frequencies[letter] = frequency + 1
# 	return frequencies


# from collections import defaultdict

# def letter_frequency(sentence):
# 	frequencies = defaultdict(int)
# 	for letter in sentence:
# 		frequencies[letter] += 1
# 	return frequencies

# from collections import defaultdict

# num_items = 0

# def tuple_counter():
# 	global num_items
# 	num_items += 1
# 	return (num_items, [])

# d = defaultdict(tuple_counter)


# from collections import Counter

# def letter_frequency(sentence):
# 	return Counter(sentence)


# from collections import Counter

# responses = [
# 	"vanilla",
# 	"chocolate",
# 	"vanilla",
# 	"vanilla",
# 	"caramel",
# 	"strawberry",
# 	"vanilla"
# ]

# print("The children voted for {} ice cream".format(
# 	Counter(responses).most_common(1)[0][0]
# ))

# import string

# CHARACTERS = list(string.ascii_letters) + [" "]

# def letter_frequency(sentence):
# 	frequencies = [(c, 0) for c in CHARACTERS]
# 	for letter in sentence:
# 		index = CHARACTERS.index(letter)
# 		frequencies[index] = (letter, frequencies[index][1]+1)
# 	return frequencies

# from functools import total_ordering

# @total_ordering
# class WeirdSortee:
# 	def __init__(self, string, number, sort_num):
# 		self.string = string
# 		self.number = number
# 		self.sort_num = sort_num

# 	def __lt__(self, object):
# 		if self.sort_num:
# 			return self.number < object.number
# 		return self.string < object.string

# 	def __repr__(self):
# 		return "{}:{}".format(self.string, self.number)

# 	def __eq__(self):
# 		return all((
# 			self.string == object.string,
# 			self.number == object.number,
# 			self.sort_num == object.sort_num,
# 		))

# song_library = [("Phantom Of The Opera", "Sarah Brightman"),
# 		("Knocking On Heaven's Door", "Guns N' Roses"),
# 		("Captain Nemo", "Sarah Brightman"),
# 		("Patterns In The Ivy", "Opeth"),
# 		("November Rain", "Guns N' Roses"),
# 		("Beautiful", "Sarah Brightman"),
# 		("Mal's Song", "Vixy and Tony")]


# artists = set()
# for song, artist in song_library:
# 	artists.add(artist)

# print(artists)



# my_artists = {"Sarah Brightman", "Guns N' Roses", 
# 	"Opeth", "Vixy and Tony"}

# auburns_artists = {"Nickelback", "Guns N' Roses", 
# 	"Savage Garden"}

# print("All: {}".format(my_artists.union(auburns_artists)))
# print("Both: {}".format(auburns_artists.intersection(my_artists)))
# print("Either but not both: {}".format(
# 	my_artists.symmetric_difference(auburns_artists)))

# my_artists = {"Sarah Brightman", "Guns N' Roses",
# "Opeth", "Vixy and Tony"}
# bands = {"Guns N' Roses", "Opeth"}
# print("my_artists is to bands:")
# print("issuperset: {}".format(my_artists.issuperset(bands)))
# print("issubset: {}".format(my_artists.issubset(bands)))
# print("difference: {}".format(my_artists.difference(bands)))
# print("*"*20)
# print("bands is to my_artists:")
# print("issuperset: {}".format(bands.issuperset(my_artists)))
# print("issubset: {}".format(bands.issubset(my_artists)))
# print("difference: {}".format(bands.difference(my_artists)))


# class SillyInt(int):
# 	def __add__(self, num):
# 		return 0



# from collections import KeysView, ItemsView, ValuesView 

# class DictSorted(dict):
# 	def __new__(*args, **kwargs):
# 		new_dict = dict.__new__(*args, **kwargs)
# 		new_dict.ordered_keys = []
# 		return new_dict

# 	def __setitem__(self, key, value):
# 		'''self[key] = value syntax'''
# 		if key not in self.ordered_keys:
# 			self.ordered_keys.append(key)
# 		super().__setitem__(key, value)

# 	def setdefault(self, key, value):
# 		if key not in self.ordered_keys:
# 			self.ordered_keys.append(key)
# 		return super().setdefault(key, value)

# 	def keys(self):
# 		return KeysView(self)

# 	def values(self):
# 		return ValuesView(self)

# 	def items(self):
# 		return ItemsView(self)

# 	def __iter__(self):
# 		'''for x in self syntax'''
# 		return self.ordered_keys.__iter__()








