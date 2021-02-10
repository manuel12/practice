/*Exercises*/



/*Looping a triangle

Write a loop that makes seven calls to console.log to output the following
triangle:*/

function loopingATriangle() {
	symbol = '#'
	for(let i=0; symbol.length<8; i++) {
		console.log(symbol)
		symbol += '#'
	}
}
// loopingATriangle()



/*FizzBuzz

Write a program that uses console.log to print all the numbers from 1 to 100,
with two exceptions. For numbers divisible by 3, print "Fizz" instead of the
number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.

When you have that working, modify your program to print "FizzBuzz" for
numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz"
for numbers divisible by only one of those).

(This is actually an interview question that has been claimed to weed out
a significant percentage of programmer candidates. So if you solved it, your
labor market value just went up.)*/


function fizzBuzz() {
	for(i=0; i<=100; i++) {
		if(i % 3 == 0 && i % 5 == 0)
			console.log('FizzBuzz')
		else if (i % 3 == 0)
			console.log('Fizz')
		else if (i % 5 == 0) 
			console.log('Buzz')
		else
			console.log(i)
	}
}

// fizzBuzz()



/*Chessboard

Write a program that creates a string that represents an 8×8 grid, using newline
characters to separate lines. At each position of the grid there is either a space
or a "#" character. The characters should form a chessboard.

Passing this string to console.log should show something like this:*/

size = 20


function chessboard(size) {
	str = '';
	hashSymbol = true;

	for(let i=0; i<size; i++) {
		i % 2 == 0 ? (hashSymbol = true) : (hashSymbol = false)

		for(let j=0; j<size; j++) {
			if(j%2 == 0) 
				str += hashSymbol ? ' ' : '#'
			else
				str += hashSymbol ? '#' : ' '
		}
		str += '\n' 	

	}
	console.log(str)
}

chessboard(size)