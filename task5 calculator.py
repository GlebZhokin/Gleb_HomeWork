#сделал много break,чтобы программа прекращала работу сразу после ввода слова "выход", а не после ввода данных во 2 строку.
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