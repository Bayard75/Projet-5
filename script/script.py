import os, mysql.connector, requests, json, constants, classes
from prettytable import PrettyTable


mydb = mysql.connector.connect( 
    host =constants.MYSQL_HOST,
    user = constants.MYSQL_USER,
    password=constants.MYSQL_PASSWORD,
    database =constants.MYSQL_DATABASE
)

#Creating our cursor, tables, and inserting our data
affichage_style = PrettyTable()

mycursor= mydb.cursor()
Pure_beurre = classes.Database(mydb, mycursor, constants.CATEGORY_TABLE, constants.ALIMENT_TABLE, constants.SUBSTITUT_TABLE, constants.FAVORITE_TABLE)

if Pure_beurre == 0:
    quit #If there's an error in the creation of our instance we stop

print("***Tables created***.\n")

Pure_beurre.insert_values_category()

if constants.ALIMENT_STATUS != "Done": #If the data hasn't been inserted we insert it
        Pure_beurre.insert_values_aliment() 
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

                    if result == 0:
                        print("Vous avez rentrez un chiffre qui n'est pas dans la catégorie.")
                        continue
                   
                    elif not result : #If the list is empty
                        print("L'aliment choisie est déjà le meilleur de sa categorie.")
                        break

                    elif result :#if the list exists
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
