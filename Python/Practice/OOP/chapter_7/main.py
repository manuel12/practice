# normal_list = [1,2,3,4,5]

# class CustomSequence():
# 	def __len__(self):
# 		return 5

# 	def __getitem__(self, index):
# 		return "x{0}".format(index)

# class FunkyBackwards():

# 	def __reversed__(self):
# 		return "BACKWARDS!"


# for seq in normal_list, CustomSequence(), FunkyBackwards():
# 	print("\n{}: ".format(seq.__class__.__name__), end="")
# 	for item in reversed(seq):
# 		print(item, end=", ")



# import sys
# filename = sys.argv[1]

# with open(filename) as file:
# 	for index, line in enumerate(file):
# 		print("{0}: {1}".format(index+1, line), end='')

# contents = "Some file contents"
# file = open("filename", "a")
# file.write(contents)
# file.close()


# with open('filename') as file:
# 	for line in file:
# 		print(line, end='')


# class StringJoiner(list):
# 	def __enter__(self):
# 		return self

# 	def __exit__(self, type, value, tb):
# 		self.result = "".join(self)


# import random, string

# with StringJoiner() as joiner:
# 	for i in range(15):
# 		joiner.append(random.choice(string.ascii_letters))

# print(joiner.result)

# def mandatory_args(x, y, z):
# 	pass

#mandatory_args("a string", a_variable, 5)

# def default_arguments(x, y, z, a="Some String", b=False):
# 	pass

#default_arguments("a string", variable, 8, "", True)

#default_arguments("a longer string", some_variable, 14)

#default_arguments("a string", variable, 14, b=True)


# def get_pages(*links):
# 	for link in links:
# 		# Downlaod thee link with urllib.
# 		print(link)

# get_pages()
# get_pages('http://www.archlinux.org')
# get_pages('http://www.archlinux.org', 'http://www.ccphillips.net/')


# class Options:
# 	default_options = {
# 		'port': 21,
# 		'host': 'localhost',
# 		'username': None,
# 		'password': None,
# 		'debug': False
# 	}

# 	def __init__(self, **kwargs):
# 		self.options = dict(Options.default_options)
# 		self.options.update(kwargs)

# 	def __getitem__(self, key):
# 		return self.options[key]


# import shutil
# import os.path

# def augmented_move(target_folder, *filenames, verbose=False, **specific):
# 	'''Move all the filenames into the target folder, allowing specific treatment 
# 	of certain files.'''

# 	def print_verbose(message, filename):
# 		'''Print the message  only if verbose is enabled.'''
# 		if verbose:
# 			print(message.format(filename))

# 	for filename in filenames:
# 		target_path = os.path.join(target_folder, filename)
		
# 		if filename in specific:
# 			if specific[filename] == 'ignore':
# 				print_verbose("Ignoring {0}", filename)
# 			elif specific[filename] == 'copy':
# 				print_verbose("Copying {0}", filename)
# 				shutil.copyfile(filename, target_path)
# 		else:
# 			print_verbose("Moving {0}", filename)
# 			shutil.move(filename, target_path)


# def show_args(arg1, arg2, arg3="THREE"):
# 	print(arg1, arg2, arg3)

# some_args = range(3)
# more_args = {
# 	"arg1": "ONE",
# 	"arg2": "TWO"
# }

# print("Unpacking a sequence: ", end=" ")

# show_args(*some_args)
# print("Unpacking a dict:", end=" ")

# show_args(**more_args)



# def my_function():
# 	print("The Function Was Called")
# my_function.description = "A silly function."


# def second_function():
# 	print("The second was called")
# second_function.description = "A sillier function."

# def another_function(function):
# 	print("The description:", end=" ")
# 	print(function.description)
# 	print("The name:", end=" ")
# 	print(function.__name__)
# 	print("The class:", end=" ")
# 	print(function.__class__)
# 	print("Now I'll call the function passed in.")
# 	function()

# another_function(my_function)
# another_function(second_function)


import datetime
import time

class TimedEvent:
	def __init__(self, endtime, callback):
		self.endtime = endtime
		self.callback = callback

	def ready(self):
		return self.endtime <= datetime.datetime.now()


class Timer:
	def __init__(self):
		self.events = []

	def call_after(self, delay, callback):
		end_time = datetime.datetime.now() + \
			datetime.timedelta(seconds=delay)

		self.events.append(TimedEvent(end_time, callback))

	def run(self):
		while True:
			ready_events = (e for e in self.events if e.ready())
			for event in ready_events:
				event.callback(self)
				self.events.remove(event)
			time.sleep(0.5)


def format_time(message, *args):
	now = datetime.datetime.now().strftime("%I:%M:%S")
	print(message.format(*args, now=now))

# def one(timer):
# 	format_time("{now}:  Called One")

# def two(timer):
# 	format_time("{now}:  Called Two")

# def three(timer):
# 	format_time("{now}:  Called Three")


class Repeater:
	def __init__(self):
		self.count = 0

	def __call__(self, timer):
		format_time("{now}: reapeat {0}", self.count)
		self.count += 1
		timer.call_after(5, self)

timer = Timer()
timer.call_after(5, Repeater())
format_time("{now}: Starting")
timer.run()

# timer = Timer()
# timer.call_after(1, one)
# timer.call_after(2, one)
# timer.call_after(2, two)
# timer.call_after(4, two)
# timer.call_after(3, three)
# timer.call_after(6, three)
# repeater = Repeater()
# timer.call_after(5, repeater.repeater)
# format_time("{now}: Starting")
# timer.run()

# class A# 	def print(self)::s

# 		print("my class is A")

# def fake_print():
# 	print("my class is not A")


# a = A()
# a.print()
# a.print = fake_print
# a.print()


