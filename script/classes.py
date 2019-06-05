#This file will be used to create our classes need
#At this point only one class will be created the database
import constants, requests, mysql.connector,json
from prettytable import PrettyTable

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
            try:
                sql_category_formula ="INSERT INTO Category(id_category,name_category) VALUES (%s,%s)"
                self.cursor.executemany(sql_category_formula,constants.categories_to_display)
                self.database.commit()
                return True
            except:
                return False
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
        affichage_style = PrettyTable()
        affichage_style.field_names =["Numero","Nom"]

        show_cat = "SELECT * FROM Category ORDER BY id_category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()
        
        for categories in showing:
            affichage_style.add_row(categories)
        print(affichage_style)

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
        sql_increment ="SET @count=0"
        self.cursor.execute(sql_increment)
        sql_increment="UPDATE Aliment SET id_aliment =@count:= @count+1"
        self.cursor.execute(sql_increment)

    def show_aliments(self, choice_category):
        affichage_style = PrettyTable()
        affichage_style.field_names =["Numero","Nom"]
        query = f"SELECT id_aliment,name_aliment FROM Aliment WHERE category = {choice_category}"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result :
            affichage_style.add_row(row)
        print(affichage_style)

    def show_substitut(self,choice_category,choice_aliment):

            query_grade = f"SELECT grade FROM Aliment WHERE id_aliment = {choice_aliment} AND category ={choice_category}"
            self.cursor.execute(query_grade)
            grade = self.cursor.fetchall()
            lettre ='a'
            if grade: #If our grade list is not empty 
                grade = grade[0][0]
                
                
                while lettre <= grade: #While our grade is superior to the lettre (which starts at 'a')
                    query = f"SELECT * from aliment where (category ={choice_category} AND id_aliment != {choice_aliment}) AND grade ='{lettre}' ORDER BY RAND() LIMIT 1"
                    self.cursor.execute(query)
                    result = self.cursor.fetchall()
                    if result: #If the grade exists we stop the loop and go insert our new substitut into the table
                        id_substitut = result[0][0]
                        querry_add_sub = f"INSERT IGNORE INTO Substitut(id_substitut, id_substitut_of) VALUES ({id_substitut}, {choice_aliment})"
                        self.cursor.execute(querry_add_sub)
                        self.database.commit()
                        return result
                    else: #If the list empty
                        lettre = chr(ord(lettre)+1) #We increment our lettre
            else : 
                return None

    def show_favorite(self):
        
        affichage_style = PrettyTable()
        affichage_style.field_names=["Nom","Substitut de","Magasin","Nutriscore","Description","Lien"]
        
        querry ="SELECT * FROM Favorite"
        self.cursor.execute(querry)
        table= self.cursor.fetchall()
        for item in table:
            affichage_style.add_row(item)
        print(affichage_style)
    
    def add_favorite(self,result,choice_aliment):

        querry_get_name =f"SELECT name_aliment FROM Aliment where id_aliment = {choice_aliment}"
        self.cursor.execute(querry_get_name)
        name = self.cursor.fetchall()
        
        #We affect our result array and name to variables to avoid errors in the coming querry
        name_sub = str(name[0][0])
        name_aliment = str(result[0][1])
        store =str(result[0][3])
        grade =str(result[0][4])
        description = str(result[0][5])
        link = str(result[0][6])
        #We now insert our favorite aliment in the table

        querry_add_favorite = f"""INSERT IGNORE INTO Favorite(name_aliment,substitut_of, store, grade, description, link) VALUES ("{name_aliment}","{name_sub}","{store}","{grade}","{description}","{link}")"""
        self.cursor.execute(querry_add_favorite)
        self.database.commit()
         