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

    def __init__(self):
        """Class that creates a db named Pur_beurre"""

        self.database = mysql.connector.connect(
                            host=constants.MYSQL_HOST,
                            user=constants.MYSQL_USER,
                            password=constants.MYSQL_PASSWORD)
        self.cursor = self.database.cursor()

        querry = """CREATE DATABASE IF NOT EXISTS pur_beurre"""
        self.cursor.execute(querry)
        querry = """USE pur_beurre"""
        self.cursor.execute(querry)


class Category_table(Database):

    def __init__(self, formula):
        """Class that creates a table for our categories
            it takes one parameters the sql formula"""

        Database.__init__(self)
        self.category_formula = formula

        try:
            self.cursor.execute(self.category_formula)
        except:
            print("""Une erreur s'est produite
            dans la création de la table Category""")

    def insert_values_category(self):
            """Method that inserts predefined
                categories into the category table"""

            # Inserting our first values into table1
            try:
                sql_category_formula = """INSERT INTO Category(id_category,name_category)
                                            VALUES (%s,%s)"""
                self.cursor.executemany(sql_category_formula, constants.CATEGORIES_TO_DISPLAY)
                self.database.commit()
                return True

            except mysql.connector.Error as e:
                if e.args[0] == 1062:  # Data already inserted
                    return
                else:
                    print("""Erreur dans l'insertion des données
                            dans la table category. Erreur : """, e)
                    return

    def show_categories(self):
        affichage_style = PrettyTable()
        affichage_style.field_names = ["Numero", "Nom"]

        show_cat = "SELECT * FROM Category ORDER BY id_category"
        self.cursor.execute(show_cat)
        showing = self.cursor.fetchall()

        for categories in showing:
            affichage_style.add_row(categories)
        print(affichage_style)


class Aliment_table(Database):

    def __init__(self, formula):

        Database.__init__(self)
        self.aliment_formula = formula

        try:
            self.cursor.execute(self.aliment_formula)
        except:
            print('''Une erreur s'est produite dans la
            création de la table Aliment''')

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

    def alter_table_aliment(self):
        """Method that deletes row where there is no grade,
         updates those where the store and description are unavailable,
         and re-increment our id_aliment"""

        sql_delete_empty = """DELETE FROM Aliment
        WHERE grade IN ('unknown','not-applicable')"""
        self.cursor.execute(sql_delete_empty)
        self.database.commit()

        sql_update_stores = """UPDATE Aliment
                                SET store = 'Non disponible'
                                WHERE store=''"""
        self.cursor.execute(sql_update_stores)
        self.database.commit()

        sql_udpate_description = """UPDATE Aliment
                                    SET description = 'Non disponible'
                                    WHERE description='' """
        self.cursor.execute(sql_udpate_description)
        self.database.commit()

    def show_aliments(self, choice_category):
        """Method that display the aliment chosen it takes 1 parametre : the category"""

        affichage_style = PrettyTable()
        affichage_style.field_names = ["Numero", "Nom"]
        query = f"""SELECT id_aliment,name_aliment FROM Aliment WHERE category = {choice_category}"""

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for row in result:
            affichage_style.add_row(row)
        print(affichage_style)

    def check_pair(self, choice_category, choice_aliment):
        """This method checks that the aliment chosen if compatible with the category chosen"""

        querry = f"""SELECT * from aliment WHERE category ={choice_category} AND id_aliment={choice_aliment}"""
        self.cursor.execute(querry)
        result = self.cursor.fetchall()
        return result

    def show_substitut(self, choice_category, choice_aliment):
        """Method that selects a substitut
            based on and aliment id and a category id"""

        querry_get_min_grade = f"""SELECT MIN(grade) FROM Aliment
                            WHERE category ={choice_category}"""
        self.cursor.execute(querry_get_min_grade)

        grade_min = self.cursor.fetchall()

        querry_get_sub = f"""SELECT id_aliment, name_aliment,
                            store, grade, description, link
                            FROM Aliment
                            WHERE(category = {choice_category} 
                            AND id_aliment != {choice_aliment})
                            AND grade ='{grade_min[0][0]}' ORDER BY RAND() LIMIT 1"""

        self.cursor.execute(querry_get_sub)
        result = self.cursor.fetchall()
        return result


class Substitut_table(Database):

    def __init__(self, formula):

        Database.__init__(self)
        self.substitut_formula = formula

        try:
            self.cursor.execute(self.substitut_formula)
        except:
            print("""" Une erreur s'est produite lors de la création
            de la table substitut""")

    def add_favorite(self, result, choice_aliment):

        querry_get_name = f"""SELECT name_aliment
                            FROM Aliment
                            WHERE id_aliment = {choice_aliment}"""
        self.cursor.execute(querry_get_name)
        name = self.cursor.fetchall()

        querry_add_sub = f'''INSERT INTO Sub(id_sub, is_sub_of)
                            VALUES({result[0][0]}, "{name[0][0]}")'''
        self.cursor.execute(querry_add_sub)
        self.database.commit()

    def show_favorite(self):

        sql = """select name_aliment, is_sub_of, store, grade, description, link
                FROM Aliment INNER JOIN Sub ON Sub.id_sub = Aliment.id_aliment"""
        self.cursor.execute(sql)
        favorite = self.cursor.fetchall()

        style = PrettyTable()
        style.field_names = ["nom", "est le substitut de",
                                "magasin", "note",
                                "description", "Lien"]
        for row in favorite:
            style.add_row(row)
            print(style)
