# *** Логические и условные операции ***

# Операции сравнения

# x = "A"
# y = "A"

# оператор "равенства"
# мы справшиваем у компьютера вопрос : значение х равно значению у ?
from tkinter import Y

# res = x == y

# оператор неравенства
# res = x != y

# оператор "меньше"
# res = x < y 
# operator bolshe

# operator menshe ili ravno 
# res = x <= y 
# res = x >= y

# logicheskie operatory (logicheskie ventili)
var_1 = False
var_2 = True

# operator NE(not, inversiya)
res = not var_1 

# operatot I (and, conuinktsiya)
# vozvraschaet true tolko togda kogda oba znacheniya yavlyayutsya true
res = var_1 and var_2

# operator ili (or, disyunktsiya)
res = var_1 or var_2

# primer kombinatsii logicheskih operatorov i operatorov sraveniya
a = 5
b = 3
c = 3

res = ((a > b) and (b != c)) or (a == c)

# print(res)


# uslovnie operatory

a = 10
# operator IF
# if a == 0:
#     print("ravno nulyu")

# if not a == 0:
#     print("ne ravno nulyu")

# operator ELSE
# if a >= 0:
#     print("bolshe ili ravno nulyu")
# else:
#     print ("menshe nulya")

# operator ELIF(else IF)
# char = "A"
# if char == "A":
#     res = "literal A"
# elif char == "a":
#     res = "literal a"
# elif char == "B":
#     res = "literal b"
# elif char == "C":
#     res = "literal c"
# else:
#     res = "other charachter"

# print(res)

# primer "konsolnyi kalkulyator"

num_1 = int(input("vvedite pervoie chislo: " ))
num_2 = int(input("vvedite vtoroie chislo: " ))

operator = input("vvedite simvol operatsii: ")

if operator == "-":
    res = num_1 + num_2
elif operator == "-":
    res = num_1 - num_2
elif operator == "*":
    res = num_1 * num_2
elif operator == "/":
    res = num_1 / num_2
else:
    res = "simvol ne raspoznan"

print(f"rezultat: {res}")