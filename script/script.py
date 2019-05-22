import os, mysql.connector, requests, json
import constants

class Database():
    
    def __init__(self,database,cursor):
        self.database = database
        self.cursor = cursor
    
    def create_category_table(self,categories_to_display):
        sql_formula_creation_table = "CREATE TABLE Category ( id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name_category VARCHAR(100) NOT NULL, PRIMARY KEY(id_category))"
        self.cursor.execute(sql_formula_creation_table)
        
        sql_formula_values  ="INSERT INTO category (id_category,name_category) VALUES (%s,%s)"
        self.cursor.executemany(sql_formula_values,categories_to_display)
        self.database.commit()

    def create_aliment_table(self):
        sql_aliment_table ="CREATE TABLE aliment (id_number SMALLINT UNSIGNED NOT NULL, name_aliment VARCHAR(100) NOT NULL, category SMALLINT(5) UNSIGNED NOT NULL, store VARCHAR(50), grade CHAR(1) NOT NULL, description VARCHAR(300), link VARCHAR(100) NOT NULL, CONSTRAINT fk_category_aliment FOREIGN KEY (category) REFERENCES Category(id_category), PRIMARY KEY(id_number))"
        self.cursor.execute(sql_aliment_table)
    
    def insert_values(self,category):
        link = "http://fr.openfoodfacts.org/categorie/" + category +".json"
        r = requests.get(link)
        print(r.status_code)

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="Vongola75",
    database ="projet5"
)

mycursor= mydb.cursor()
projet5= Database(mydb,mycursor)
projet5.insert_values("Pizzas")
projet5.create_category_table(constants.categories_to_display)
projet5.create_aliment_table()
mydb.commit()
os.system("pause")