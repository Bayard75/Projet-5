import os, mysql.connector, requests, json, constants,classes

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)
#Creating our cursor, tables, and inserting our data
mycursor= mydb.cursor()
Pure_beurre = classes.Database(mydb,mycursor,constants.Category_table,constants.Aliment_table,constants.Substitut_table)
print("***Tables created***.\n")
Pure_beurre.insert_values_category()
Pure_beurre.insert_values_aliment()
Pure_beurre.insert_values_substitut()
print("***All data inserted***.\n")
print("***Ready to begin***.\n")

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
                Pure_beurre.show_aliments(choice_category)
                
                while True: # Loop to make sure the aliment is chosen with an int

                    print("Selectionnez l'aliment.")
                    choice_aliment = input()
                    try :
                        choice_aliment = int(choice_aliment)
                    except ValueError:
                        print("Veuillez rentrer un chiffre")
                        continue
                    
                    result = Pure_beurre.show_substitut(choice_category)
                    for row in result:
                        print(f"Voici le meilleur substitut pour votre aliment:\n{row[0]}\nNote = {row[2]}\nMagasin = {row[1]}\nDescription = {row[3]}\nURL = {row[4]}")
                    break
                break
        break
    elif path == 2:
        pass    
        
os.system("pause")