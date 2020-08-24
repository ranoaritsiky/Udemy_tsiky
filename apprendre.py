# a=19
# b=1
# try:
#     print (a/b)
# except ZeroDivisionError as divisionperzero:
#     print ("tsy mety ny zero")

# except TypeError as typing:
#     print ("tsy mety ny chaine de caractère")

def calc(*args):
    return args


func = calc("e", 1, 23, 2323, "2222")
