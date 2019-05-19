import os, mysql.connector, requests, json
import constants

class Database():
    
    def __init__(self,database,cursor):
        self.database = database
        self.cursor = cursor
    
    def create_category_table(self,categories_to_display):
        sql_formula_creation_table = "CREATE TABLE category ( id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name_category VARCHAR(100) NOT NULL, PRIMARY KEY(id_category))"
        self.cursor.execute(sql_formula_creation_table)
        
        sql_formula_values  ="INSERT INTO category (id_category,name_category) VALUES (%s,%s)"
        self.cursor.executemany(sql_formula_values,categories_to_display)
        self.database.commit()






mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="Vongola75",
    database ="projet5"
)

mycursor= mydb.cursor()
projet5= Database(mydb,mycursor)
projet5.create_category_table(constants.categories_to_display)

mydb.commit()
os.system("pause")