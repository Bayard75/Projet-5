#This file will be used to create our classes need
#At this point only one class will be created the database
import constants, requests, mysql.connector

class Database():
    
    def __init__(self,database,cursor,table1_formula,table2_formula):
        self.database = database
        self.cursor = cursor
        
        #creating our two tables
        try:
            self.cursor.execute(table1_formula)
            self.cursor.execute(table2_formula)
        except:
            print("Erreur dans la creation des tables.")
        #Inserting our first values into table1
        sql_category_formula ="INSERT INTO Category(id_category,name_category) VALUES (%s,%s)"
        try :
            self.cursor.executemany(sql_category_formula,constants.categories_to_display)
            self.database.commit()
        except:
            print ("Erreur dans l'insertion des données pour la table Categorie.")
    def insert_values(self,category):
        link = "http://fr.openfoodfacts.org/categorie/" + category +".json"
        r = requests.get(link)
        print(r.status_code)