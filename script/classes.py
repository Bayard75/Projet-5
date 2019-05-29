#This file will be used to create our classes need
#At this point only one class will be created the database
import constants, requests, mysql.connector,json, pickle

mysql.connector.IntegrityError
class Database():
    
    def __init__(self,database,cursor,table1_formula,table2_formula,table3_formula,table4_formula):
        self.database = database
        self.cursor = cursor
        
        #creating our two tables
        try:
            self.cursor.execute(table1_formula)
            self.cursor.execute(table2_formula)
            self.cursor.execute(table3_formula)
            self.cursor.execute(table4_formula)
        except:
            print("Erreur dans la creation des tables.")
        
    def insert_values_category(self):
        #Inserting our first values into table1
        try :
            sql_category_formula ="INSERT INTO Category(id_category,name_category) VALUES (%s,%s)"
            self.cursor.executemany(sql_category_formula,constants.categories_to_display)
            self.database.commit()
        except:
            print ("Erreur dans l'insertion des données pour la table Categorie.")
    
    def insert_values_aliment(self):
        
        id_category = 0
        for names in constants.categories_to_display:
            for page in range(1,3):
                link = f"https://fr.openfoodfacts.org/categorie/{constants.categories_to_display[id_category][1]}/{page}.json"
                response = requests.get(link)
                category_json = json.loads(response.text)
            
                for products in category_json["products"]:
                    try:  
                        sql_formula_aliment = f"""INSERT IGNORE INTO Aliment(id_aliment,name_aliment,category,store,grade,description,link) VALUES ("{None}","{products["product_name"]}",{id_category+1},"{products["stores"].replace("''","Non Disponibe")}","{products["nutrition_grades_tags"][0]}","{products["generic_name_fr"].replace("''","Non disponible")}","{products["url"]}")"""
                        self.cursor.execute(sql_formula_aliment)
                        self.database.commit()
                
                    except KeyError:    
                        continue

            id_category +=1


        sql_delete_empty = 'DELETE FROM Aliment WHERE grade IN ("unknown","not-applicable")'
        self.cursor.execute(sql_delete_empty)
        self.database.commit()

    def insert_values_substitut(self):
        sql_substitut ="INSERT IGNORE INTO substitut (id_aliment,category) SELECT id_aliment, category FROM Aliment WHERE grade = 'a' OR grade ='b' OR grade ='c'  ORDER BY grade"
        self.cursor.execute(sql_substitut)
        self.database.commit()


    def insert_values_favorite(self):
        
       #Add loop to go trough each object not just the fisrt one
        with open(r"files\favorite_list.txt","rb") as list_fav:
            favs = pickle.load(list_fav)
        for row in favs:
            querry = f"""INSERT INTO Favorite (name_aliment, category, store, grade, description, link) VALUES ("{row[0]}",{row[1]},"{row[2]}","{row[3]}",
            "{row[4]}","{row[5]}")"""
        self.cursor.execute(querry)
        self.database.commit()

    def alter_table_aliment(self):
        sql_alter ="ALTER TABLE Aliment ADD COLUMN substitut SMALLINT NOT NULL"
        self.cursor.execute(sql_alter)
        sql_add_sub="UPDATE Aliment INNER JOIN Substitut ON Aliment.category = Substitut.category SET Aliment.substitut = Substitut.id_aliment"
        self.cursor.execute(sql_add_sub)
        self.database.commit()
    
    
    def show_categories(self):
        show_cat = "SELECT * FROM Category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()
        
        for categories in showing:
            print("|| ",categories," ||")

    def show_aliments(self, choice_category):
        
        query = f"SELECT id_aliment,name_aliment FROM Aliment WHERE category = {choice_category}"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result :
            print (row)

    def show_substitut(self,choice_category,choice_aliment):

        try:
            query = f"SELECT substitut FROM Aliment WHERE id_aliment = {choice_aliment} AND category = {choice_category}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            result =result[0][0]

            query_second=f"SELECT name_aliment, category, store, grade, description, link FROM Aliment WHERE id_aliment ={result}"
            self.cursor.execute(query_second)
            return self.cursor.fetchall()
        except IndexError:
            return False
    
    def show_favorite(self):
        
        querry ="SELECT * FROM Favorite"
        self.cursor.execute(querry)
        table= self.cursor.fetchall()
        for item in table:
            print(table)
    
    def add_favorite(self,result):
         with open(r"files\favorite_list.txt","ab") as written_file:
            pickle.dump(result,written_file)
        
    def terminate(self):
        sql_terminate_animal = "DROP TABLE IF EXISTS Aliment"
        sql_terminate_substitut ="DROP TABLE IF EXISTS Substitut"
        sql_terminate_favorite="DROP TABLE IF EXISTS Favorite"
        sql_terminate_category ="DROP TABLE IF EXISTS Category"

        self.cursor.execute(sql_terminate_animal)
        self.cursor.execute(sql_terminate_substitut)
        self.cursor.execute(sql_terminate_favorite)
        self.cursor.execute(sql_terminate_category)
