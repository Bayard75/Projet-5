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
    
    def insert_values(self,id_category,category_name):
        
        link = "https://fr.openfoodfacts.org/categorie/pizzas.json"
        response = requests.get(link)
        category_json = json.loads(response.text)
        category_array =[]
        sql_formula_aliment = "INSERT INTO Aliment(barecode,name_aliment,category,store,grade,link) VALUES (%s,%s,%s,%s,%s,%s)" 
        
        for i in range(0,19):
            try:    
                category_array.append(
                (category_json["products"][i]["code"]
                ,category_json["products"][i]["product_name_fr"]
                ,id_category
                ,category_json["products"][i]["stores_tags"][0]
                ,category_json["products"][i]["nutrition_grades_tags"][0]
                ,category_json["products"][i]["url"]))
            except KeyError:
                category_array.append(None)
            except:
                print("Un erreur s'est produite pendant la création de l'array des données")

        
        self.cursor.executemany(sql_formula_aliment,category_array)
        self.database.commit()