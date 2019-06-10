import os, mysql.connector, requests, json, constants, classes
from prettytable import PrettyTable

mydb = mysql.connector.connect( 
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)
#Creating our cursor, tables, and inserting our data
affichage_style = PrettyTable()

mycursor= mydb.cursor()
Pure_beurre = classes.Database(mydb,mycursor, constants.Category_table, constants.Aliment_table, constants.Substitut_table, constants.Favorite_table)

if Pure_beurre == False:
    quit

print("***Tables created***.\n")

if Pure_beurre.insert_values_category() == True: #If the category values haven't already been inserted we assume that the aliment ones haven't been too
    Pure_beurre.insert_values_aliment() #This allows us to gain some time when we relaunch the program
    Pure_beurre.alter_table_aliment()
    
print("***All data inserted***.\n")
print("***Ready to begin***.\n")


path = 0
#The main part of our program
while path !=3:
    
    print(" 1- Quel aliment souhaitez-vous remplacer ?\n 2- Retrouvez mes aliments substitués\n 3- Quitter")
    path = input()
    try:
        path = int(path)
    except ValueError:
        print("La valeur saisie n'est pas un chifrre")
        continue
    if path not in (1,2,3):
        print("Veuillez choisir entre 1 et 2 ou 3 pour quitter.")
        continue

    if path == 1:
        while True: # Loop to make sure the category is chosen with an int

                print("Selectionnez la catégorie.")
                Pure_beurre.show_categories()
                choice_category = input()
                try :
                    choice_category = int(choice_category)
                except ValueError:
                    print("Veuillez rentrer un chiffre")
                    continue
                
                while True: # Loop to make sure the aliment is chosen with an int

                    print("Selectionnez l'aliment.")
                    Pure_beurre.show_aliments(choice_category)

                    choice_aliment = input()
                    try :
                        choice_aliment = int(choice_aliment)
                    except ValueError:
                        print("Veuillez rentrer un chiffre")
                        continue
                    result = Pure_beurre.show_substitut(choice_category,choice_aliment)
                    if result == None:
                        print("Vous avez rentrez un chiffre qui n'est pas dans la catégorie.")
                        continue
                    elif result != None:
                        print("Voici le meilleur substitut de l'aliment selectionné.")
                        affichage_style.field_names=["Numero","Nom","Category","Magasin","Nutriscore","Description","Lien"]
                        affichage_style.add_row((result[0]))
                        print(affichage_style)
                    
                        save = input("Souhaitez vous enregistrer ce resultat ou quitter le programme ?\n1- Sauvegarder\n2-Quitter\n")
                    
                    try:
                        save= int(save)
                    except ValueError:
                        print("Saissiez 1 ou 2 s'il vous plait.")
                        continue
                    if save == 1 :
                        Pure_beurre.add_favorite(result,choice_aliment) 
                        print("Votre aliment a bien était sauvegardé !\n\n")
                        break
                    if save == 2:
                        quit()
                break
        continue
    if path == 2:
        Pure_beurre.show_favorite()

os.system("pause")
