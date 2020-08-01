# def nb_mystere(nb):
#     nb_myst = 7
#     nb = int(input("nombre mystere "))
#     if nb != nb_myst:
#         return False    
#     else:
#         return True
# print (nb_mystere(10))

# nb_myst=7
# quest=int(input("saisir un nombre "))

# if quest ==nb_myst:
#     print("Bravo")
# elif quest > nb_myst:
#     print (f"{quest} est superieur a {nb_myst}")
# elif quest < nb_myst:
#     print (f"{quest} est inferieur a {nb_myst}")

import random
a= random.randint(0,50)
b= random.randint(0,50)
if a==b:
    print ("le nombre a et le nombre b sont égaux")
elif a > b:
    print ("Le nombre a est plus grand que le nombre b")
else:
    # print ("Le nombre b est plus grand que le nombre a")