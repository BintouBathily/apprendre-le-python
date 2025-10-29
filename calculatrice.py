nombre1 = input("choisi un nombre : ")
nombre2= input("choisi un second nombre : ")
if not nombre1.isnumeric() or not nombre2.isnumeric() : 
    print("Erreur : les deux nombres doivent etre des nombres entiers")
    raise SystemExit("Fin du programme")
nombre1= int(nombre1)
nombre2=int(nombre2)
operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']: ")
if operation not in ["+", "-", "*", "/"]:
    print("Erreur : le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme ")
if operation == "+" :
    resultat=nombre1 + nombre2
elif operation == "-" :
    resultat=nombre1-nombre2
elif operation == "*":
    resultat=nombre1*nombre2
elif operation == "/":
    if nombre2== 0 :
        print("Operation invalide")
        raise SystemExit("Fin du programme ")
    resultat = round(nombre1/nombre2, 2)

#afficher le resultat
print(f"Le résultat est : {resultat}")