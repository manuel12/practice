# Collatz w/ Try Catch

def collatz(number):
	if number % 2 == 0:
		collatz_num = number // 2
	else:
		collatz_num = 3 * number + 1
	print(collatz_num)
	return collatz_num

collatz_result = None

while True:
	try:		
		if not collatz_result:
			user_input = int(input('Enter number: '))
			collatz_result = collatz(user_input)
		
		if collatz_result == 1:
			break
		collatz_result = collatz(collatz_result)

	except ValueError:
		print('Please enter a numerical character only!')

