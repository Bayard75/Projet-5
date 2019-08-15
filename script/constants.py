"""In this file we will find our constants such as mysql identification
along a list of the categories and product available"""

import os

working_dir = os.getcwd()  # We search and get our workig directory
path_files = os.path.join(working_dir, 'files')  # then our files directory ect
path_files_category = os.path.join(path_files, 'Category.sql')
path_files_Aliment = os.path.join(path_files, 'Aliment.sql')
path_files_Substitut = os.path.join(path_files, 'Substitut.sql')
path_files_aliment_status = os.path.join(path_files, 'aliment_status.txt')

# The user only has to enter these 4 parameters before starting the program

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Vongola75"
# -------------------------------------------------------------------------

CATEGORIES_TO_DISPLAY = [(None, "Pizzas"), (None, "volailles"),
                         (None, "snacks"), (None, "desserts"),
                         (None, "fromage"), (None, "petit-dejeuners"),
                         (None, "epicerie"), (None, "produits-a-tartiner"),
                         (None, "charcuteries")]
# -------------------------------------------------------------------------

try:
    with open(path_files_aliment_status, "r") as file:
        ALIMENT_STATUS = file.read()
except:
        ALIMENT_STATUS = "Not Done"
