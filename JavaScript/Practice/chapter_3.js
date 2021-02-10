
const hummus = function(factor) {
	const ingredient = function(amount, unit, name) {
		let ingredientAmount = amount * factor;
		if (ingredientAmount > 1) 
			unit += "s";
		console.log(`${ingredientAmount} ${unit} of ${name}`)
	}

	ingredient(1, "can", "chickpeas");
	ingredient(0.25, "cup", "tahiti");
	ingredient(0.25, "cup", "lemon juice");
	ingredient(1, "clove", "garlic");
	ingredient(2, "tablespoon", "olive oil");
	ingredient(0.5, "teaspoon", "cumin");
}

// hummus(9)

function findSolution(target) {

	function find(current, history) {
		if(current == target) {
			return history;
		} else if (current > target) {
			return null;
		} else {
			return find(current + 5, `(${history} + 5)`) ||
				find(current * 3, `(${history} * 3)`);
		}
	}
	
	return find(1, "1")
}

// findSolution(24)

function printFarmInventory(cows, chickens) {
	let cowString = String(cows);

	while(cowString.length < 3) {
		cowString = "0" + cowString;
	}
	console.log(`${cowString} Cows`)

	let chickenString = String(chickens)

	while(chickenString.length < 3) {
		chickenString = "0" + chickenString
	}
	console.log(`${chickenString} Chickens`)
}

// printFarmInventory(7, 11)


function printZeroPaddedWithLabel(number, label) {
	let numberString = String(number);
	while(numberString.length < 3) {
		numberString = "0" + numberString;
	}
	console.log(`${numberString} ${label}`)
}

function printFarmInvetory (cows, chickens, pigs) {
	printZeroPaddedWithLabel(cows, "Cows")
	printZeroPaddedWithLabel(chickens, "Chickens")
	printZeroPaddedWithLabel(pigs, "Pigs")
}

// printFarmInvetory(7, 11, 3)

function zeroPad(number, width) {
	let string = String(number);
	while(string.length < width) {
		string = "0" + string;
	}
	return string;
}

function printFarmInventory(cows, chickens, pigs) {
	console.log(`${zeroPad(cows, 3)} Cows`)
	console.log(`${zeroPad(chickens, 3)} Chickens`)
	console.log(`${zeroPad(pigs, 3)} Pigs`)
}

printFarmInventory(7, 16, 3);




/*Exercises


Minimum

The previous chapter introduced the standard function Math.min that returns
its smallest argument. We can build something like that now. Write a function
min that takes two arguments and returns their minimum.*/

function minimum(a, b) {
	if (a > b)
		return b;
	else
		return a;
}




/*Recursion

We’ve seen that % (the remainder operator) can be used to test whether a
number is even or odd by using % 2 to see whether it’s divisible by two. Here’s
another way to define whether a positive whole number is even or odd:

• Zero is even.
• One is odd.
• For any other number N, its evenness is the same as N - 2.

Define a recursive function isEven corresponding to this description. The
function should accept a single parameter (a positive, whole number) and return
a Boolean.

Test it on 50*/

function isEven(number) {
	result = number - 2;
	if (result == 1) 
		return false
	else if (result == 0) 
		return true;
	else
		return isEven(result)
}



/*Bean counting

You can get the Nth character, or letter, from a string by writing "string"[N].
The returned value will be a string containing only one character (for example,
"b"). The first character has position 0, which causes the last one to be found at
position string.length - 1. In other words, a two-character string has length
2, and its characters have positions 0 and 1.

Write a function countBs that takes a string as its only argument and returns
a number that indicates how many uppercase “B” characters there are in the
string.

Next, write a function called countChar that behaves like countBs, except
it takes a second argument that indicates the character that is to be counted
(rather than counting only uppercase “B” characters). Rewrite countBs to
make use of this new function.*/

function countBs(string) {
	return countChar(string, "B")
}

function countChar(string, character) {
	countedChars = 0
	currPosition = 0
	while(string.length > currPosition) {
		currChar = string[currPosition]
		if(currChar == character)
			countedChars += 1;
		currPosition += 1
	}
	return countedChars
}