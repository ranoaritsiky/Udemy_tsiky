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

# import random
# a= random.randint(0,50)
# b= random.randint(0,50)
# if a==b:
#     print ("le nombre a et le nombre b sont égaux")
# elif a > b:
#     print ("Le nombre a est plus grand que le nombre b")
# else:
#     print ("Le nombre b est plus grand que le nombre a")

# import random 
# nombre_mystere=random.randint(0,100)
# nb=int(input("saisir un nombre: "))
# if nb == nombre_mystere:
#     print("Le nombre a et le nombre b sont égaux.")
# elif nb > nombre_mystere:
#         print ("Le nombre saisi est plus grand que le nombre random")
# else:
#     print ("Le nombre b est plus grand que le nombre a")
# import urllib2
# import time
# import threading

# class DoConnect(threading.Thread):
# 	def __init__(self):		
# 		threading.Thread.__init__(self)

# 	def run(self):
# 		self.running = True
# 		req = urllib2.Request('http://www.google.fr')
# 		while self.running:
# 			try:
# 				urllib2.urlopen(req)
# 			except IOError, e:
# 				print "Connect Error:", e.reason[1]
# 			else: print 'ping Ok'
# 			time.sleep(2)
		
# 	def stop(self):
# 		self.running = False

# connect_test = DoConnect()
# connect_test.start()
# time.sleep(5)
# connect_test.stop()

liste = ["Java", "Python", "C++"]
liste.insert(2, liste[1])