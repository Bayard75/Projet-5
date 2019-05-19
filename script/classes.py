#This file will be used to create our classes need
#At this point only one class will be created the database
import constants
import script

class Database():
    
    def __init__(self,database,cursor):
        self.database = database
        self.cursor = cursor
    
    def create_category_table(self):
        sql_formula_creation_table = "CREATE TABLE cateogry ( id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name_cateogry VARCHAR(100) NOT NULL, PRIMARY KEY(id_category))"
        self.cursor.execute(sql_formula_creation_table)
