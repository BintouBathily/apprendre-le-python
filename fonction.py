#programme qui calcul el salaire horaire

def salaire_mensuel(salaire_annuel):
    resultat= salaire_annuel / 12
    return resultat

def salaire_hebdomadaire(salaire_mensuel):
    resultat= salaire_mensuel/4
    return resultat

def salaire_horaire(salaire_hebdomadaire, heures_travaillees ) :
    resultat = salaire_hebdomadaire/ heures_travaillees
    return resultat

salaire_annuel = float(input("quel est votre saire annuel? : "))
heures_travaillees = float(input("quels est le nombre d'heures travaillées par semaine? :"))

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire= salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

print(f"votre salaire horaire est de {horaire :.2f} euros.")