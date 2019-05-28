import os, mysql.connector, requests, json, constants,classes

mydb = mysql.connector.connect(
    host =constants.mysql_host,
    user = constants.mysql_user,
    password=constants.mysql_password,
    database =constants.mysql_database
)
#Creating our cursor, tables, and inserting our data
mycursor= mydb.cursor()
Pure_beurre = classes.Database(mydb,mycursor,constants.Category_table,constants.Aliment_table)
print("***Tables created***.\n")
Pure_beurre.insert_values()
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
        while True:
                
                print("Selectionnez la catégorie.")
                Pure_beurre.show_categories()
                choice_category = input()
                try :
                    choice_category = int(choice_category)
                except ValueError:
                    print("Veuillez rentrer un chiffre")
                    continue
                Pure_beurre.show_aliments(choice_category)
                
                while True:
                    print("Selectionnez l'aliment.")
                    choice_aliment = input()
                    try :
                        choice_aliment = int(choice_aliment)
                    except ValueError:
                        print("Veuillez rentrer un chiffre")
                        continue

    
    
    
    
    
    elif path == 2:
        pass    
        
os.system("pause")