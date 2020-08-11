employes = {
    "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
    "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
    "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
}
print (employes)
if "id03" in employes:
    del employes["id03"]

if "id02" in employes:
    employes["id02"]["age"]=26

if "id01" in employes:
    print (employes["id01"]["age"])
# print(employes)
