import os
import mysql.connector
import requests
import json
import constants
import classes
from prettytable import PrettyTable


# Creating our cursor, tables, and inserting our data
affichage_style = PrettyTable()

pur_beurre = classes.Database()

print("***Creating Tables****")

category = classes.Category_table(constants.CATEGORY_TABLE)
aliment = classes.Aliment_table(constants.ALIMENT_TABLE)
substitut = classes.Substitut_table(constants.SUBSTITUT_TABLE)

category.insert_values_category()
if constants.ALIMENT_STATUS != "Done":  # We insert the data if neccesary
    aliment.insert_values_aliment()
    aliment.alter_table_aliment()

print("***All data inserted***.\n***Ready To Begin***\n")

path = 0
# The main part of our program
while path != 3:
    print(
        "1- Quel aliment souhaitez-vous remplacer ?\n"
        "2- Retrouvez mes aliments substitués\n"
        "3- Quitter\n"
        "4- Reinistialiser le programme")

    path = input()
    try:
        path = int(path)
    except ValueError:
        print("La valeur saisie n'est pas un chifrre")
        continue
    if path not in (1, 2, 3, 4):
        print("Veuillez choisir entre 1,2,3 ou 4")
        continue

    if path == 1:
        while True:  # Loop to make sure the category is chosen with an int

            print("Selectionnez la catégorie.")
            category.show_categories()
            choice_category = input()
            try:
                choice_category = int(choice_category)
            except ValueError:
                print("Veuillez rentrer un chiffre")
                continue
            if choice_category not in(range(1, 10)):
                print("Vous avez rentrer une categorie qui n'exite pas!")
                continue

            while True:  # Loop to make sure the aliment is chosen with an int

                print("Selectionnez l'aliment.")
                aliment.show_aliments(choice_category)
                choice_aliment = input()
                try:
                    choice_aliment = int(choice_aliment)
                except ValueError:
                        print("Veuillez rentrer un chiffre")
                        continue
                check = aliment.check_pair(choice_category, choice_aliment)
                # We make sure that the category/aliment is compatible
                if not check:
                    print("L'aliment choisie n'est pas dans cette catégorie")
                    continue
                else:
                    result = aliment.show_substitut(choice_category,
                                                    choice_aliment)

                if not result:  # If the list is empty
                    print("""L'aliment choisie est
                            déjà le meilleur de sa categorie.""")
                    break

                elif result:  # if the list exists
                    print("""Voici le meilleur substitut
                            de l'aliment selectionné.""")
                    affichage_style = PrettyTable()
                    affichage_style.field_names = ["ID", "Nom",
                                                   "Magasin", "Note",
                                                   "Description", "Lien"]

                    for item in result:
                        affichage_style.add_row(item)
                    print(affichage_style)

                    while True:  # To make sure we enter an int : either 1 or 2
                        print("""Souhaitez vous enregistrer ce resultat
                                ou quitter le programme ?
                                \n1- Sauvegarder\n2-Quitter\n""")
                        save = input()
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
                        substitut.add_favorite(result, choice_aliment)
                        print("Votre aliment a bien était sauvegardé !\n\n")
                    elif save == 2:
                        quit()
                    break
                break
            break
    if path == 2:
        print("Voici vos substituts favoris !")
        substitut.show_favorite()

    if path == 4:
        pur_beurre.reset()
        print("Le programme a été reinistaliser !\n"
              "Pour entammer une nouvelle session,"
              "veuillez le relancer.")
        break
os.system("pause")
