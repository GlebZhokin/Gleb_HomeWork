divisible = input("Введите делимое: ")
if divisible == "выход":
  print ("До свидания!")
else:
  divider = input("Введите делитель: ")
  while divisible != "выход":
    try:
      divisible = float(divisible)
      divider = float(divider)
      divisible /= divider      
      print("Частное:", divisible)
      divisible = input("Введите делимое: ")
      if divisible == "выход":
        print("До свидания!")
        break
      else:
        divider = input("Введите делитель: ")            
    except ZeroDivisionError:
      print("Нельзя делить на 0!")
      divisible = input("Введите делимое: ")
      if divisible == "выход":
        print("До свидания!")
        break
      else:
        divider = input("Введите делитель: ") 
    except ValueError:
      print("Введите число!")
      divisible = input("Введите делимое: ")
      if divisible == "выход":
        print("До свидания!")
        break
      else:
        divider = input("Введите делитель: ") 
  else:
    print("До свидания!")