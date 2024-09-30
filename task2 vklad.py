P = int(input("Введите процент по вкладу: "))
X = int(input("Введите количество вложенных рублей: "))
Y = int(input("Введите количество вложенных копеек: "))
Y /= float(100)
X += float(Y)
FinalSum = (X / 100 * P + X)
X = int(FinalSum)
Y = FinalSum * 100 % 100
print ("Сумма вашего вклада через год:", X, "руб", int(Y), "коп")