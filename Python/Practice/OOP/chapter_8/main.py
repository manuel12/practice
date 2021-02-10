# template = "Hello {}, you are currently {}."
# print(template.format('Dusty', 'writing'))

# template = "Hello {0}, you are {1}. Your name is {0}."
# print(template.format('Dusty', 'writing'))

# template = """
# public class {0} {{
# 	public static void main(String[] 	 args) {{
# 		System.out.println("{1}");
# 	}}
# }}"""
# print(template.format("MyClass", "print('hello world')"));

# template = """
# FROM: <{from_email}>
# To: <{to_email}>
# Subject: {subject}

# {message}"""

# print(template.format(
# 	from_email = "a@example.com",
# 	to_email = "b@example.com",
# 	message = "Here's some mail for you. "
# 	" Hope you enjoy the message!",
# 	subject = "You have mail!"
# ))

# print("{} {label} {}".format("x", "y", label="z"))


# emails = ("a@example.com", "b@example.com")
# message = {
# 	'subject': "You have Mail!",
# 	'message': "Here's some mail for you!",
# }

# template = """
# From:<{0[0]}>
# To:<{0[1]}>
# Subject: {message[subject]}
# {message[message]}"""
# print(template.format(emails, message=message))



# emails = ("a@example.com", "b@example.com")
# message = {
# 	'emails': emails
# 	'subject': "You have Mail!",
# 	'message': "Here's some mail for you!",
# }

# template = """
# From:<{0[emails][0]}>
# To:<{0[emails][1]}>
# Subject: {0[subject]}
# {0[message]}"""
# print(template.format(message))


# class EMail:
# 	def __init__(self, from_addr, to_addr, subject, message):
# 		self.from_addr = from_addr
# 		self.to_addr = to_addr
# 		self.subject = subject
# 		self.message = message

# email = EMail("a@example.com", "b@example.com", 
# 	"You Have Mail!", 
# 	"Here's some mail for you!")

# template = """
# From: <{0.from_addr}>
# To: <{0.to_addr}>
# Subject: {0.subject}
# {0.message}"""


# print(template.format(email))

# subtotal = 12.32
# tax = subtotal * 0.07
# total = subtotal + tax

# print("Sub: ${0} Tax: ${1} Total: ${total}".format(
# 	subtotal, tax, total=total))

# print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
# 	"Total: ${total: 0.2f}".format(
# 		subtotal, tax, total=total))


# orders = [('burger', 2, 5),
# 	('fries', 3.5, 1),
# 	('cola', 1.75, 3)]

# print("PRODUCT QUANTITY PRICE SUBTOTAL")

# for product, price, quantity in orders:
# 	subtotal = price * quantity
# 	print("{0:10s}{1: ^9d} ${2: <8.2f}${3: >7.2f}".format(
# 	product, quantity, price, subtotal))



# import datetime

# print("{0:%Y-%m-%d %I:%M:p}".format(
# 	datetime.datetime.now()))


# characters = b'\x63\x6c\x69\x63\x68\xe9'
# print(characters)
# print(characters.decode("latin-1"))

# characters = "cliché"
# print(characters.encode("UTF-8"))
# print(characters.encode("latin-1"))
# print(characters.encode("CP437"))
# print(characters.encode("ascii"))


# b = bytearray(b"abcdefgh")
# b[4:6] = b"\x15\xa3"
# print(b)

# b = bytearray(b"abcdefgh")
# b[3] = ord(b'g')
# b[4] = 68
# print(b)


# import re

# search_string = "hello world"
# pattern = "ello world"

# match = re.match(pattern, search_string)

# if match:
# 	print("regex matches!")
# else: print("no match")

# import sys
# import re

# pattern =  sys.argv[1]
# search_string = sys.argv[2]
# match = re.match(pattern, search_string)

# if match:
# 	template = "'{}' matches pattern '{}'"
# else:
# 	template = "'{}'does not match pattern '{}'"

# print(template.format(search_string, pattern))



# import re

# pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
# search_string = "some.user@example.com"
# match = re.match(pattern, search_string)

# if match:
# 	print(match.groups())
# 	domain = match.groups()[0]
# 	print(domain)


# import pickle

# some_data = ["a list", "containing", 5, 
# 	"values including amother list",
# 	["inner", "list"]]

# with open("pickled_list", 'wb') as file:
# 	pickle.dump(some_data, file)

# with open("pickled_list", 'rb') as file:
# 	loaded_data = pickle.load(file)

# print(loaded_data)
# assert loaded_data == some_data

# from threading import Timer
# import datetime
# from urllib.request import urlopen

# class UpdateURL:
# 	def __init__(self, url):
# 		self.url = url
# 		self.contents = ''
# 		self.last_updated = None
# 		self.update()

# 	def update(self):
# 		self.contents = urlopen(self.url).read()
# 		self.last_updated = datetime.datetime.now()
# 		self.schedule()

# 	def schedule(self):
# 		self.timer = Timer(3600, self.update)
# 		self.timer.setDaemon(True)
# 		self.timer.start()

# 	def __getstate__(self):
# 		new_state = self.__dict__.copy()
# 		if 'timer' in new_state:
# 			del new_state['timer']
# 		return new_state

# 	def __setstate__(self, data):
# 		self.__dict__ = data
# 		self.schedule()


import json

class Contact:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def full_name(self):
		return("{} {}".format(self.first, self.last))


class ContactEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Contact):
			return { 
				'is_contact': True,
				'first': obj.first,
				'last': obj.last,
				'full': obj.full_name}
		return super().default(obj)


def decode_contact(dic):
	if dic.get('is_contact'):
		return Contact(dic['first'], dic['last'])
	else:
		return dic