import os
import mysql.connector
import requests
import json
import constants
import classes
from prettytable import PrettyTable


# Creating our cursor, tables, and inserting our data
affichage_style = PrettyTable()

Pur_beurre = classes.Database()

print("***Creating Tables****")

Category = classes.Category_table(constants.CATEGORY_TABLE)
Aliment = classes.Aliment_table(constants.ALIMENT_TABLE)
Substitut = classes.Substitut_table(constants.SUBSTITUT_TABLE)

Category.insert_values_category()
if constants.ALIMENT_STATUS != "Done":  # We insert the data if neccesary
    Aliment.insert_values_aliment()
    Aliment.alter_table_aliment()

print("***All data inserted***.\n***Ready To Begin***\n")

path = 0
# The main part of our program
while path != 3:
    print(
        "1- Quel aliment souhaitez-vous remplacer ?\n"
        "2- Retrouvez mes aliments substitués\n"
        "3- Quitter")
    path = input()
    try:
        path = int(path)
    except ValueError:
        print("La valeur saisie n'est pas un chifrre")
        continue
    if path not in (1, 2, 3):
        print("Veuillez choisir entre 1 et 2 ou 3 pour quitter.")
        continue

    if path == 1:
        while True:  # Loop to make sure the category is chosen with an int

            print("Selectionnez la catégorie.")
            Category.show_categories()
            choice_category = input()
            try:
                choice_category = int(choice_category)
            except ValueError:
                print("Veuillez rentrer un chiffre")
                continue
            if choice_category not in(range(1,10)):
                print("Vous avez rentrer une categorie qui n'exite pas!")
                continue

            while True:  # Loop to make sure the aliment is chosen with an int

                print("Selectionnez l'aliment.")
                Aliment.show_aliments(choice_category)
                choice_aliment = input()
                try:
                    choice_aliment = int(choice_aliment)
                except ValueError:
                        print("Veuillez rentrer un chiffre")
                        continue
                check = Aliment.check_pair(choice_category, choice_aliment) # We make sure that the category/aliment is compatible
                if not check:
                    print("L'aliment choisie n'est pas dans cette catégorie")
                    continue
                else:
                    result = Aliment.show_substitut(choice_category, choice_aliment)

                if not result:  # If the list is empty
                    print("L'aliment choisie est déjà le meilleur de sa categorie.")
                    break

                elif result:  # if the list exists
                    print("Voici le meilleur substitut de l'aliment selectionné.")
                    affichage_style = PrettyTable()
                    affichage_style.field_names = ["ID", "Nom",
                                                   "Magasin", "Note",
                                                   "Description", "Lien"]

                    for item in result:
                        affichage_style.add_row(item)
                    print(affichage_style)

                    while True:  # To make sure we enter an int : either 1 or 2
                        save = input("""Souhaitez vous enregistrer ce resultat ou quitter le programme ?\n1- Sauvegarder\n2-Quitter\n""")
                        try:
                            save = int(save)
                        except ValueError:
                            print("Veuillez rentrer un chiffre")
                            continue
                        if save in (1, 2):
                            break
                        else:
                            print("Saisissez 1 ou 2 s'il vous plaît : ")
                            continue

                    if save == 1:
                        Substitut.add_favorite(result, choice_aliment)
                        print("Votre aliment a bien était sauvegardé !\n\n")
                    elif save == 2:
                        quit()
                    break
                break
            break
    if path == 2:
        print("Voici vos substituts favoris !")
        Substitut.show_favorite()

os.system("pause")
