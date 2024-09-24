n = int(input("Введите номер числа: "))
f1 = 0
f2 = 1
count = 0
while count < n:
	fsum = f1 + f2
	f1 = f2
	f2 = fsum
	count += 1
else:
	print (f1)