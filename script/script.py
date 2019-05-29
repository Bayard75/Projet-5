import os, mysql.connector, requests, json, constants, classes, pickle

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)
#Creating our cursor, tables, and inserting our data
mycursor= mydb.cursor()
Pure_beurre = classes.Database(mydb,mycursor, constants.Category_table, constants.Aliment_table, constants.Substitut_table, constants.Favorite_table)
print("***Tables created***.\n")
Pure_beurre.insert_values_category()
Pure_beurre.insert_values_aliment()
Pure_beurre.insert_values_substitut()
Pure_beurre.alter_table_aliment()
print("***All data inserted***.\n")
print("***Ready to begin***.\n")
result = Pure_beurre.show_substitut(1, 1)



#The main part of our program
while True:
    
    print(" 1- Quel aliment souhaitez-vous remplacer ?\n 2- Retrouvez mes aliemnts substitués")
    path = input()
    try:
        path = int(path)
    except ValueError:
        print("La valeur saisie n'est pas un chifrre")
        continue
    if path not in (1,2):
        print("Veuillez choisir entre 1 et 2.")
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
                    if result == False:
                        print("Vous avez rentrez un chiffre qui n'est pas dans la catégorie.")
                        continue
                    print(f"Voici le meilleur substitut pour l'aliment selectionné:\nNom = {result[0][0]}\nMagasin = {result[0][1]}\nNutriScore = {result[0][2]}\nDescription = {result[0][3]}\nLien = {result[0][4]}")
                    save = input("Souhaitez vous enregistrer ce resultat ou quitter le programme ?\n1- Sauvegarder\n2-Quitter\n")
                    
                    try:
                        save= int(save)
                    except ValueError:
                        print("Saissiez 1 ou 2 s'il vous plait.")
                        continue
                    if save == 1 :
                        Pure_beurre.add_favorite(result) 
                    break
                break
        break

    if path == 2:
        Pure_beurre.insert_values_favorite()
        Pure_beurre.show_favorite()
Pure_beurre.terminate()
os.system("pause")