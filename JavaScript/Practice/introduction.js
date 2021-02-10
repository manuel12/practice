function factorial(n) {
	console.log(n)
	if(n == 0) {
		return 1;
	} else {
		return (n - 1) * n
	}
}

console.log(factorial(8))