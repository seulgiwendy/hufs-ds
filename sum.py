def sum(n):
	if (n == 1):
		return 1
	if (n != 0):
		return n + sum(n - 1)
	else:
		return n

print(sum(10))

