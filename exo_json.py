
import os
import json

dossier_courant = os.path.dirname(__file__)
pth=os.path.join(dossier_courant,"liste.json")

if os.path.exists(pth):
    with open(pth,"r") as file_read:
        liste_course=json.load(f)

else:
    liste_course=[]

