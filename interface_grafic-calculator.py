import json
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

def initialiser_fichier_json(fichier_json, cle_historique):
    if not os.path.exists(fichier_json):
        print(f"Le fichier '{fichier_json}' n'existe pas. Création du fichier avec une structure de base.")
        with open(fichier_json, 'w') as f:
            json.dump({cle_historique: []}, f, indent=4)

def ajouter_calcul_historique(fichier_json, cle_historique, calcul, historique_text):
    try:
        with open(fichier_json, 'r') as f:
            data = json.load(f)
        if cle_historique not in data:
            data[cle_historique] = []
        data[cle_historique].append(calcul)
        with open(fichier_json, 'w') as f:
            json.dump(data, f, indent=4)
        print("Le calcul a été ajouté à l'historique.")
        # Mettre à jour l'historique dans l'interface graphique
        historique_text.config(state=tk.NORMAL)
        historique_text.insert(tk.END, calcul + '\n')
        historique_text.config(state=tk.DISABLED)
    except json.JSONDecodeError:
        print(f"Le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def charger_historique(fichier_json, cle_historique, historique_text):
    try:
        with open(fichier_json, 'r') as f:
            data = json.load(f)
        if cle_historique in data:
            for calcul in data[cle_historique]:
                historique_text.insert(tk.END, calcul + '\n')
    except json.JSONDecodeError:
        print(f"Le fichier '{fichier_json}' n'est pas un fichier json valide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def calculatrice():
    fichier_json = 'historique.json'
    cle_historique = 'historique'
    initialiser_fichier_json(fichier_json, cle_historique)

    root = tk.Tk()
    root.title("Calculatrice")
    root.geometry("400x600")  # Taille de la fenêtre fixée
    root.resizable(False, False)  # Empêcher la redimension de la fenêtre
    root.config(bg="#f0f0f0")  # Couleur de fond claire pour l'interface

    expression = ""

    def press(num):
        nonlocal expression
        expression = expression + str(num)
        equation.set(expression)

    def equalpress():
        nonlocal expression
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = total
            ajouter_calcul_historique(fichier_json, cle_historique, f"{expression} = {total}", historique_text)
        except Exception as e:
            equation.set("Erreur")
            expression = ""

    def clear():
        nonlocal expression
        expression = ""
        equation.set("")

    def hide_window():
        root.withdraw()  # Masquer la fenêtre principale

    equation = tk.StringVar()

    # Champ d'entrée de l'expression
    expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 24, 'bold'), bd=10, relief="sunken", justify="right", bg="#ffffff")
    expression_field.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    button_frame = tk.Frame(root, bg="#f0f0f0")
    button_frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('Clear', 5, 0, 2, 1)  # Le bouton "Clear" couvre deux colonnes
    ]

    # Créer les boutons
    for (text, row, col, *args) in buttons:
        if text == 'Clear':
            button = tk.Button(button_frame, text=text, fg='white', bg='#d9534f', font=('Arial', 18, 'bold'), relief="raised", command=clear)
        elif text == '=':
            button = tk.Button(button_frame, text=text, fg='white', bg='#5bc0de', font=('Arial', 18, 'bold'), relief="raised", command=equalpress)
        else:
            button = tk.Button(button_frame, text=text, fg='white', bg='#0275d8', font=('Arial', 18, 'bold'), relief="raised", command=lambda t=text: press(t))
        
        # Le bouton "Clear" occupe deux colonnes et est centré
        button.grid(row=row, column=col, columnspan=args[0] if args else 1, sticky="nsew", padx=5, pady=5)

    for i in range(6):
        button_frame.grid_rowconfigure(i, weight=1)
        button_frame.grid_columnconfigure(i, weight=1)

    # Créer la zone de texte pour l'historique
    historique_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED, font=('Arial', 12), bg="#f9f9f9", bd=5, relief="sunken")
    historique_text.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    # Charger l'historique existant
    charger_historique(fichier_json, cle_historique, historique_text)

    # Lancer l'interface graphique
    root.after(5000, hide_window)  # Masque la fenêtre après 5 secondes (par exemple, si tu veux la fermer après un délai)

    root.mainloop()

calculatrice()
















