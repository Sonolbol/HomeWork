def get_power(arg,power):
	print(arg)
	a = 3
	for i in range(power):
		a *= arg
	return a


print(get_power(2,5))
