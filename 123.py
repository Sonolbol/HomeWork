def func_name(arg,power):
	print(arg)
	a = 1
	for i in range(power):
		a *= arg
	return a
print(func_name(2,5))
