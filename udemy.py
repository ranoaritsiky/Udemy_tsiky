# liste = ["Java", "Python", "C++"]
# liste.insert(3, liste[1])
# liste.remove("Python")
# print (liste)

# liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
# print (liste[0:3])
# liste = [1, 2, 3, 4, 5]
# liste.append(6)
# if 6 in liste:
#     print ("Le nombre 6 a bien été ajouté à la liste.")
# print(liste)
mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp=str(mdp)
ln_mdp=len(mdp)

if ln_mdp =="":
    print (mdp_trop_court.upper())

elif ln_mdp <=8:
    print(mdp_trop_court.capitalize())

elif mdp.isdigit() and ln_mdp>8:
    print('Votre mot de passe ne contient que des nombres.')

else:
    print("Inscription terminée.")
