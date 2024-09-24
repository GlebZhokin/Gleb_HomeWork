num = int(input("Введите число: "))
hh = num // 3600
mm = num % 3600 // 60
ss = num % 3600 % 60
print ("Время:", hh, mm, ss)