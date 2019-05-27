#This file will be used to create our classes need
#At this point only one class will be created the database
import constants, requests, mysql.connector,json

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
    
    def insert_values(self):
        
        id_category = 0
        i = 1
        for names in constants.categories_to_display:
            
            link = f"https://fr.openfoodfacts.org/categorie/{constants.categories_to_display[id_category][1]}.json"
            response = requests.get(link)
            category_json = json.loads(response.text)
            
            id_category +=1
            for products in category_json["products"]:
                try:  
                    sql_formula_aliment = f'INSERT INTO Aliment(id_aliment,name_aliment,category,store,grade,link) VALUES ({i},"{products["product_name"]}",{id_category},"{products["stores"]}","{products["nutrition_grades_tags"][0]}","{products["url"]}")'
                    i +=1
                    self.cursor.execute(sql_formula_aliment)
                    self.database.commit()
                
                except KeyError:    
                    sql_key_error = f'INSERT INTO Aliment(id_aliment,name_aliment,category,store,grade,link) VALUES ({i},"{products["product_name"]}",{id_category}," ","{products["nutrition_grades_tags"][0]}","{products["url"]}")'
                    self.cursor.execute(sql_key_error)
                    self.database.commit()
                    i +=1
