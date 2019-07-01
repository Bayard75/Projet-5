"""This file will be used to create our classes need
At this point only one class will be created the database"""

import constants
import requests
import mysql.connector
import os
import json
from prettytable import PrettyTable
from mysql.connector.errors import Error


class Database():

    def __init__(self, database, cursor, table1_formula, table2_formula):
        """Class that creates 4 tables on initiation"""
        self.database = database
        self.cursor = cursor

        #  creating our two tables
        try:
            self.cursor.execute(table1_formula)
            self.cursor.execute(table2_formula)
        except:
            print("Erreur dans la creation des tables.")
            quit()

    def insert_values_category(self):
            """Method that inserts predefined categories into the category table"""

            # Inserting our first values into table1
            try:
                sql_category_formula = "INSERT INTO Category(id_category,name_category) VALUES (%s,%s)"
                self.cursor.executemany(sql_category_formula, constants.CATEGORIES_TO_DISPLAY)
                self.database.commit()
                return True

            except mysql.connector.Error as e:
                if e.args[0] == 1062:
                    return  # 1062 means that our values have already been inserted
                else:
                    print("Erreur dans l'insertion des données dans la table category. Erreur : ", e)
                    return

    def insert_values_aliment(self):
        """Method that inserts our aliemnt into the aliment table
            by searching through our API : Openfoodfacts"""

        id_category = 0
        for names in constants.CATEGORIES_TO_DISPLAY:
            # We get our aliment based on our categories
            for page in range(1, 4):
                link = f"https://fr.openfoodfacts.org/categorie/{constants.CATEGORIES_TO_DISPLAY[id_category][1]}/{page}.json"
                response = requests.get(link)
                category_json = json.loads(response.text)

                for products in category_json["products"]:
                    try:
                        sql_formula_aliment = f"""INSERT IGNORE INTO Aliment(id_aliment,name_aliment,category,store,grade,description,link) VALUES (
                            '{None}',"{products["product_name"]}",{id_category+1},"{products["stores"]}","{products["nutrition_grades_tags"][0]}",
                            "{products["generic_name_fr"]}","{products["url"]}")"""

                        self.cursor.execute(sql_formula_aliment)

                    except KeyError:
                        continue
                    except mysql.connector.Error as e:
                            print("Erreur rencontrée : ", e)
                    self.database.commit()

            id_category += 1

        with open(constants.path_files_aliment_status, "w") as file:
            # Once inserted we create a file to keep track of that status
            file.write("Done")

    def show_categories(self):
        affichage_style = PrettyTable()
        affichage_style.field_names = ["Numero", "Nom"]

        show_cat = "SELECT * FROM Category ORDER BY id_category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()

        for categories in showing:
            affichage_style.add_row(categories)
        print(affichage_style)

    def alter_table_aliment(self):
        """Method that deletes row where there is no grade, updates those were the store and description our unavailable,the re_increment our id_aliment"""

        sql_delete_empty = "DELETE FROM Aliment WHERE grade IN ('unknown','not-applicable')"
        self.cursor.execute(sql_delete_empty)
        self.database.commit()

        sql_update_store = "UPDATE Aliment SET store ='Non disponible' WHERE store =''"
        sql_update_descri = "UPDATE Aliment set description ='Non disponible' WHERE description =''"
        self.cursor.execute(sql_update_descri)
        self.database.commit()
        self.cursor.execute(sql_update_store)
        self.database.commit()

        sql_increment = "SET @count=0"
        self.cursor.execute(sql_increment)
        sql_increment = "UPDATE Aliment SET id_aliment =@count:= @count+1"
        self.cursor.execute(sql_increment)
        self.database.commit()

    def show_aliments(self, choice_category):
        """Method that display the aliment chosen it takes 1 parametre : the category"""

        affichage_style = PrettyTable()
        affichage_style.field_names =["Numero", "Nom"]
        query = f"SELECT id_aliment,name_aliment FROM Aliment WHERE category = {choice_category}"

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result:
            affichage_style.add_row(row)
        print(affichage_style)

    def show_substitut(self, choice_category, choice_aliment):
        """Method that selects a substitut
            based on and aliment id and a category id"""

        querry_get_min_grade = f"""SELECT MIN(grade) FROM Aliment
                            WHERE category ={choice_category}"""
        self.cursor.execute(querry_get_min_grade)

        grade_min = self.cursor.fetchall()

        querry_get_sub = f"""SELECT * FROM Aliment
                            WHERE(category = {choice_category} 
                            AND id_aliment != {choice_aliment})
                            AND grade ='{grade_min}' ORDER BY RAND() LIMIT 1"""

        self.cursor.execute(querry_get_sub)
        result = self.cursor.fetchall()
        return result

    def show_favorite(self):

        affichage_style = PrettyTable()
        affichage_style.field_names = ["Nom", "Substitut de", "Magasin", "Nutriscore", "Description", "Lien"]

        querry = "SELECT name_aliment,substitut_of, store, grade, description, link FROM Aliment WHERE favorite = 1"
        self.cursor.execute(querry)
        table = self.cursor.fetchall()
        for item in table:
            affichage_style.add_row(item)
        print(affichage_style)

    def add_favorite(self, result, choice_aliment):

        querry_get_name = f"""SELECT name_aliment
                            FROM Aliment
                            WhERE id_aliment = {choice_aliment}"""
        self.cursor.execute(querry_get_name)
        name = self.cursor.fetchall()

        querry_add_substitut_of = f"UPDATE Aliment SET substitut_of ='{name[0][0]}' WHERE name_aliment = '{result[0][0]}'"
        self.cursor.execute(querry_add_substitut_of)
        self.database.commit()

        querry_add_favorite = f"UPDATE Aliment SET favorite = 1 WHERE name_aliment = '{result[0][0]}'"
        self.cursor.execute(querry_add_favorite)
        self.database.commit()