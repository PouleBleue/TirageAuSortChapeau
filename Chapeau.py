import random

def saisir_equipes(nom_chapeau, nombre_equipes):
    equipes = []
    print(f"Veuillez saisir les noms des {nombre_equipes} équipes pour le {nom_chapeau}:")
    for i in range(nombre_equipes):
        equipe = input(f"Équipe {i + 1}: ")
        equipes.append(equipe)
    return equipes

def repartir_equipes(chapeaux, nombre_groupes):
    groupes = {chr(65 + i): [] for i in range(nombre_groupes)}  # Création des groupes dynamiquement
    for chapeau in chapeaux:
        random.shuffle(chapeau)  # Mélange aléatoirement les équipes du chapeau
        for i, equipe in enumerate(chapeau):
            groupe = chr(65 + (i % nombre_groupes))
            groupes[groupe].append(equipe)
    return groupes

def afficher_groupes(groupes):
    for groupe, equipes in sorted(groupes.items()):
        print(f"Groupe {groupe}: {', '.join(equipes)}")

def main():
    nombre_chapeaux = int(input("Combien de chapeaux (groupes d'équipes) souhaitez-vous ? "))
    nombre_equipes_par_chapeau = int(input("Combien d'équipes y a-t-il par chapeau ? "))
    nombre_groupes = int(input("Combien de groupes souhaitez-vous créer ? "))
    
    chapeaux = []
    for i in range(nombre_chapeaux):
        chapeau = saisir_equipes(f"chapeau {i + 1}", nombre_equipes_par_chapeau)
        chapeaux.append(chapeau)
    
    groupes = repartir_equipes(chapeaux, nombre_groupes)
    afficher_groupes(groupes)

if __name__ == "__main__":
    main()
