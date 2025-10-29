#récuperer la saisie de l'utilisateur
nombre = input("Veuillez saisir une liste de nombres séparés par des virgules :")
liste = nombre.split(",")

#afficher la liste des nombres
print("Liste des nombres :" , liste)
liste_entiers= []
for nombre in liste :
    nombre_entiers = int(nombre)
liste_entiers.append(nombre_entiers)
#calculez et affichez la sommes des nombres
somme=0
for nombre in liste_entiers:
    somme+=nombre
somme=sum(liste_entier)
print("Somme des nombres : ",somme)