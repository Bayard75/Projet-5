#This file will be used to create our classes need
#At this point only one class will be created the database
import constants, requests, mysql.connector,json

mysql.connector.IntegrityError
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
        try :
            sql_category_formula ="INSERT INTO Category(id_category,name_category) VALUES (%s,%s)"
            self.cursor.executemany(sql_category_formula,constants.categories_to_display)
            self.database.commit()
        except:
            print ("Erreur dans l'insertion des données pour la table Categorie.")
    
    def insert_values(self):
        
        id_category = 0
        for names in constants.categories_to_display:
            for page in range(1,4):
                link = f"https://fr.openfoodfacts.org/categorie/{constants.categories_to_display[id_category][1]}/{page}.json"
                response = requests.get(link)
                category_json = json.loads(response.text)
            
                for products in category_json["products"]:
                    try:  
                        sql_formula_aliment = f'INSERT IGNORE INTO Aliment(id_aliment,name_aliment,category,store,grade,link) VALUES ("{None}","{products["product_name"]}",{id_category+1},"{products["stores"]}","{products["nutrition_grades_tags"][0]}","{products["url"]}")'
                        self.cursor.execute(sql_formula_aliment)
                        self.database.commit()
                
                    except KeyError:    
                        sql_key_error = f'INSERT IGNORE INTO Aliment(id_aliment,name_aliment,category,store,grade,link) VALUES ("{None}","{products["product_name"]}","{id_category+1}","Non disponible","{products["nutrition_grades_tags"][0]}","{products["url"]}")'
                        self.cursor.execute(sql_key_error)
                        self.database.commit()

            id_category +=1


        sql_delete_empty = 'DELETE FROM Aliment WHERE grade IN ("unknown","not-applicable")'
        self.cursor.execute(sql_delete_empty)
        self.database.commit()

    def category_choice(self):
        show_cat = "SELECT * FROM Category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()
        
        for categories in showing:
            print("|| ",categories," ||")

        choice = int(input())
        query = f"SELECT id_aliment,name_aliment FROM Aliment where category = {choice}"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result :
            print (row)

    def terminate(self):
        sql_terminate_animal = "DROP TABLE IF EXISTS animal"
        sql_terminate_category ="DROP TABLE IF EXISTS category"

        self.cursor.execute(sql_terminate_animal)
        self.cursor.execute(sql_terminate_category)
