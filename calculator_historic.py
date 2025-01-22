import json
import os

def initialiser_fichier_json(fichier_json, cle_historique):
    if not os.path.exists(fichier_json):
        print(f"le fichier '{fichier_json}' n'existe pas. création du fichier avec une structure de base.")
        with open(fichier_json, 'w') as f:
            json.dump({cle_historique: []}, f, indent=4)

def sauvegarder_historique_avant_suppression(fichier_json, cle_historique, fichier_sauvegarde):
    try:
        # lire le fichier json
        with open(fichier_json, 'r') as f:
            data = json.load(f)

        # sauvegarder l'historique dans un fichier de sauvegarde
        with open(fichier_sauvegarde, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"l'historique a été sauvegardé dans '{fichier_sauvegarde}' avant suppression.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def supprimer_historique(fichier_json, cle_historique, fichier_sauvegarde):
    try:
        # sauvegarder l'historique avant suppression
        sauvegarder_historique_avant_suppression(fichier_json, cle_historique, fichier_sauvegarde)

        # lire le fichier json
        with open(fichier_json, 'r') as f:
            data = json.load(f)

        # supprimer la clé de l'historique si elle existe
        if cle_historique in data:
            del data[cle_historique]

        # écrire les modifications dans le fichier json
        with open(fichier_json, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"l'historique '{cle_historique}' a été supprimé avec succès.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def restaurer_historique(fichier_json, cle_historique, fichier_sauvegarde):
    try:
        # lire le fichier de sauvegarde
        with open(fichier_sauvegarde, 'r') as f:
            data = json.load(f)

        # restaurer l'historique dans le fichier json
        with open(fichier_json, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"l'historique a été restauré à partir de '{fichier_sauvegarde}'.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_sauvegarde}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def voir_historique(fichier_json, cle_historique):
    try:
        # lire le fichier json
        with open(fichier_json, 'r') as f:
            data = json.load(f)

        # afficher l'historique si la clé existe
        if cle_historique in data:
            print(f"historique '{cle_historique}':")
            for calcul in data[cle_historique]:
                print(calcul)
        else:
            print(f"la clé '{cle_historique}' n'existe pas dans le fichier json.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def sauvegarder_historique_txt(fichier_json, cle_historique, repertoire_txt, fichier_txt):
    try:
        # lire le fichier json
        with open(fichier_json, 'r') as f:
            data = json.load(f)

        # créer le répertoire s'il n'existe pas
        if not os.path.exists(repertoire_txt):
            os.makedirs(repertoire_txt)

        # sauvegarder l'historique dans un fichier txt si la clé existe
        if cle_historique in data:
            chemin_complet = os.path.join(repertoire_txt, fichier_txt)
            with open(chemin_complet, 'w') as f:
                for calcul in data[cle_historique]:
                    f.write(calcul + '\n')
            print(f"l'historique '{cle_historique}' a été sauvegardé dans '{chemin_complet}'.")
        else:
            print(f"la clé '{cle_historique}' n'existe pas dans le fichier json.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def calculatrice(fichier_json, cle_historique):
    print("bienvenue ! prêt à additionner un peu de fun à vos chiffres ?")
    print("veuillez entrer la première valeur :")
    try:
        valeur1 = float(input())
    except ValueError:
        print("veuillez entrer un nombre valide.")
        return

    print("veuillez entrer l'opérateur (+, -, *, /) :")
    operateur = input()

    print("veuillez entrer la deuxième valeur :")
    try:
        valeur2 = float(input())
    except ValueError:
        print("veuillez entrer un nombre valide.")
        return

    if operateur == '+':
        resultat = valeur1 + valeur2
    elif operateur == '-':
        resultat = valeur1 - valeur2
    elif operateur == '*':
        resultat = valeur1 * valeur2
    elif operateur == '/':
        if valeur2 != 0:
            resultat = valeur1 / valeur2
        else:
            print("erreur : division par zéro.")
            return
    else:
        print("opérateur non valide.")
        return

    print(f"le résultat est : {resultat}")

    # ajouter le calcul à l'historique
    try:
        with open(fichier_json, 'r') as f:
            data = json.load(f)

        if cle_historique not in data:
            data[cle_historique] = []

        data[cle_historique].append(f"{valeur1} {operateur} {valeur2} = {resultat}")

        with open(fichier_json, 'w') as f:
            json.dump(data, f, indent=4)

        print("le calcul a été ajouté à l'historique.")
    except json.JSONDecodeError:
        print(f"le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"une erreur s'est produite : {e}")

def menu():
    fichier_json = 'historique.json'
    cle_historique = 'historique'
    repertoire_txt = 'historique_txt'
    fichier_txt = 'historique.txt'
    fichier_sauvegarde = 'historique_sauvegarde.json'

    # initialiser le fichier json si nécessaire
    initialiser_fichier_json(fichier_json, cle_historique)

    while True:
        print("\n === menu === :")
        print("\n1. supprimer l'historique")
        print("2. voir l'historique")
        print("3. sauvegarder l'historique dans un fichier txt")
        print("4. utiliser la calculatrice")
        print("5. restaurer l'historique")
        print("6. quitter")

        choix = input("veuillez choisir une option (1-6) : ")

        if choix == '1':
            supprimer_historique(fichier_json, cle_historique, fichier_sauvegarde)
        elif choix == '2':
            voir_historique(fichier_json, cle_historique)
        elif choix == '3':
            sauvegarder_historique_txt(fichier_json, cle_historique, repertoire_txt, fichier_txt)
        elif choix == '4':
            calculatrice(fichier_json, cle_historique)
        elif choix == '5':
            restaurer_historique(fichier_json, cle_historique, fichier_sauvegarde)
        elif choix == '6':
            print("à bientôt pour de nouvelles aventures mathématiques !")
            break
        else:
            print("option invalide. merci de choisir une option disponible.")

# lancer le menu
menu()










