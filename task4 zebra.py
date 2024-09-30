num = int(input("Введите номер зебры: "))
sharp_strip = "####"
dot_strip = "••••"
count = 1
print("Ваша зебра:")
while count <= num:
		if count % 2 != 0:
			count = num / num + count
			print(sharp_strip)
		else:
			count = num / num + count
			print(dot_strip)