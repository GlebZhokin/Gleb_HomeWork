message = input("Введите сообщение: ")
ch = ""
for i in message:
    if i == "а":        
        i = "о"
    elif i == "о":
        i = "а"
    elif i == "е":
        i = "и"
    elif i == "и":
        i = "е"    
    ch += i
print(ch)