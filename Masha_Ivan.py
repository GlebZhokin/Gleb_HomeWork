# Вашингтон -7, Токио +6, Пекин +5, Бразилиа -6, Мадрид -1
ivan = 1
msk = int(input())
timeiv = msk - ivan
if timeiv <= 12:
	if timeiv == 7:
		print("Иван в Вашингтоне")
	elif timeiv == 6:
		print("Иван в Бразилиа")
	elif timeiv == 1:
		print("Иван в Мадриде")
	else:
		print("Неизвестно где Иван")
else:
	timeiv = ivan + 24 - msk
	if timeiv == 6:
		print("Иван в Токио")
	elif timeiv == 5:
		print("Иван в Пекине")
	else:
		print("Неизвестно где Иван")