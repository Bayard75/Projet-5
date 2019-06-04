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
            sql_category_formula ="INSERT IGNORE INTO Category(id_category,name_category) VALUES (%s,%s)"
            self.cursor.executemany(sql_category_formula,constants.categories_to_display)
            self.database.commit()
    
    def insert_values_aliment(self):
        
        id_category = 0
        for names in constants.categories_to_display:
            for page in range(1,3):
                link = f"https://fr.openfoodfacts.org/categorie/{constants.categories_to_display[id_category][1]}/{page}.json"
                response = requests.get(link)
                category_json = json.loads(response.text)
            
                for products in category_json["products"]:
                    try:  
                        sql_formula_aliment = f"""INSERT IGNORE INTO Aliment(id_aliment,name_aliment,category,store,grade,description,link) VALUES ("{None}","{products["product_name"]}",{id_category+1},"{products["stores"]}","{products["nutrition_grades_tags"][0]}","{products["generic_name_fr"]}","{products["url"]}")"""
                        self.cursor.execute(sql_formula_aliment)
                        self.database.commit()
                
                    except KeyError:    
                        continue

            id_category +=1


    def insert_values_substitut(self):
        sql_substitut ="INSERT IGNORE INTO substitut (id_aliment,category) SELECT id_aliment, category FROM Aliment WHERE grade = 'a' OR grade ='b' OR grade ='c'  ORDER BY grade"
        self.cursor.execute(sql_substitut)
        self.database.commit()



    def show_categories(self):
        show_cat = "SELECT * FROM Category ORDER BY id_category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()
        
        for categories in showing:
            print("|| ",categories," ||")

    def alter_table_aliment(self):
        sql_delete_empty = "DELETE FROM Aliment WHERE grade IN ('unknown','not-applicable')"
        self.cursor.execute(sql_delete_empty)
        self.database.commit()

        sql_update_store = "UPDATE Aliment SET store ='Non disponible' WHERE store =''"
        sql_update_descri= "UPDATE Aliment set description ='Non disponible' WHERE description =''"
        self.cursor.execute(sql_update_descri)
        self.database.commit()
        self.cursor.execute(sql_update_store)
        self.database.commit()


    def show_aliments(self, choice_category):
        
        query = f"SELECT id_aliment,name_aliment FROM Aliment WHERE category = {choice_category}"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result :
            print (row)

    def show_substitut(self,choice_category,choice_aliment):

            query_grade = f"SELECT grade FROM Aliment WHERE id_aliment = {choice_aliment} AND category ={choice_category}"
            self.cursor.execute(query_grade)
            grade = self.cursor.fetchall()

            if grade: #If our grade list is not empty 
                query = f"SELECT * from aliment where (category ={choice_category} AND id_aliment != {choice_aliment}) AND (grade ='a' OR grade ='b' OR grade ='c' OR grade = 'd' OR grade ='e') AND grade <= '{grade[0][0]}'ORDER BY RAND() LIMIT 1"
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                id_substitut = result[0][0]
                querry_add_sub = f"INSERT IGNORE INTO Substitut(id_substitut, id_substitut_of) VALUES ({id_substitut}, {choice_aliment})"
                self.cursor.execute(querry_add_sub)
                self.database.commit()
                return result
            else : 
                return None

    def show_favorite(self):
        
        querry ="SELECT * FROM Favorite"
        self.cursor.execute(querry)
        table= self.cursor.fetchall()
        for item in table:
            print(item)
    
    def add_favorite(self,result,choice_aliment):
        querry_get_name =f"SELECT name_aliment FROM Aliment where id_aliment = {choice_aliment}"
        self.cursor.execute(querry_get_name)
        name = self.cursor.fetchall()
        
        name_sub = str(name[0][0])
        name_aliment = str(result[0][1])
        store =str(result[0][3])
        grade =str(result[0][4])
        description = str(result[0][5])
        link = str(result[0][6])

        querry_add_favorite = f"""INSERT IGNORE INTO Favorite(name_aliment,substitut_of, store, grade, description, link) VALUES ("{name_aliment}","{name_sub}","{grade}","{store}","{description}","{link}")"""
        self.cursor.execute(querry_add_favorite)
        self.database.commit()
        self.database.commit()
         